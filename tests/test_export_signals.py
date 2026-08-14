import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "tools" / "export_signals.py"
PYTHON = ROOT / ".venv" / "bin" / "python"
PYTHON = str(PYTHON) if PYTHON.exists() else sys.executable


class ExportSignalsTests(unittest.TestCase):
    def run_export(self, *args: str) -> dict:
        result = subprocess.run(
            [PYTHON, str(EXPORTER), "--purpose", "artistic-research", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(result.stdout)

    def test_envelope_uses_research_signal_export_contract(self) -> None:
        payload = self.run_export("--limit", "1")

        self.assertEqual(payload["contract_version"], "research-signal-export/v1")
        self.assertEqual(payload["source_repository"], "marketing-trends")
        self.assertEqual(payload["purpose"], "artistic-research")
        self.assertEqual(payload["signal_count"], len(payload["signals"]))
        self.assertNotIn("records", payload)
        self.assertNotIn("record_count", payload)
        self.assertTrue(payload["source_commit"].isalnum())
        self.assertRegex(payload["generated_at"], r"^\d{4}-\d{2}-\d{2}T")

    def test_all_trends_are_exported(self) -> None:
        payload = self.run_export()

        self.assertEqual(payload["signal_count"], 60)
        self.assertEqual(payload["signal_count"], len(payload["signals"]))
        self.assertEqual(payload["stale_count"], 0)
        self.assertTrue(all(signal["entity_id"].startswith("trend/") for signal in payload["signals"]))


if __name__ == "__main__":
    unittest.main()
