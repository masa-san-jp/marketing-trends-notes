import json
import subprocess
import sys
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from export_signals import EVIDENCE_KIND, build_record  # noqa: E402


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
        self.assertNotIn("unknown", {signal["evidence_kind"] for signal in payload["signals"]})

    def test_all_kb_certainty_values_have_an_explicit_boundary_mapping(self) -> None:
        self.assertEqual(EVIDENCE_KIND["attested"], "primary")
        self.assertEqual(EVIDENCE_KIND["measured"], "primary")
        self.assertEqual(EVIDENCE_KIND["hypothesis"], "unknown")

        record = build_record({
            "id": "trend/example",
            "path": "entities/trends/example.md",
            "label_ja": "例",
            "label_en": "Example",
            "stage": "growing",
            "sources": ["https://example.com"],
            "freshness": {"valid_as_of": "2026-08-01", "recheck_by": "2026-11-01"},
            "evidence": [{"certainty": "attested", "retrieved": "primary"}],
            "predictions": [],
        }, "a" * 40, datetime(2026, 8, 25), "test")
        self.assertEqual(record["evidence_kind"], "primary")


if __name__ == "__main__":
    unittest.main()
