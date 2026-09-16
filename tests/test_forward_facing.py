import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_graph import (FORWARD_HEADING, GROUND_HEADING, REFUTATION_HEADING,  # noqa: E402
                         coverage, validate_evidence, validate_trend)

CFG = {
    "forward_required_from": "2026-10-01",
    "categories": {"cross-category": {"label_ja": "カテゴリ横断"}},
    "geographies": {"japan": {"label_ja": "日本"}},
    "thresholds": {
        "trend_total": 0, "vendor_only_max_ratio": 1.0, "independent_min_ratio": 0.0,
        "primary_read_min_ratio": 0.0, "per_category_min": 0, "stale_max_ratio": 1.0,
        "practice_linked_ratio": 0.0, "resolved_prediction_min": 0,
        "forward_stated_ratio_min": 0.0, "intended_evidence_ratio_min": 0.0,
    },
}

BASE_BODY = (
    f"{FORWARD_HEADING}（何に向かって動いているか）\n\n本文\n\n"
    f"{GROUND_HEADING}（完了した事実）\n\n本文\n\n"
    f"{REFUTATION_HEADING}（これが偽なら何が観測されるか）\n\n本文\n"
)


def base_meta(**overrides):
    meta = {
        "id": "trend/test", "type": "trend", "status": "draft",
        "kind": "demand-shift", "stage": "emerging", "market": "cross-category", "geo": "japan",
        "naming": {"self_identified": True},
        "freshness": {"valid_as_of": "2026-09-16", "recheck_by": "2026-10-16"},
        "channel_scope": {"status": "not-applicable", "note": "特定チャネル発ではない"},
        "channels": [],
        "predictions": [{"claim": "x", "by": "2027-01", "resolved": None, "outcome": None}],
        "evidence": [{"field": "stage", "source": "https://example.com", "certainty": "independent",
                      "retrieved": "primary", "as_of": "2026-09", "tense": "completed"}],
        "updated": "2026-09-16",
    }
    meta.update(overrides)
    return meta


class ForwardFacingTests(unittest.TestCase):
    def test_a_missing_forward_heading_errs(self):
        meta = base_meta(updated="2026-10-05")
        body = BASE_BODY.replace(FORWARD_HEADING, "## 何が変わったか")
        errors = []
        validate_trend(meta, body, CFG, errors.append)
        self.assertTrue(any(FORWARD_HEADING in e for e in errors), errors)

    def test_b_missing_predictions_errs(self):
        meta = base_meta(updated="2026-10-05", predictions=[])
        errors = []
        validate_trend(meta, BASE_BODY, CFG, errors.append)
        self.assertTrue(any("predictions" in e for e in errors), errors)

    def test_c_tense_out_of_vocab_errs_regardless_of_date(self):
        meta = base_meta(updated="2026-09-01", evidence=[
            {"field": "stage", "source": "https://example.com", "certainty": "independent",
             "retrieved": "primary", "as_of": "2026-09", "tense": "someday"},
        ])
        errors = []
        validate_evidence(meta, errors.append)
        self.assertTrue(any("tense" in e for e in errors), errors)

    def test_d_pre_gate_trend_without_forward_fields_is_clean(self):
        meta = base_meta(updated="2026-09-01", predictions=[], evidence=[
            {"field": "stage", "source": "https://example.com", "certainty": "independent",
             "retrieved": "primary", "as_of": "2026-09"},
        ])
        body = ("## 何が変わったか\n\n本文\n\n"
                f"{REFUTATION_HEADING}（これが偽なら何が観測されるか）\n\n本文\n")
        errors = []
        validate_trend(meta, body, CFG, errors.append)
        validate_evidence(meta, errors.append)
        self.assertEqual(errors, [])

    def test_e_coverage_forward_ratios(self):
        entities, records = {}, []

        def add(tid, forward_stated, intended, stage="emerging"):
            meta = base_meta(id=tid, stage=stage)
            if intended:
                meta["evidence"] = [dict(meta["evidence"][0], tense="intended")]
            if forward_stated:
                body = BASE_BODY
            else:
                body = BASE_BODY.replace(FORWARD_HEADING, "## 何が変わったか")
                meta["predictions"] = []
            entities[tid] = meta
            records.append((Path(tid), meta, body))

        add("trend/a", True, False)
        add("trend/b", True, True)
        add("trend/c", False, False)
        add("trend/d", False, False, stage="dead")

        cov = coverage(entities, CFG, records)
        checks = cov["acceptance"]["checks"]
        self.assertAlmostEqual(checks["forward_stated_ratio"]["actual"], 2 / 3)
        self.assertAlmostEqual(checks["intended_evidence_ratio"]["actual"], 1 / 3)


if __name__ == "__main__":
    unittest.main()
