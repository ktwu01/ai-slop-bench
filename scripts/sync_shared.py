#!/usr/bin/env python3
"""Copy the shared environment and checker files into every task.

Harbor tasks are meant to be self-contained, so each task carries its own copy
of the checker rather than importing from this repo. This script is the single
writer of those copies; `--check` fails when a task has drifted, which is what
CI should run.

    python3 scripts/sync_shared.py
    python3 scripts/sync_shared.py --check
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED_TESTS = ROOT / "shared" / "tests"
SHARED_DOCKERFILE = ROOT / "shared" / "environment" / "Dockerfile"
TASKS = ROOT / "tasks"

SHARED_TEST_FILES = ("test.sh", "slopcheck.py", "grade.py", "test_output.py")


def test_dirs(task: Path) -> list[Path]:
    """Every directory that needs a verifier: the task's, or each step's."""
    steps = sorted((task / "steps").glob("*/tests"))
    return steps if steps else [task / "tests"]


def targets() -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    for task in sorted(p for p in TASKS.iterdir() if (p / "task.toml").exists()):
        pairs.append((SHARED_DOCKERFILE, task / "environment" / "Dockerfile"))
        for tests in test_dirs(task):
            for name in SHARED_TEST_FILES:
                pairs.append((SHARED_TESTS / name, tests / name))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = parser.parse_args()

    drifted: list[Path] = []
    for src, dst in targets():
        if args.check:
            if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
                drifted.append(dst)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        if dst.suffix == ".sh":
            dst.chmod(0o755)

    if args.check:
        for path in drifted:
            print(f"out of sync: {path.relative_to(ROOT)}")
        print(f"{len(drifted)} file(s) out of sync")
        return 1 if drifted else 0

    print(f"synced {len(targets())} file(s) across {len(list(TASKS.iterdir()))} task(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
