import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import card_excerpts as ce  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

TREND = """---
id: trend/sample
label_ja: 見本
---

# 見本

## 見出している未来（何に向かっているか）

> 生活者は、今後の生活の見通しを悲観しつつ、
資産・貯蓄に力を入れたいと考える割合が増えている。
詳しくは [調査の結果](https://example.com/a) と P571 を参照。

これは意向調査であり、`independent` な **第三者** の数字である。

## 足元の根拠（完了した事実）

| 調査 | 割合 |
|---|---|
| 令和3年 | 77.6％ |

Retail media
spend keeps growing in Japan.

**未確認**: 令和3年より前の推移は未確認である。

## 反証

ここは対象外の節である。
"""


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()


def make_repo(tmp: str, text: str = TREND) -> Path:
    root = Path(tmp)
    (root / "entities" / "trends").mkdir(parents=True)
    (root / "data").mkdir()
    (root / "entities" / "trends" / "sample.md").write_text(text, encoding="utf-8")
    git(root, "init", "-q")
    git(root, "-c", "user.email=t@example.com", "-c", "user.name=t", "add", ".")
    git(root, "-c", "user.email=t@example.com", "-c", "user.name=t", "commit", "-qm", "init")
    return root


class ScriptedAnswerer:
    """element_id ごとに attempt 順の値を返す。受け取った依頼を記録する。"""

    def __init__(self, values: dict[str, list[str]]):
        self.values = values
        self.requests: list[dict] = []

    def __call__(self, request: dict) -> dict:
        self.requests.append(request)
        values = self.values[request["element_id"]]
        value = values[min(request["attempt"] - 1, len(values) - 1)]
        return {"contract_version": "element-answer/v1", "value": value,
                **{k: request[k] for k in ("run_id", "element_id", "attempt")}}


class NormalizeTests(unittest.TestCase):
    def sections(self) -> dict:
        return ce.extract_sections(TREND)

    def test_only_target_sections_are_taken(self) -> None:
        self.assertEqual(list(self.sections()), ["見出している未来", "足元の根拠"])

    def test_japanese_lines_are_joined_and_latin_lines_get_one_space(self) -> None:
        sections = self.sections()
        self.assertIn("悲観しつつ、資産・貯蓄に力を入れたい", sections["見出している未来"][0])
        self.assertIn("Retail media spend keeps growing in Japan.", sections["足元の根拠"])

    def test_quote_links_urls_ids_markup_and_tables_are_removed(self) -> None:
        text = ce.sections_text(self.sections())
        for noise in (">", "https://", "P571", "**", "`", "|", "](", "令和3年 "):
            self.assertNotIn(noise, text)
        self.assertIn("詳しくは 調査の結果 と を参照", text)
        self.assertIn("independent な 第三者 の数字", text)

    def test_body_hash_ignores_other_sections_and_changes_with_target_text(self) -> None:
        base = ce.body_sha256(TREND)
        self.assertEqual(base, ce.body_sha256(TREND.replace("ここは対象外の節である。", "別の文")))
        self.assertNotEqual(base, ce.body_sha256(TREND.replace("増えている", "減っている")))

    def test_request_body_is_cut_on_paragraph_and_sentence_boundaries(self) -> None:
        sections = {"見出している未来": ["あ" * 50 + "。", "い" * 50 + "。" + "う" * 50 + "。"], "足元の根拠": ["え。"]}
        body = ce.request_body(sections, max_bytes=340)
        self.assertLessEqual(len(body.encode("utf-8")), 340)
        self.assertTrue(body.startswith("【見出している未来】\n"))
        self.assertNotIn("え。", body)
        for line in body.splitlines()[1:]:
            self.assertTrue(line.endswith("。"))


