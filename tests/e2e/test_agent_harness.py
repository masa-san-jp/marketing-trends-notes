import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from agent_task import GitHubAdapter  # noqa: E402
from certify_agent_harness import ADAPTER_METHODS, FixtureGitHubAdapter  # noqa: E402


@unittest.skipIf(os.environ.get("AGENT_VERIFY_REGRESSION") == "1", "avoid verifier recursion")
class AgentHarnessE2ETests(unittest.TestCase):
    def test_certification_cli_runs_the_closed_loop_without_network(self):
        command = [
            sys.executable, str(ROOT / "tools" / "certify_agent_harness.py"),
            "--now", "2026-08-25", "--actor", "fixture-agent", "--json",
        ]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(result.stderr, "")
        payload = json.loads(result.stdout)
        self.assertEqual(payload["schema_version"], "agent-harness-certification/v1")
        self.assertEqual(payload["status"], "passed")
        self.assertGreaterEqual(len(payload["scenarios"]), 10)
        self.assertTrue(all(row["status"] == "passed" for row in payload["scenarios"]), payload)

    def test_fake_and_github_adapters_expose_the_same_contract(self):
        for adapter_type in (FixtureGitHubAdapter, GitHubAdapter):
            for method in ADAPTER_METHODS:
                self.assertTrue(callable(getattr(adapter_type, method, None)),
                                f"{adapter_type.__name__}.{method}")


if __name__ == "__main__":
    unittest.main()
