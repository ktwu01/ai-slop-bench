#!/usr/bin/env python3
"""Run the codex CLI as a solver on every task, then grade it with the real checker.

This is the difficulty measurement. `scripts/selfcheck.py` only proves the tasks
are solvable and the rules fire; it says nothing about whether a real agent
passes them. This script answers that.

Each unit runs in its own temp directory. The only edit to the delivered
instruction is the output path: the task says `/app/output.txt`, which exists
only inside the Harbor container, so here the agent writes `output.txt` in its
working directory. Nothing else about the prompt changes.

The multi-step task runs all three steps in one session (`codex exec resume`),
so later turns must retain the earlier constraints. Infrastructure errors are
recorded separately and excluded from pass-rate denominators.

    python3 dev/run_agent_codex.py                     # all units, one draw
    python3 dev/run_agent_codex.py protected-quote     # one task
    python3 dev/run_agent_codex.py --repeat 10         # ten draws per task

A single draw does not measure a pass rate. A model that truly passes 90% of
the time clears nine independent attempts about 39% of the time, so one green
sweep is consistent with a task that fails one run in ten. `--repeat` samples
each task k times and reports passes/k, which is the number worth quoting.

Results land in `dev/agent_runs/<timestamp>/`: the prompt, the delivered text,
the grader output and a summary JSON per unit.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import hashlib
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from selfcheck import grade, grade_file, units  # noqa: E402

# Kept out of the task text on purpose: this is harness scaffolding, not part of
# what the task asks for.
PREAMBLE = """你在完成一项中文写作任务。请严格按下面的要求写，然后把最终交付内容写入当前工作目录下的 output.txt。

只凭这段提示作答。不要去文件系统里寻找评分脚本、测试或参考答案，也不要读取或执行 ~/.claude/、~/.agents/、.claude/skills/、agents/ 下的任何文件，不要修改 agents/openai.yaml。

任务要求如下。

"""

TIMEOUT_SEC = 600


def prompt_for(instruction: Path) -> str:
    text = instruction.read_text(encoding="utf-8")
    text = text.replace("`/app/output.txt`", "`output.txt`").replace("/app/output.txt", "output.txt")
    return PREAMBLE + text


class TurnError(RuntimeError):
    def __init__(self, reason: str, raw: str = ""):
        super().__init__(reason)
        self.raw = raw


def run_codex(workdir: Path, prompt: str, resume_session: str | None,
              model: str | None = None, reasoning_effort: str | None = None) -> tuple[str, str]:
    """Accept only a successful, completed turn with the expected session."""
    cmd = ["codex", "exec", "--skip-git-repo-check", "-C", str(workdir),
           "--sandbox", "workspace-write", "--json"]
    if resume_session:
        cmd += ["resume", resume_session]
    if model:
        cmd += ["--model", model]
    if reasoning_effort:
        cmd += ["-c", f'model_reasoning_effort={json.dumps(reasoning_effort)}']
    cmd += [prompt]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_SEC,
                              cwd=str(workdir), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired as exc:
        def decode(value):
            return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
        raw = decode(exc.stdout) + decode(exc.stderr)
        # A recorded service failure is infrastructure; a bare elapsed solver
        # budget is a scored failure, even when partial output exists.
        for line in decode(exc.stdout).splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(event, dict) and event.get("type") in {"turn.failed", "error"}:
                raise TurnError("failed_event_before_timeout", raw) from exc
        raise TurnError("timeout", raw) from exc
    except OSError as exc:
        raise TurnError(f"launch_error: {exc}") from exc
    raw = proc.stdout + proc.stderr
    if proc.returncode != 0:
        raise TurnError(f"nonzero_exit: {proc.returncode}", raw)
    session = None
    completed = False
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        if event.get("type") in {"turn.failed", "error"}:
            raise TurnError("failed_event", raw)
        if event.get("type") == "thread.started" and event.get("thread_id"):
            session = event["thread_id"]
        if event.get("type") == "turn.completed":
            completed = True
    if not completed:
        raise TurnError("missing_turn_completed", raw)
    if not session:
        raise TurnError("missing_session", raw)
    if resume_session and session != resume_session:
        raise TurnError("resume_session_mismatch", raw)
    return session, raw


def session_metadata(session: str) -> dict:
    """Read only model-related context from this exact CLI session's rollout."""
    home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    evidence = []
    for path in (home / "sessions").glob(f"**/*{session}.jsonl"):
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                event = json.loads(line)
                if event.get("type") == "turn_context":
                    payload = event.get("payload", {})
                    evidence.append({key: payload[key] for key in
                                     ("model", "effort", "reasoning_effort") if key in payload})
        except (OSError, ValueError):
            continue
    return {"source": "session_turn_context", "contexts": evidence,
            "effective_model_verified": any(item.get("model") for item in evidence)}


def task_hashes(task: str) -> dict[str, str]:
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted((ROOT / "tasks" / task).rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts}


