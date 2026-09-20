#!/usr/bin/env python3
"""Validate an editorial review and apply its all-or-nothing score gate."""

from __future__ import annotations

import json
from pathlib import Path
import sys

POLICY_VERSION = "strict-v1"
STYLE_CHECKS_BY_RUBRIC = {
    "0.2": ("S1", "S2", "S3", "S4"),
    "0.3": ("S1", "S2", "S3", "S4", "S5", "S6", "S7"),
}
OTHER_CHECKS = ("validity", "fidelity", "task_fitness")
VERDICTS = {"pass", "fail", "unresolved"}
EXIT_CODES = {"pass": 0, "fail": 1, "unresolved": 2}


class InvalidReview(ValueError):
    """The review cannot be scored because its structure is invalid."""


def require_text(value: object, location: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise InvalidReview(f"{location} must be a nonempty string")


def validate_judgment(value: object, location: str, answer: str, *, style: bool) -> str:
    if not isinstance(value, dict):
        raise InvalidReview(f"{location} must be an object")
    verdict = value.get("verdict")
    if not isinstance(verdict, str) or verdict not in VERDICTS:
        raise InvalidReview(f"{location}.verdict must be pass, fail, or unresolved")
    require_text(value.get("reason"), f"{location}.reason")
    if style:
        evidence = value.get("evidence")
        if not isinstance(evidence, list):
            raise InvalidReview(f"{location}.evidence must be a list")
        for index, item in enumerate(evidence):
            item_location = f"{location}.evidence[{index}]"
            if not isinstance(item, dict):
                raise InvalidReview(f"{item_location} must be an object")
            require_text(item.get("quote"), f"{item_location}.quote")
            require_text(item.get("reason"), f"{item_location}.reason")
            if item["quote"] not in answer:
                raise InvalidReview(f"{item_location}.quote must occur exactly in answer")
        if verdict == "fail" and not evidence:
            raise InvalidReview(f"{location}: a style failure requires evidence")
    return verdict


def score_review(review: object) -> dict:
    """Score supplied judgments without independently deciding their truth."""
    if not isinstance(review, dict):
        raise InvalidReview("review must be an object")
    rubric_version = review.get("rubric_version")
    if not isinstance(rubric_version, str) or rubric_version not in STYLE_CHECKS_BY_RUBRIC:
        raise InvalidReview("rubric_version must be '0.2' or '0.3'")
    if review.get("policy_version") != POLICY_VERSION:
        raise InvalidReview(f"policy_version must be {POLICY_VERSION!r}")
    style_checks = STYLE_CHECKS_BY_RUBRIC[rubric_version]
    answer = review.get("answer")
    if not isinstance(answer, str):
        raise InvalidReview("answer must be a string")
    style = review.get("style")
    if not isinstance(style, dict) or set(style) != set(style_checks):
        raise InvalidReview(f"style must contain exactly {', '.join(style_checks)}")

    judgments = {
        f"style.{name}": validate_judgment(style[name], f"style.{name}", answer, style=True)
        for name in style_checks
    }
    judgments.update({
        name: validate_judgment(review.get(name), name, answer, style=False)
        for name in OTHER_CHECKS
    })
    if not answer.strip() and judgments["validity"] != "fail":
        raise InvalidReview("an empty answer requires validity=fail")
    failed = [name for name, verdict in judgments.items() if verdict == "fail"]
    unresolved = [name for name, verdict in judgments.items() if verdict == "unresolved"]
    overall = "fail" if failed else "unresolved" if unresolved else "pass"
    return {
        "rubric_version": rubric_version,
        "policy_version": POLICY_VERSION,
        "overall": overall,
        "reward": {"pass": 1, "fail": 0, "unresolved": None}[overall],
        "failed_checks": failed,
        "unresolved_checks": unresolved,
    }


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InvalidReview(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise InvalidReview(f"invalid JSON constant: {value}")


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    try:
        if len(args) != 1:
            raise InvalidReview("usage: python3 scripts/score_review.py REVIEW.json (or - for stdin)")
        raw = sys.stdin.read() if args[0] == "-" else Path(args[0]).read_text(encoding="utf-8")
        review = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)
        result = score_review(review)
    except (ValueError, OSError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 3
    print(json.dumps(result, ensure_ascii=False))
    return EXIT_CODES[result["overall"]]


if __name__ == "__main__":
    raise SystemExit(main())
