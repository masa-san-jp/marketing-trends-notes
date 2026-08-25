import sys
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_graph import acceptance_checks, channel_scope_errors  # noqa: E402


class AcceptanceAndScopeTests(unittest.TestCase):
    def test_acceptance_checks_are_machine_readable_and_boundary_safe(self):
        thresholds = {
            "trend_total": 60,
            "vendor_only_max_ratio": 0.20,
            "independent_min_ratio": 0.50,
            "primary_read_min_ratio": 0.30,
            "per_category_min": 2,
            "stale_max_ratio": 0.15,
            "practice_linked_ratio": 0.50,
            "resolved_prediction_min": 5,
        }
        result = acceptance_checks(60, 12, 42, 30, {"a": 2, "b": 3}, 9, 10, 5, 5, thresholds)
        self.assertTrue(result["passed"])
        self.assertTrue(all(isinstance(row["actual"], (int, float))
                            for row in result["checks"].values()))
        self.assertEqual(set(result["checks"]), {
            "trend_total", "vendor_only_ratio", "independent_ratio", "primary_read_ratio",
            "per_category_min", "stale_ratio", "practice_linked_ratio", "resolved_predictions",
        })

        failed = acceptance_checks(59, 13, 43, 29, {"a": 1, "b": 3}, 10, 10, 4, 4, thresholds)
        self.assertFalse(failed["passed"])
        self.assertFalse(failed["checks"]["trend_total"]["passed"])

    def test_channel_scope_contract(self):
        self.assertEqual(channel_scope_errors({
            "status": "draft",
            "channel_scope": {"status": "mapped", "note": None},
            "channels": [{"role": "originated_on", "target": "channel/tiktok"}],
        }), [])
        self.assertEqual(channel_scope_errors({
            "status": "verified",
            "channel_scope": {"status": "not-applicable", "note": "制度起点"},
            "channels": [],
        }), [])
        self.assertTrue(channel_scope_errors({
            "status": "verified",
            "channel_scope": {"status": "unresolved", "note": "未確認"},
            "channels": [],
        }))
        self.assertTrue(channel_scope_errors({
            "status": "draft",
            "channel_scope": {"status": "mapped", "note": "補足"},
            "channels": [{"role": "observed_on", "target": "channel/tiktok"}],
        }))

    def test_current_migration_is_complete(self):
        trends = sorted((ROOT / "entities" / "trends").glob("*.md"))
        self.assertEqual(len(trends), 60)
        mapped = []
        not_applicable = []
        for path in trends:
            text = path.read_text(encoding="utf-8")
            meta = yaml.safe_load(text.split("---\n", 2)[1])
            status = meta["channel_scope"]["status"]
            self.assertIn(status, {"mapped", "not-applicable", "unresolved"})
            self.assertNotIn("## 自分の事業にどう使うか", text)
            if status == "mapped":
                mapped.append(meta["id"])
                self.assertTrue(meta["channels"])
            elif status == "not-applicable":
                not_applicable.append(meta["id"])
                self.assertEqual(meta["channels"], [])
                self.assertTrue(meta["channel_scope"]["note"].strip())
        self.assertEqual(mapped, ["trend/short-video-mainstream"])
        self.assertEqual(len(not_applicable), 59)

        for path in (ROOT / "entities" / "practices").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("## 自分の事業にどう使うか", text)
            self.assertNotIn("## 効いた条件・効かない条件", text)
            self.assertNotIn("**未実施", text)
            self.assertIn("## 成立条件・失敗条件", text)
            self.assertIn("## 利用上の注意", text)
            self.assertIn("## 未着手", text)

    def test_audit_fail_on_findings_is_read_only(self):
        result = subprocess.run(
            [sys.executable, "tools/audit.py", "--dry-run", "--now", "2026-08-25", "--fail-on-findings"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
