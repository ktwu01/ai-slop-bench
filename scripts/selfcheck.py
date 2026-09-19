#!/usr/bin/env python3
"""Grade every reference answer and every counterexample, without Docker.

Two things must hold before a task is worth running against a model:

1. the committed `solution/solve.sh` answer scores 1.0, so the task is solvable
   and the checker is not accidentally impossible;
2. each counterexample in `dev/fixtures.py` scores 0.0 *and* is caught by the
   rule that is supposed to catch it, so a rule cannot silently stop working.

This runs the real `tests/grade.py` entrypoint as a subprocess, so it exercises
the same code path the Harbor verifier uses.

    python3 scripts/selfcheck.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "dev"))

from fixtures import FAILING  # noqa: E402

HEREDOC = re.compile(r"<<'TXT'\n(.*?)\nTXT\n", re.DOTALL)


def units() -> list[tuple[str, Path, Path]]:
    """(key, tests_dir, solution_dir) for each gradeable unit."""
    out: list[tuple[str, Path, Path]] = []
    for task in sorted(p for p in (ROOT / "tasks").iterdir() if (p / "task.toml").exists()):
        steps = sorted((task / "steps").glob("*"))
        if steps:
            for step in steps:
                out.append((f"{task.name}/{step.name}", step / "tests", step / "solution"))
        else:
            out.append((task.name, task / "tests", task / "solution"))
    return out


def reference_answer(solution_dir: Path) -> str:
    match = HEREDOC.search((solution_dir / "solve.sh").read_text(encoding="utf-8"))
    if not match:
        raise SystemExit(f"no TXT heredoc in {solution_dir / 'solve.sh'}")
    return match.group(1) + "\n"


def grade(tests_dir: Path, answer: str) -> tuple[float, set[str], str]:
    """Run grade.py on `answer`; return (reward, failed rule names, stdout)."""
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        out_file = tmpdir / "output.txt"
        out_file.write_text(answer, encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(tests_dir / "grade.py")],
            capture_output=True,
            text=True,
            env={
                "SLOPCHECK_REWARD_DIR": str(tmpdir),
                "SLOPCHECK_OUTPUT_PATH": str(out_file),
                "PATH": "/usr/bin:/bin",
                "PYTHONIOENCODING": "utf-8",
            },
        )
        reward_path = tmpdir / "reward.json"
        if not reward_path.exists():
            raise SystemExit(f"grade.py wrote no reward\n{proc.stdout}\n{proc.stderr}")
        reward = json.loads(reward_path.read_text(encoding="utf-8"))["reward"]
        failed = {
            m.group(1)
            for m in re.finditer(r"^  FAIL  (\S+):", proc.stdout, re.MULTILINE)
        }
        return reward, failed, proc.stdout


def main() -> int:
    problems: list[str] = []
    checked = 0

    for key, tests_dir, solution_dir in units():
        reward, failed, stdout = grade(tests_dir, reference_answer(solution_dir))
        checked += 1
        if reward != 1.0:
            problems.append(
                f"{key}: 参照答案未通过，失败规则 {sorted(failed)}\n{stdout}"
            )
        else:
            print(f"ok    {key}: 参照答案通过")

        for label, answer, expected_rule in FAILING.get(key, []):
            reward, failed, stdout = grade(tests_dir, answer)
            checked += 1
            if reward != 0.0:
                problems.append(f"{key} / {label}: 反例竟然通过了\n{stdout}")
            elif expected_rule not in failed:
                problems.append(
                    f"{key} / {label}: 期望 {expected_rule} 判失败，实际失败规则 "
                    f"{sorted(failed)}\n{stdout}"
                )
            else:
                print(f"ok    {key} / {label}: 被 {expected_rule} 判失败")

    print(f"\n{checked} 个样例已评分")
    for problem in problems:
        print(f"\nPROBLEM {problem}")
    if problems:
        print(f"\n{len(problems)} 个问题")
        return 1
    print("全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
