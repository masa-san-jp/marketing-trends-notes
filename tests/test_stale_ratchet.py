import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_graph  # noqa: E402


def trend(recheck_by, stage="current", status="verified"):
    return {"type": "trend", "status": status, "stage": stage,
            "freshness": {"recheck_by": recheck_by}}


class StaleRatchetTests(unittest.TestCase):
    def test_stale_ids_counts_only_live_trends_past_their_deadline(self):
        entities = {
            "old": trend("2026-11-11"),
            "due-today": trend("2026-11-27"),
            "dead": trend("2026-01-01", stage="dead"),
            "stub": trend("2026-01-01", status="stub"),
            "practice": {"type": "practice", "freshness": {"recheck_by": "2026-01-01"}},
        }
        self.assertEqual(build_graph.stale_ids(entities, "2026-11-27"), {"old"})

    def test_baseline_counts_previous_commit_at_the_new_as_of(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "data").mkdir()
            graph = {"entities": {"a": trend("2026-11-22"), "b": trend("2027-02-01")}}
            (repo / "data" / "graph.json").write_text(json.dumps(graph), encoding="utf-8")
            for cmd in (["init", "-q"], ["add", "."],
                        ["-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "-qm", "x"]):
                subprocess.run(["git", *cmd], cwd=repo, check=True)
            original = build_graph.ROOT
            build_graph.ROOT = repo
            try:
                self.assertEqual(build_graph.baseline_stale_count("2026-11-23"), 1)
                self.assertEqual(build_graph.baseline_stale_count("2026-11-01"), 0)
            finally:
                build_graph.ROOT = original

    def test_baseline_is_none_without_a_previous_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = build_graph.ROOT
            build_graph.ROOT = Path(tmp)
            try:
                self.assertIsNone(build_graph.baseline_stale_count("2026-11-23"))
            finally:
                build_graph.ROOT = original


if __name__ == "__main__":
    unittest.main()
