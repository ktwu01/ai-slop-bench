#!/usr/bin/env python3
"""Report what the task set currently contains, derived from the tree.

Design docs describe intent and stay valid as the set changes. Status is read
from disk here so it cannot go stale in prose.

    python3 scripts/status.py
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASKS = ROOT / "examples" / "tasks"
OBSERVATIONS = ROOT / "examples" / "observations"


def rubric_version(task_dir):
    rubric = task_dir / "rubric.md"
    if not rubric.exists():
        return None
    m = re.search(r"[Rr]ubric:?\s*`?([0-9]+\.[0-9]+)`?", rubric.read_text())
    return m.group(1) if m else None


def outcome(data):
    """Reward is computed from the judgments, not stored in the review."""
    verdicts = [v.get("verdict") for v in data.get("style", {}).values()]
    for key in ("validity", "fidelity", "task_fitness"):
        if key in data:
            verdicts.append(data[key].get("verdict"))
    if "fail" in verdicts:
        return "reward=0"
    if "unresolved" in verdicts:
        return "reward=null (unresolved)"
    return "reward=1"


def observations_for(task_id):
    """An observation counts for a task when its review names that task_id."""
    hits = []
    for review in sorted(OBSERVATIONS.glob("*.review.json")):
        try:
            data = json.loads(review.read_text())
        except json.JSONDecodeError:
            continue
        if data.get("task_id") == task_id:
            hits.append((review.name, outcome(data)))
    return hits


def main():
    if not TASKS.is_dir():
        print(f"no task directory at {TASKS}", file=sys.stderr)
        return 1

    task_dirs = sorted(d for d in TASKS.iterdir() if d.is_dir())
    print(f"tasks: {len(task_dirs)}")
    for d in task_dirs:
        version = rubric_version(d) or "?"
        parts = [f"  {d.name}  rubric {version}"]
        missing = [f for f in ("prompt.md", "rubric.md") if not (d / f).exists()]
        if missing:
            parts.append(f"MISSING {', '.join(missing)}")
        obs = observations_for(d.name)
        parts.append(f"{len(obs)} observation(s)" if obs else "untested")
        print("  ".join(parts))
        for name, result in obs:
            print(f"      {name}  {result}")

    loose = sorted(OBSERVATIONS.glob("*.review.json")) if OBSERVATIONS.is_dir() else []
    claimed = {n for d in task_dirs for n, _ in observations_for(d.name)}
    orphans = [r.name for r in loose if r.name not in claimed]
    if orphans:
        print(f"\nobservations not matched to a task ({len(orphans)}):")
        for name in orphans:
            print(f"  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
