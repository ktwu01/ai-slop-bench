"""Integrity checks for the direct-answer review gate; no model calls."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from score_review import InvalidReview, score_review  # noqa: E402


def passing_review(rubric_version: str = "0.2") -> dict:
    answer = "回复由客服撰写，工具不会自动发给客户。"
    style_checks = ("S1", "S2", "S3", "S4")
    if rubric_version == "0.3":
        style_checks += ("S5", "S6", "S7")
    return {
        "rubric_version": rubric_version,
        "policy_version": "strict-v1",
        "answer": answer,
        "style": {
            name: {"verdict": "pass", "reason": "No confirmed defect in this family.", "evidence": []}
            for name in style_checks
        },
        "validity": {"verdict": "pass", "reason": "The response is available for review."},
        "fidelity": {"verdict": "pass", "reason": "The supplied responsibility and sending limits remain."},
        "task_fitness": {"verdict": "pass", "reason": "The requested sentence is usable."},
    }


class ScoreReviewTests(unittest.TestCase):
    def test_necessary_negation_with_justification_can_pass(self):
        review = passing_review()
        review["style"]["S3"]["evidence"] = [{
            "quote": "工具不会自动发给客户",
            "reason": "This states a required boundary once without an emphasis preface or repeated disclaimer.",
        }]
        self.assertEqual(score_review(review), {
            "rubric_version": "0.2", "policy_version": "strict-v1",
            "overall": "pass", "reward": 1, "failed_checks": [], "unresolved_checks": [],
        })

    def test_every_single_failure_vetoes_all_other_passes(self):
        for name in ("S1", "S2", "S3", "S4", "validity", "fidelity", "task_fitness"):
            with self.subTest(name=name):
                review = passing_review()
                judgment = review["style"][name] if name.startswith("S") else review[name]
                judgment["verdict"] = "fail"
                judgment["reason"] = "A reviewer confirmed a defect."
                if name.startswith("S"):
                    judgment["evidence"] = [{"quote": "回复", "reason": "The reviewed defect occurs here."}]
                result = score_review(review)
                self.assertEqual(result["overall"], "fail")
                self.assertEqual(result["reward"], 0)
                self.assertEqual(result["failed_checks"], [f"style.{name}" if name.startswith("S") else name])

    def test_full_defensive_passage_receives_zero(self):
        review = passing_review()
        review["answer"] = "工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息。"
        review["style"]["S3"] = {
            "verdict": "fail", "reason": "A chained disclaimer defensively overframes the tool's role.",
            "evidence": [{"quote": review["answer"], "reason": "The restriction and two negative assurances form one passage."}],
        }
        result = score_review(review)
        self.assertEqual((result["overall"], result["reward"]), ("fail", 0))
        self.assertEqual(result["failed_checks"], ["style.S3"])

    def test_each_unresolved_check_prevents_a_pass(self):
        for name in ("S1", "S2", "S3", "S4", "validity", "fidelity", "task_fitness"):
            with self.subTest(name=name):
                review = passing_review()
                judgment = review["style"][name] if name.startswith("S") else review[name]
                judgment["verdict"] = "unresolved"
                judgment["reason"] = "Required context is missing."
                result = score_review(review)
                self.assertEqual(result["overall"], "unresolved")
                self.assertIsNone(result["reward"])
                self.assertEqual(result["unresolved_checks"], [f"style.{name}" if name.startswith("S") else name])

    def test_fail_takes_precedence_but_retains_unresolved_checks(self):
        review = passing_review()
        review["fidelity"]["verdict"] = "fail"
        review["style"]["S2"]["verdict"] = "unresolved"
        result = score_review(review)
        self.assertEqual(result["overall"], "fail")
        self.assertEqual(result["reward"], 0)
        self.assertEqual(result["failed_checks"], ["fidelity"])
        self.assertEqual(result["unresolved_checks"], ["style.S2"])

    def test_empty_answer_cannot_be_marked_valid(self):
        for answer in ("", " \n\t"):
            for verdict in ("pass", "unresolved"):
                review = passing_review()
                review["answer"] = answer
                review["validity"]["verdict"] = verdict
                with self.subTest(answer=answer, verdict=verdict), self.assertRaises(InvalidReview):
                    score_review(review)
        review = passing_review()
        review["answer"] = ""
        review["validity"] = {"verdict": "fail", "reason": "The answer is empty."}
        self.assertEqual(score_review(review)["reward"], 0)

    def test_all_required_top_level_fields(self):
        for key in passing_review():
            with self.subTest(key=key):
                review = passing_review()
                del review[key]
                with self.assertRaises(InvalidReview):
                    score_review(review)

    def test_versions_shape_and_labels(self):
        cases = [[], None, "review", 1]
        for field, value in (
            ("rubric_version", "0.1"), ("policy_version", "lenient"),
            ("answer", None), ("style", []), ("validity", "pass"),
        ):
            review = passing_review()
            review[field] = value
            cases.append(review)
        for verdict in ("PASS", "partial", "", 1, [], None):
            review = passing_review()
            review["fidelity"]["verdict"] = verdict
            cases.append(review)
        for review in cases:
            with self.subTest(review=review), self.assertRaises(InvalidReview):
                score_review(review)

    def test_style_requires_exactly_all_four_families(self):
        for name in ("S1", "S2", "S3", "S4"):
            review = passing_review()
            del review["style"][name]
            with self.subTest(missing=name), self.assertRaises(InvalidReview):
                score_review(review)
        review = passing_review()
        review["style"]["S5"] = deepcopy(review["style"]["S1"])
        with self.assertRaises(InvalidReview):
            score_review(review)

    def test_rubric_03_all_passes_echoes_accepted_version(self):
        self.assertEqual(score_review(passing_review("0.3")), {
            "rubric_version": "0.3", "policy_version": "strict-v1",
            "overall": "pass", "reward": 1, "failed_checks": [], "unresolved_checks": [],
        })

    def test_rubric_03_each_new_family_failure_vetoes_other_passes(self):
        for name in ("S5", "S6", "S7"):
            with self.subTest(name=name):
                review = passing_review("0.3")
                review["style"][name] = {
                    "verdict": "fail", "reason": "A reviewer confirmed a defect.",
                    "evidence": [{"quote": "回复", "reason": "The reviewed defect occurs here."}],
                }
                result = score_review(review)
                self.assertEqual((result["overall"], result["reward"]), ("fail", 0))
                self.assertEqual(result["failed_checks"], [f"style.{name}"])

    def test_rubric_03_each_new_unresolved_family_prevents_pass(self):
        for name in ("S5", "S6", "S7"):
            with self.subTest(name=name):
                review = passing_review("0.3")
                review["style"][name]["verdict"] = "unresolved"
                result = score_review(review)
                self.assertEqual(result["overall"], "unresolved")
                self.assertIsNone(result["reward"])
                self.assertEqual(result["unresolved_checks"], [f"style.{name}"])

    def test_rubric_03_failure_precedes_unresolved_new_family(self):
        for name in ("validity", "fidelity", "task_fitness"):
            with self.subTest(name=name):
                review = passing_review("0.3")
                review[name]["verdict"] = "fail"
                review["style"]["S7"]["verdict"] = "unresolved"
                result = score_review(review)
                self.assertEqual((result["overall"], result["reward"]), ("fail", 0))
                self.assertEqual(result["failed_checks"], [name])
                self.assertEqual(result["unresolved_checks"], ["style.S7"])

    def test_rubric_03_requires_exactly_all_seven_families(self):
        for name in ("S1", "S2", "S3", "S4", "S5", "S6", "S7"):
            review = passing_review("0.3")
            del review["style"][name]
            with self.subTest(missing=name), self.assertRaises(InvalidReview):
                score_review(review)
        review = passing_review("0.3")
        review["style"]["S8"] = deepcopy(review["style"]["S1"])
        with self.assertRaises(InvalidReview):
            score_review(review)

    def test_rubric_02_rejects_each_new_family(self):
        for name in ("S5", "S6", "S7"):
            review = passing_review()
            review["style"][name] = deepcopy(review["style"]["S1"])
            with self.subTest(name=name), self.assertRaises(InvalidReview):
                score_review(review)

    def test_unsupported_or_malformed_rubric_versions_are_invalid(self):
        for version in ("0.4", "", 0.3, [], {}):
            review = passing_review("0.3")
            review["rubric_version"] = version
            with self.subTest(version=version), self.assertRaisesRegex(InvalidReview, "rubric_version"):
                score_review(review)
        result = self.run_cli(json.dumps(passing_review("0.4")), "-")
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertIn("error", json.loads(result.stdout))
        self.assertNotIn("reward", json.loads(result.stdout))

    def test_judgments_require_nonempty_reasons(self):
        for name in ("S1", "S2", "S3", "S4", "validity", "fidelity", "task_fitness"):
            for reason in (None, "", " \n ", 1):
                review = passing_review()
                judgment = review["style"][name] if name.startswith("S") else review[name]
                judgment["reason"] = reason
                with self.subTest(name=name, reason=reason), self.assertRaises(InvalidReview):
                    score_review(review)

    def test_evidence_must_be_complete_and_quote_exact_answer_text(self):
        cases = [
            None, {}, "回复", [None], [{}],
            [{"quote": "回复", "reason": ""}],
            [{"quote": "", "reason": "Reason."}],
            [{"quote": " ", "reason": "Reason."}],
            [{"quote": 3, "reason": "Reason."}],
            [{"quote": "客服自己写", "reason": "Paraphrases are not verbatim evidence."}],
            [{"quote": "回复 由客服撰写", "reason": "Whitespace must match too."}],
        ]
        for evidence in cases:
            with self.subTest(evidence=evidence):
                review = passing_review()
                review["style"]["S3"]["evidence"] = evidence
                with self.assertRaises(InvalidReview):
                    score_review(review)
        review = passing_review()
        del review["style"]["S3"]["evidence"]
        with self.assertRaises(InvalidReview):
            score_review(review)

    def test_style_failure_requires_evidence(self):
        review = passing_review()
        review["style"]["S3"]["verdict"] = "fail"
        with self.assertRaisesRegex(InvalidReview, "style failure requires evidence"):
            score_review(review)

    def test_invalid_judgment_is_rejected_even_after_confirmed_failure(self):
        review = passing_review()
        review["validity"]["verdict"] = "fail"
        del review["task_fitness"]
        with self.assertRaises(InvalidReview):
            score_review(review)

    def run_cli(self, raw: str, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "score_review.py"), *args],
            input=raw, capture_output=True, text=True, check=False,
        )

    def test_cli_stdin_exit_statuses(self):
        for verdict, status in (("pass", 0), ("fail", 1), ("unresolved", 2)):
            with self.subTest(verdict=verdict):
                review = passing_review()
                review["fidelity"]["verdict"] = verdict
                result = self.run_cli(json.dumps(review), "-")
                self.assertEqual(result.returncode, status, result.stderr)
                self.assertEqual(json.loads(result.stdout)["overall"], verdict)
                self.assertEqual(result.stderr, "")

    def test_cli_file_input(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "review.json"
            path.write_text(json.dumps(passing_review(), ensure_ascii=False), encoding="utf-8")
            result = self.run_cli("", str(path))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["reward"], 1)

    def test_cli_rejects_invalid_json_schema_duplicate_keys_and_constants(self):
        valid = json.dumps(passing_review())
        for raw in ("{", "[]", "{}", valid.replace('"rubric_version": "0.2"',
                    '"rubric_version": "0.1", "rubric_version": "0.2"'),
                    valid.replace('"answer":', '"metadata": NaN, "answer":')):
            with self.subTest(raw=raw):
                result = self.run_cli(raw, "-")
                self.assertEqual(result.returncode, 3, result.stderr)
                self.assertIn("error", json.loads(result.stdout))
                self.assertNotIn("reward", json.loads(result.stdout))

    def test_cli_missing_file_bad_encoding_and_usage_are_invalid(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "review.json"
            for args in ((), (str(path),), ("-", "extra")):
                with self.subTest(args=args):
                    result = self.run_cli("", *args)
                    self.assertEqual(result.returncode, 3)
                    self.assertIn("error", json.loads(result.stdout))
            path.write_bytes(b"\xff")
            result = self.run_cli("", str(path))
            self.assertEqual(result.returncode, 3)
            self.assertIn("error", json.loads(result.stdout))


if __name__ == "__main__":
    unittest.main()
