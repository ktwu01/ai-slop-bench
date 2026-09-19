#!/usr/bin/env python3
"""Run the codex CLI as a solver on every task, then grade it with the real checker.

This is the difficulty measurement. `scripts/selfcheck.py` only proves the tasks
are solvable and the rules fire; it says nothing about whether a real agent
passes them. This script answers that.

Each unit runs in its own temp directory. The only edit to the delivered
instruction is the output path: the task says `/app/output.txt`, which exists
only inside the Harbor container, so here the agent writes `output.txt` in its
working directory. Nothing else about the prompt changes.

The multi-step task is run as two turns of one session (`codex exec resume`), so
the second turn really has to remember the first turn's constraints.

    python3 dev/run_agent_codex.py                # all units
    python3 dev/run_agent_codex.py protected-quote  # one task

Results land in `dev/agent_runs/<timestamp>/`: the prompt, the delivered text,
the grader output and a summary JSON per unit.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from selfcheck import grade, units  # noqa: E402

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


def run_codex(workdir: Path, prompt: str, resume_session: str | None) -> tuple[str | None, str]:
    """Run one codex turn. Returns (session_id, raw jsonl)."""
    # Shared options go before the subcommand: `codex exec resume` rejects -C.
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "-C",
        str(workdir),
        "--sandbox",
        "workspace-write",
        "--json",
    ]
    if resume_session:
        cmd += ["resume", resume_session]
    cmd += [prompt]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=TIMEOUT_SEC, cwd=str(workdir)
    )
    raw = proc.stdout + proc.stderr
    if proc.returncode != 0 and "thread.started" not in proc.stdout:
        raise RuntimeError(f"codex turn did not run (exit {proc.returncode}):\n{raw[:2000]}")
    session = resume_session
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started" and event.get("thread_id"):
            session = event["thread_id"]
    return session, raw


def deliver(workdir: Path) -> str | None:
    path = workdir / "output.txt"
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("only", nargs="*", help="task directory names; default all")
    args = parser.parse_args()

    if not shutil.which("codex"):
        print("codex CLI not on PATH; cannot measure difficulty", file=sys.stderr)
        return 2

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    outdir = ROOT / "dev" / "agent_runs" / stamp
    outdir.mkdir(parents=True, exist_ok=True)

    by_task: dict[str, list[tuple[str, Path, Path]]] = {}
    for key, tests_dir, solution_dir in units():
        by_task.setdefault(key.split("/")[0], []).append((key, tests_dir, solution_dir))

    selected = sorted(by_task) if not args.only else [t for t in sorted(by_task) if t in args.only]
    if not selected:
        print(f"no such task: {args.only}", file=sys.stderr)
        return 2

    summary: list[dict] = []
    for task in selected:
        workdir = Path(tempfile.mkdtemp(prefix=f"slop-{task}-"))
        session: str | None = None
        for key, tests_dir, _ in by_task[task]:
            slug = key.replace("/", "__")
            step_dir = tests_dir.parent
            prompt = prompt_for(step_dir / "instruction.md")
            (outdir / f"{slug}.prompt.txt").write_text(prompt, encoding="utf-8")
            try:
                session, raw = run_codex(workdir, prompt, session)
            except subprocess.TimeoutExpired:
                session, raw = session, "TIMEOUT"
            (outdir / f"{slug}.codex.jsonl").write_text(raw, encoding="utf-8")

            answer = deliver(workdir)
            if answer is None:
                record = {"unit": key, "reward": 0.0, "failed": ["no_output_file"]}
                print(f"FAIL  {key}: 没有产出 output.txt")
            else:
                (outdir / f"{slug}.output.txt").write_text(answer, encoding="utf-8")
                reward, failed, stdout = grade(tests_dir, answer)
                (outdir / f"{slug}.grade.txt").write_text(stdout, encoding="utf-8")
                record = {"unit": key, "reward": reward, "failed": sorted(failed)}
                verdict = "PASS" if reward == 1.0 else "FAIL"
                print(f"{verdict}  {key}: reward={reward} failed={sorted(failed)}")
            summary.append(record)

    # The multi-step task's trial reward is its final step.
    trials: dict[str, float] = {}
    for record in summary:
        trials[record["unit"].split("/")[0]] = record["reward"]
    passed = sum(1 for r in trials.values() if r == 1.0)
    print(f"\n{passed}/{len(trials)} 个任务通过（多步任务以最后一步计分）")

    (outdir / "summary.json").write_text(
        json.dumps(
            {"units": summary, "tasks": trials, "passed": passed, "total": len(trials)},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"详细记录：{outdir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
