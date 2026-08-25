import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_agent_completion import validate  # noqa: E402


FIXTURES = ROOT / "tests/fixtures/completion"


class AgentCompletionTests(unittest.TestCase):
    def read(self, name):
        return (FIXTURES / name).read_text(encoding="utf-8")

    def report(self, name="passed-agent-verify.json"):
        return json.loads(self.read(name))

    def test_valid_completion_passes(self):
        result = validate(self.read("valid-pr.md"), self.read("valid-issue.md"), self.report(), 900)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["violations"], [])

    def test_unchecked_issue_fails(self):
        result = validate(self.read("valid-pr.md"), self.read("unchecked-issue.md"), self.report(), 900)
        self.assertFalse(result["valid"])
        self.assertIn("unchecked-completion", {row["code"] for row in result["violations"]})

    def test_failed_report_fails(self):
        result = validate(self.read("valid-pr.md"), self.read("valid-issue.md"), self.report("failed-agent-verify.json"), 900)
        self.assertFalse(result["valid"])
        self.assertIn("verify-status", {row["code"] for row in result["violations"]})

    def test_unmerged_pr_metadata_fails(self):
        metadata = json.loads(self.read("unmerged-pr.json"))
        result = validate(self.read("valid-pr.md"), self.read("valid-issue.md"), self.report(), 900, metadata)
        self.assertFalse(result["valid"])
        self.assertIn("pr-not-merged", {row["code"] for row in result["violations"]})

    def test_merged_pr_must_match_verifier_source(self):
        metadata = json.loads(self.read("merged-pr.json"))
        result = validate(self.read("valid-pr.md"), self.read("valid-issue.md"), self.report(), 900, metadata)
        self.assertTrue(result["valid"], result)
        mismatched = dict(self.report())
        mismatched["source_commit"] = "1234567890abc"
        result = validate(self.read("valid-pr.md"), self.read("valid-issue.md"), mismatched, 900, metadata)
        self.assertFalse(result["valid"])
        self.assertIn("verify-source-mismatch", {row["code"] for row in result["violations"]})

    def test_bootstrap_manual_completion_can_skip_pr(self):
        result = validate("", self.read("manual-bootstrap-issue.md"), self.report(), 82, {})
        self.assertTrue(result["valid"], result)

    def test_multiple_closing_issues_fail(self):
        result = validate(self.read("multiple-closing-pr.md"), self.read("valid-issue.md"), self.report(), 900)
        self.assertFalse(result["valid"])
        self.assertIn("closing-issue-count", {row["code"] for row in result["violations"]})

    def test_missing_evidence_is_identified(self):
        issue = self.read("valid-issue.md").replace(
            "- Actions: https://github.com/example/repo/actions/runs/900", ""
        )
        result = validate(self.read("valid-pr.md"), issue, self.report(), 900)
        self.assertFalse(result["valid"])
        self.assertIn("actions-run-url", {row["code"] for row in result["violations"]})

    def test_cli_json_and_exit_codes(self):
        command = [sys.executable, str(ROOT / "tools/validate_agent_completion.py"),
                   "--pr-body", str(FIXTURES / "valid-pr.md"),
                   "--issue-body", str(FIXTURES / "valid-issue.md"),
                   "--verify-report", str(FIXTURES / "passed-agent-verify.json"),
                   "--expected-issue", "900",
                   "--json"]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["valid"])

        command[command.index(str(FIXTURES / "valid-issue.md"))] = str(FIXTURES / "unchecked-issue.md")
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertFalse(json.loads(result.stdout)["valid"])


if __name__ == "__main__":
    unittest.main()
