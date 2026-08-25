import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_agent_issue import validate_body  # noqa: E402


FIXTURES = ROOT / "tests" / "fixtures" / "issues"
VALIDATOR = ROOT / "tools" / "validate_agent_issue.py"


class AgentIssueContractTests(unittest.TestCase):
    def read(self, name):
        return (FIXTURES / name).read_text(encoding="utf-8")

    def test_valid_fixture_passes(self):
        result = validate_body(self.read("valid.md"))
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["violations"], [])

    def test_contract_and_placeholder_words_in_code_spans_are_explanatory(self):
        body = self.read("valid.md").replace(
            "検証エージェントが契約適合のissue本文を判定できるようにする。",
            "検証エージェントが `Contract: agent-task/v1` と `TODO` を説明できるようにする。",
        )
        result = validate_body(body)
        self.assertTrue(result["valid"], result)

    def test_invalid_fixtures_have_stable_violation_codes(self):
        expected = {
            "missing-section.md": "missing-section",
            "placeholders.md": "placeholder",
            "no-checkbox.md": "completion-checkbox",
            "bad-dependencies.md": "dependency-format",
        }
        for filename, code in expected.items():
            with self.subTest(filename=filename):
                result = validate_body(self.read(filename))
                self.assertFalse(result["valid"])
                self.assertIn(code, {row["code"] for row in result["violations"]})

    def test_issue_mode_requires_agent_task_label_and_open_state(self):
        result = validate_body(self.read("valid.md"), labels=[], state="OPEN")
        self.assertIn("missing-agent-task-label", {row["code"] for row in result["violations"]})
        result = validate_body(self.read("valid.md"), labels=["agent-task"], state="CLOSED")
        self.assertIn("issue-not-open", {row["code"] for row in result["violations"]})

    def test_cli_exit_codes_and_json_contract(self):
        passed = subprocess.run(
            [sys.executable, str(VALIDATOR), "--body-file", str(FIXTURES / "valid.md"), "--json"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(passed.returncode, 0, passed.stderr)
        payload = json.loads(passed.stdout)
        self.assertEqual(payload["schema_version"], "agent-task-validation/v1")
        self.assertTrue(payload["valid"])

        failed = subprocess.run(
            [sys.executable, str(VALIDATOR), "--body-file", str(FIXTURES / "no-checkbox.md"), "--json"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(failed.returncode, 2, failed.stderr)
        self.assertFalse(json.loads(failed.stdout)["valid"])

    def test_cli_rejects_ambiguous_input(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "--json"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 3)


if __name__ == "__main__":
    unittest.main()
