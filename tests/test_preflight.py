import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import preflight  # noqa: E402


class PreflightTests(unittest.TestCase):
    def test_report_is_machine_readable_and_optional_gaps_do_not_fail(self):
        result = preflight.report(preflight.collect_checks(command_lookup=lambda name: "/bin/" + name))
        encoded = json.dumps(result)
        decoded = json.loads(encoded)
        self.assertEqual(decoded["schema_version"], "agent-preflight/v1")
        self.assertIn(decoded["status"], {"passed", "failed"})
        self.assertTrue(all({"name", "status", "required", "detail"} <= set(row)
                            for row in decoded["checks"]))

    def test_missing_required_command_fails(self):
        checks = preflight.collect_checks(command_lookup=lambda name: None)
        result = preflight.report(checks)
        self.assertEqual(result["status"], "failed")
        self.assertIn("git-command", result["failed_required"])

    def test_missing_optional_gh_does_not_fail_unless_required(self):
        with patch.object(preflight.shutil, "which", return_value=None):
            checks = preflight.collect_checks(command_lookup=lambda name: "/bin/" if name == "git" else None)
        result = preflight.report(checks)
        self.assertNotIn("github-cli", result["failed_required"])

        with patch.object(preflight.shutil, "which", return_value=None):
            checks = preflight.collect_checks(require_gh=True,
                                              command_lookup=lambda name: "/bin/" if name == "git" else None)
        result = preflight.report(checks)
        self.assertIn("github-cli", result["failed_required"])

    def test_hooks_path_mismatch_is_required_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".python-version").write_text(preflight.expected_python(ROOT) + "\n", encoding="utf-8")
            (root / "requirements.txt").write_text("", encoding="utf-8")
            with patch.object(preflight, "read_git", return_value=(0, "wrong-hooks", "")):
                checks = preflight.collect_checks(root, command_lookup=lambda name: "/bin/" + name)
        result = preflight.report(checks)
        self.assertIn("hooks-path", result["failed_required"])


if __name__ == "__main__":
    unittest.main()