class ContractAndCheckTests(unittest.TestCase):
    def request(self, index: int = 1, **kw) -> dict:
        defaults = dict(run_id="r", slug="sample", index=index, attempt=1,
                        body="【見出している未来】\n" + "あ" * 20 + "。\n" + "い" * 20 + "。",
                        first_quote=("あ" * 20 + "。") if index == 2 else None, previous_failure=None)
        defaults.update(kw)
        return ce.build_request(**defaults)

    def test_requests_conform_to_the_copied_schema(self) -> None:
        for index in (1, 2):
            self.assertEqual(ce.validate_message(self.request(index), "request"), [])

    def test_schema_validator_rejects_broken_messages(self) -> None:
        good = self.request()
        for mutate in (lambda r: r.update(contract_version="x"), lambda r: r.pop("checks"),
                       lambda r: r.update(extra=1), lambda r: r.update(attempt=0),
                       lambda r: r.update(element_id="bad id"),
                       lambda r: r["answer_format"].update(type="nope")):
            broken = json.loads(json.dumps(good))
            mutate(broken)
            self.assertTrue(ce.validate_message(broken, "request"), broken)
        answer = {"contract_version": "element-answer/v1", "run_id": "r", "element_id": "e", "attempt": 1, "value": "v"}
        self.assertEqual(ce.validate_message(answer, "answer"), [])
        self.assertTrue(ce.validate_message({**answer, "value": 3}, "answer"))
        self.assertTrue(ce.validate_message({**answer, "stray": 1}, "answer"))

    def failures(self, value, index=1) -> list[str]:
        return [f["check"] for f in ce.check_value(value, self.request(index))]

    def test_first_element_checks(self) -> None:
        self.assertEqual(self.failures("あ" * 20 + "。"), [])
        self.assertIn("exact_input_excerpt:body", self.failures("う" * 20))
        self.assertIn("min_chars", self.failures("あ" * 5))
        self.assertIn("max_chars", self.failures("あ" * 121))
        self.assertIn("non_empty", self.failures("  "))
        self.assertIn("single_line", self.failures("あ" * 20 + "。\n" + "い" * 20))

    def test_reference_and_unconfirmed_tokens_are_rejected(self) -> None:
        body = "【見出している未来】\n未確認: 令和3年より前の推移。 https://example.com/x と P571 と **強調** を含む文である。"
        request = self.request(body=body)
        for value in ("未確認: 令和3年より前の推移。", "https://example.com/x と P571 と", "P571 と **強調** を含む文"):
            names = [f["check"] for f in ce.check_value(value, request)]
            self.assertTrue({"no_reference_tokens", "forbidden:未確認"} & set(names), value)

    def test_second_element_accepts_none_but_not_overlap(self) -> None:
        self.assertEqual(self.failures(ce.NO_MORE, 2), [])
        self.assertEqual(self.failures("い" * 20 + "。", 2), [])
        self.assertIn("distinct_from_input:first_quote", self.failures("あ" * 20 + "。", 2))
        self.assertIn("exact_input_excerpt_or_none:body", self.failures("う" * 20, 2))
        self.assertIn("exact_input_excerpt_or_none:body", self.failures("い" * 5, 2))

    def test_failure_reasons_fit_the_contract(self) -> None:
        failures = ce.check_value("う" * 130 + "\nhttps://x", self.request())
        self.assertTrue(failures)
        request = self.request(previous_failure=failures)
        self.assertEqual(ce.validate_message(request, "request"), [])


