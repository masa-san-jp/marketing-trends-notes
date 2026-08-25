import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import agent_verify  # noqa: E402


@unittest.skipIf(os.environ.get("AGENT_VERIFY_REGRESSION") == "1", "agent_verify child regression run")
class AgentVerifyTests(unittest.TestCase):
    def run_verify(self, *extra):
        environment = os.environ.copy()
        environment["AGENT_VERIFY_REGRESSION"] = "1"
        return subprocess.run(
            [sys.executable, str(ROOT / "tools/agent_verify.py"), "--issue-body",
             str(ROOT / "tests/fixtures/issues/valid.md"), "--now", "2026-08-25", "--json", *extra],
            cwd=ROOT, env=environment, capture_output=True, text=True,
        )

    def test_current_repository_passes_and_stdout_is_json_only(self):
        result = self.run_verify()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["schema_version"], "agent-verify/v1")
        self.assertEqual(payload["status"], "passed")
        self.assertEqual([row["name"] for row in payload["checks"]], list(agent_verify.CHECK_NAMES))
        self.assertTrue(all({"name", "required", "status", "exit_code", "summary"} <= set(row)
                            for row in payload["checks"]))

    def test_invalid_issue_body_returns_two(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/agent_verify.py"), "--issue-body",
             str(ROOT / "tests/fixtures/issues/no-checkbox.md"), "--now", "2026-08-25", "--json"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "failed")
        self.assertEqual(payload["checks"][0]["name"], "issue-contract")
        self.assertEqual(payload["checks"][0]["exit_code"], 2)

    def test_missing_or_invalid_now_returns_three(self):
        for now in (None, "2026/08/25"):
            command = [sys.executable, str(ROOT / "tools/agent_verify.py"), "--issue-body",
                       str(ROOT / "tests/fixtures/issues/valid.md"), "--json"]
            if now:
                command.extend(["--now", now])
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 3)
            self.assertEqual(json.loads(result.stdout)["status"], "failed")

    def test_output_file_is_allowed_and_worktree_contents_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            before = agent_verify.snapshot_worktree(ROOT, output)
            result = self.run_verify("--output", str(output))
            after = agent_verify.snapshot_worktree(ROOT, output)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertEqual(before, after)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["status"], "passed")


class AgentVerifyCheckTests(unittest.TestCase):
    def test_export_contract_failure_is_exit_two(self):
        raw = (ROOT / "tests/fixtures/verify/invalid-export.json").read_text(encoding="utf-8")
        code, summary = agent_verify.validate_export_payload(raw)
        self.assertEqual(code, 2)
        self.assertIn("missing", summary)

    def test_strict_audit_failure_is_exit_two(self):
        row, _ = agent_verify.run_command(
            "strict-live-audit-fixture",
            [sys.executable, "tools/audit.py", "--dry-run", "--now", "2099-01-01", "--fail-on-findings"],
        )
        self.assertEqual(row["status"], "failed")
        self.assertEqual(row["exit_code"], 2)

    def test_generated_artifact_staleness_is_exit_two_without_touching_source(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory) / "repo"
            shutil.copytree(ROOT, temporary, ignore=agent_verify.copy_ignore)
            graph = temporary / "data/graph.json"
            graph.write_text(graph.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            code, summary = agent_verify.generated_artifacts_check(temporary)
            self.assertEqual(code, 2)
            self.assertIn("data/graph.json", summary)


if __name__ == "__main__":
    unittest.main()