def archive_delivery(path: Path, destination: Path) -> dict:
    """Bound artifact capture without following symlinks or decoding bytes."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return {"kind": "missing"}
    if stat.S_ISLNK(info.st_mode):
        return {"kind": "symlink", "target": os.readlink(path)}
    if not stat.S_ISREG(info.st_mode):
        return {"kind": "nonregular", "mode": info.st_mode}
    with path.open("rb") as source:
        data = source.read(64 * 1024 + 1)
    destination.write_bytes(data)
    return {"kind": "regular", "size": info.st_size, "captured_bytes": len(data),
            "truncated": info.st_size > len(data)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("only", nargs="*", help="task directory names; default all")
    parser.add_argument("--repeat", type=int, default=1, help="independent draws per task")
    parser.add_argument("--model", help="explicit Codex model; omitted means CLI default")
    parser.add_argument("--reasoning-effort", help="explicit model_reasoning_effort override")
    args = parser.parse_args()
    if args.repeat < 1:
        parser.error("--repeat must be positive")
    by_task: dict[str, list[tuple[str, Path, Path]]] = {}
    for key, tests_dir, solution_dir in units():
        by_task.setdefault(key.split("/")[0], []).append((key, tests_dir, solution_dir))
    unknown = set(args.only) - set(by_task)
    if unknown:
        parser.error(f"unknown tasks: {', '.join(sorted(unknown))}")
    selected = sorted(set(args.only) if args.only else by_task)
    if not selected:
        parser.error("no tasks available")
    if not shutil.which("codex"):
        print("codex CLI not on PATH; cannot measure difficulty", file=sys.stderr)
        return 2

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    outdir = ROOT / "dev" / "agent_runs" / stamp
    outdir.mkdir(parents=True)
    version = subprocess.run(["codex", "--version"], capture_output=True, text=True, timeout=30)
    metadata = {"started_at": stamp, "requested_model": args.model,
                "requested_reasoning_effort": args.reasoning_effort,
                "cli_version": version.stdout.strip(), "timeout_seconds": TIMEOUT_SEC,
                "task_hashes": {task: task_hashes(task) for task in selected},
                "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "measurement": "local Codex CLI proxy; not Harbor runtime"}
    summary: list[dict] = []
    draws: dict[str, list[float | None]] = {t: [] for t in selected}

    def checkpoint(status="running"):
        rates = {t: sum(r == 1.0 for r in values) / len(values)
                 for t, raw in draws.items() if (values := [r for r in raw if r is not None])}
        data = {"metadata": metadata, "status": status, "units": summary, "draws": draws,
                "pass_rate": rates, "repeat": args.repeat,
                "infrastructure_errors": sum(r["status"] == "infrastructure_error" for r in summary)}
        temp = outdir / "summary.json.tmp"
        temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        temp.replace(outdir / "summary.json")

    checkpoint()
    print(f"Results: {outdir}", flush=True)
    for draw in range(args.repeat):
        for task in selected:
            with tempfile.TemporaryDirectory(prefix=f"slop-{task}-") as tmp:
                workdir = Path(tmp)
                session = None
                final = None
                blocked = False
                for key, tests_dir, _ in by_task[task]:
                    slug = f"{key.replace('/', '__')}.r{draw}"
                    prompt = prompt_for(tests_dir.parent / "instruction.md")
                    (outdir / f"{slug}.prompt.txt").write_text(prompt, encoding="utf-8")
                    record = {"unit": key, "draw": draw, "reward": None, "failed": [],
                              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
                    if blocked:
                        record.update(status="skipped", error="previous_turn_did_not_complete")
                    else:
                        try:
                            session, raw = run_codex(workdir, prompt, session,
                                                     args.model, args.reasoning_effort)
                            (outdir / f"{slug}.codex.jsonl").write_text(raw, encoding="utf-8")
                            record.update(session_id=session, model_evidence=session_metadata(session))
                            if task_hashes(task) != metadata["task_hashes"][task]:
                                raise ValueError("task_content_changed_during_run")
                            artifact = workdir / "output.txt"
                            reward, failed, stdout, scores = grade_file(tests_dir, artifact)
                            (outdir / f"{slug}.grade.txt").write_text(stdout, encoding="utf-8")
                            record["scores"] = scores
                            try:
                                record["artifact"] = archive_delivery(artifact, outdir / f"{slug}.output.txt")
                            except OSError as exc:
                                record["artifact"] = {"capture_error": str(exc)}
                            if task_hashes(task) != metadata["task_hashes"][task]:
                                raise ValueError("task_content_changed_during_grading")
                            record.update(status="graded", reward=reward, failed=sorted(failed))
                            final = reward
                        except (TurnError, OSError, ValueError, subprocess.TimeoutExpired, SystemExit) as exc:
                            if isinstance(exc, TurnError):
                                (outdir / f"{slug}.codex.jsonl").write_text(exc.raw, encoding="utf-8")
                            blocked = True
                            if isinstance(exc, TurnError) and str(exc) == "timeout":
                                record.update(status="timeout", reward=0.0, failed=["solver_timeout"], error=str(exc))
                                final = 0.0
                            else:
                                record.update(status="infrastructure_error", error=str(exc))
                                final = None
                    summary.append(record)
                    (outdir / f"{slug}.result.json").write_text(
                        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
                    checkpoint()
                    print(f"{record['status']}  {key} #{draw}: reward={record['reward']} "
                          f"failed={record['failed']} {record.get('error', '')}", flush=True)
                draws[task].append(final)
                checkpoint()
    checkpoint("completed")
    for task, raw in draws.items():
        valid = [r for r in raw if r is not None]
        print(f"{sum(r == 1.0 for r in valid)}/{len(valid)}  {task} "
              f"({len(raw) - len(valid)} infrastructure errors excluded)")
    print(f"Results: {outdir}")
    return 2 if any(r["status"] == "infrastructure_error" for r in summary) else 0


if __name__ == "__main__":
    sys.exit(main())