class GenerateTests(unittest.TestCase):
    first = "生活者は、今後の生活の見通しを悲観しつつ、資産・貯蓄に力を入れたいと考える割合が増えている。"
    second = "Retail media spend keeps growing in Japan."

    def run_generate(self, root: Path, answerer, **kw) -> dict:
        return ce.generate(answerer, root=root, state_path=root / "data" / "card-excerpts.json",
                           log=lambda *_: None, **kw)

    def test_retry_resume_and_rerun_only_changed_body(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(tmp)
            state_path = root / "data" / "card-excerpts.json"
            answerer = ScriptedAnswerer({
                "K1.card.trend.sample.1": ["本文にない文章を勝手に作って書いた偽の抜き書きです", self.first],
                "K1.card.trend.sample.2": [ce.NO_MORE]})
            report = self.run_generate(root, answerer)
            self.assertEqual(report["blocked"], {})
            # 落ちた要素だけが previous_failure 付きで再依頼され、もう一方は聞き直されない
            ids = [(r["element_id"], r["attempt"]) for r in answerer.requests]
            self.assertEqual(ids, [("K1.card.trend.sample.1", 1), ("K1.card.trend.sample.1", 2),
                                   ("K1.card.trend.sample.2", 1)])
            self.assertIsNone(answerer.requests[0]["previous_failure"])
            self.assertEqual(answerer.requests[1]["previous_failure"][0]["check"], "exact_input_excerpt:body")
            self.assertEqual(answerer.requests[2]["inputs"]["first_quote"], self.first)
            entry = ce.load_state(state_path)["entries"]["trend/sample"]
            self.assertEqual(entry["elements"]["1"]["accepted"], self.first)
            self.assertEqual(len(entry["elements"]["1"]["attempts"]), 2)
            self.assertEqual(entry["elements"]["1"]["accepted_sha256"], ce.sha256_text(self.first))
            self.assertEqual(entry["source_commit"], git(root, "rev-parse", "HEAD"))
            self.assertEqual(ce.verify(root=root, state=ce.load_state(state_path)), [])

            # 本文が同じなら何も聞かない
            silent = ScriptedAnswerer({})
            self.run_generate(root, silent)
            self.assertEqual(silent.requests, [])

            # 対象外の節だけの変更では、やり直さない
            path = root / "entities" / "trends" / "sample.md"
            path.write_text(TREND.replace("ここは対象外の節である。", "別の文である。"), encoding="utf-8")
            git(root, "-c", "user.email=t@example.com", "-c", "user.name=t", "commit", "-qam", "other")
            self.run_generate(root, silent)
            self.assertEqual(silent.requests, [])

            # 対象の節が変わると、その trend だけやり直し、履歴に前の受理値を残す
            changed = TREND.replace("増えている", "高まっている")
            path.write_text(changed, encoding="utf-8")
            git(root, "-c", "user.email=t@example.com", "-c", "user.name=t", "commit", "-qam", "body")
            again = ScriptedAnswerer({
                "K1.card.trend.sample.1": ["生活者は、今後の生活の見通しを悲観しつつ、資産・貯蓄に力を入れたいと考える割合が高まっている。"],
                "K1.card.trend.sample.2": [self.second]})
            self.run_generate(root, again)
            self.assertEqual(len(again.requests), 2)
            entry = ce.load_state(state_path)["entries"]["trend/sample"]
            self.assertEqual(entry["superseded"][0]["elements"]["1"]["accepted"], self.first)
            self.assertEqual(ce.entry_quotes(entry)[1], self.second)
            self.assertEqual(ce.verify(root=root, state=ce.load_state(state_path)), [])

    def test_blocked_after_five_failures_and_state_resumes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(tmp)
            bad = ScriptedAnswerer({"K1.card.trend.sample.1": ["本文にない文章を勝手に作って書いた偽の抜き書きです"]})
            report = self.run_generate(root, bad)
            self.assertIn("trend/sample", report["blocked"])
            self.assertEqual(len(bad.requests), ce.MAX_ATTEMPTS)
            self.assertEqual(bad.requests[-1]["attempt"], ce.MAX_ATTEMPTS)
            self.assertEqual(ce.entry_quotes(ce.load_state(root / "data" / "card-excerpts.json")["entries"]["trend/sample"]), None)
            self.assertTrue(ce.verify(root=root, state=ce.load_state(root / "data" / "card-excerpts.json")))

    def test_dirty_entities_are_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(tmp)
            (root / "entities" / "trends" / "sample.md").write_text(TREND + "\n追記\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                self.run_generate(root, ScriptedAnswerer({}))

    def test_export_card_matches_pinned_blob_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = make_repo(tmp)
            answerer = ScriptedAnswerer({"K1.card.trend.sample.1": [self.first], "K1.card.trend.sample.2": [self.second]})
            self.run_generate(root, answerer)
            state = ce.load_state(root / "data" / "card-excerpts.json")
            commit = git(root, "rev-parse", "HEAD")
            card = ce.export_card("trend/sample", "entities/trends/sample.md", commit, state, root)
            self.assertEqual([c["text"] for c in card], [self.first, self.second])
            self.assertEqual({c["source_locator"] for c in card},
                             {"entities/trends/sample.md#見出している未来", "entities/trends/sample.md#足元の根拠"})
            self.assertEqual({c["source_sha256"] for c in card},
                             {ce.hashlib.sha256((root / "entities/trends/sample.md").read_bytes()).hexdigest()})
            # 本文が変わったら card は出さない（古い抜き書きを運ばない）
            (root / "entities/trends/sample.md").write_text(TREND.replace("増えている", "高まっている"), encoding="utf-8")
            git(root, "-c", "user.email=t@example.com", "-c", "user.name=t", "commit", "-qam", "body")
            self.assertEqual(ce.export_card("trend/sample", "entities/trends/sample.md", git(root, "rev-parse", "HEAD"), state, root), [])


class CommandAnswererTests(unittest.TestCase):
    def test_command_answerer_round_trip_and_rejections(self) -> None:
        request = ce.build_request("r", "sample", 1, 1, "【見出している未来】\n" + "あ" * 20 + "。", None, None)
        script = ("import json,sys\nr=json.load(sys.stdin)\n"
                  "print(json.dumps({'contract_version':'element-answer/v1','run_id':r['run_id'],"
                  "'element_id':r['element_id'],'attempt':r['attempt'],'value':'x'}))")
        answer = ce.command_answerer([sys.executable, "-c", script])(request)
        self.assertEqual(answer["value"], "x")
        wrong = script.replace("r['attempt']", "r['attempt']+1")
        with self.assertRaises(ce.AnswererError):
            ce.command_answerer([sys.executable, "-c", wrong])(request)
        with self.assertRaises(ce.AnswererError):
            ce.command_answerer([sys.executable, "-c", "print('not json')"])(request)
        with self.assertRaises(ce.AnswererError):
            ce.command_answerer([sys.executable, "-c", "import sys;sys.exit(3)"])(request)

    def test_haiku_adapter_wraps_only_the_value(self) -> None:
        import haiku_answerer
        request = ce.build_request("r", "sample", 1, 2, "【見出している未来】\n" + "あ" * 20 + "。", None,
                                   [{"check": "min_chars", "reason": "x"}])
        prompt = haiku_answerer.build_prompt(request)
        self.assertIn("previous_failure", prompt)
        self.assertNotIn("run_id", prompt)
        self.assertEqual(haiku_answerer.MODEL, "claude-haiku-5-5")
        self.assertEqual(haiku_answerer.EFFORT, "max")


class RealDataTests(unittest.TestCase):
    """完了の確認: 全 trend にカードがあり、すべての抜き書きが固定 commit の本文に一字一句ある。"""

    def test_every_trend_has_verified_cards(self) -> None:
        self.assertEqual(ce.verify(), [])

    def test_export_carries_label_and_card(self) -> None:
        result = subprocess.run([sys.executable, str(ROOT / "tools" / "export_signals.py"), "--purpose", "artistic-research"],
                                cwd=ROOT, check=True, capture_output=True, text=True)
        signals = json.loads(result.stdout)["signals"]
        self.assertEqual(len(signals), 65)
        for signal in signals:
            self.assertTrue(signal["label_ja"])
            self.assertIn(len(signal["card"]), (1, 2), signal["entity_id"])
            for item in signal["card"]:
                self.assertEqual(set(item), {"text", "source_locator", "source_sha256"})
                self.assertTrue(item["source_locator"].startswith(signal["source_locator"] + "#"))


if __name__ == "__main__":
    unittest.main()
