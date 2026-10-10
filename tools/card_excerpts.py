#!/usr/bin/env python3
"""trend の「カード」（一字一句の抜き書き）を、1件1要素の推論で作って保存する。

    python3 tools/card_excerpts.py status
    python3 tools/card_excerpts.py next    --entity trend/anxiety-multiplication
    python3 tools/card_excerpts.py generate [--entity trend/...] [--limit N]
    python3 tools/card_excerpts.py verify

正本: 親 agentic-art-orchestration の docs/20261010-phase-a-v2-design.md（4.1〜4.2・9.3）と
docs/20261007-element-harness-design.md（2〜3章）。

- 対象の本文は「見出している未来」「足元の根拠」の2節。引用記号・リンク記法・URL・ID・強調記号を
  取り除き、日本語の間の改行は詰め、英字の間の改行は空白1つにした文字列（4.1）を本文として扱う。
  抜き書きの確認も、この規則を通した後の文字列に対して行う。
- 1 trend につき要素は2つ。`K1.card.<slug>.1` は最もよく表す部分、`.2` は別の1箇所
  （無ければ「これ以上なし」）。1要素1推論で、落ちたらその要素だけを previous_failure 付きで再依頼する。
- 結果は本文の sha256・要素の履歴とともに `data/card-excerpts.json` に保存する。
  本文（2節）の sha256 が変わった trend だけやり直す。
- 答え手は外部コマンド（stdin に依頼1件、stdout に答え1件）。プログラムは答えを作らない。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from kb import ROOT
except ModuleNotFoundError:  # tools.card_excerpts として読まれた場合
    from tools.kb import ROOT

STATE_PATH = ROOT / "data" / "card-excerpts.json"
SCHEMA_DIR = ROOT / "schemas"
STATE_VERSION = "card-excerpts/v1"
REQUEST_CONTRACT = "element-request/v1"
ANSWER_CONTRACT = "element-answer/v1"

SECTIONS = ("見出している未来", "足元の根拠")
MAX_ATTEMPTS = 5
QUOTE_MIN, QUOTE_MAX = 12, 120
NO_MORE = "これ以上なし"
BODY_MAX_BYTES = 3000
FORBIDDEN_IN_QUOTE = ("未確認",)

INSTRUCTION_FIRST = (
    "この本文から、この動きが何に向かっているかを最もよく表す部分を、一字も変えずに1箇所だけ抜き書きしてください。"
    "「未確認」の注記、出典の説明、URL、IDは含めないでください。"
)
INSTRUCTION_SECOND = (
    "first_quote とは別の箇所で、この動きが何に向かっているかをよく表す部分を、一字も変えずに抜き書きしてください。"
    f"無ければ「{NO_MORE}」とだけ答えてください。「未確認」の注記、出典の説明、URL、IDは含めないでください。"
)


# --- 本文の取り出しと正規化（4.1 の固定規則） -----------------------------------

_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_URL = re.compile(r"https?://\S+")
_ID = re.compile(r"\b[PQ]\d+\b")
_LIST_MARK = re.compile(r"^(?:[-*+]|\d+\.)\s+")
_ASCII_EDGE = re.compile(r"[\x21-\x7e]")


def _clean_line(line: str) -> str:
    line = _LINK.sub(r"\1", line)
    line = _URL.sub("", line)
    line = _ID.sub("", line)
    line = line.replace("**", "").replace("`", "")
    return re.sub(r"[ \t]+", " ", line).strip()


def _join(lines: list[str]) -> str:
    """段落内の改行: 日本語の間は詰め、英字の間は空白1つ。"""
    out = ""
    for line in lines:
        if out and _ASCII_EDGE.fullmatch(out[-1]) and _ASCII_EDGE.fullmatch(line[0]):
            out += " "
        out += line
    return out


def normalize_paragraphs(raw: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []

    def flush() -> None:
        if current:
            joined = _join(current)
            if joined:
                paragraphs.append(joined)
            current.clear()

    for raw_line in raw.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("|"):  # 表の行は文章ではない
            flush()
            continue
        stripped = re.sub(r"^>+\s*", "", stripped)
        starts_item = bool(_LIST_MARK.match(stripped)) or stripped.startswith("#")
        stripped = _LIST_MARK.sub("", stripped).lstrip("#").strip()
        cleaned = _clean_line(stripped)
        if not cleaned:
            flush()
            continue
        if starts_item:
            flush()
        current.append(cleaned)
    flush()
    return paragraphs


def split_front_matter(markdown: str) -> str:
    if markdown.startswith("---"):
        end = markdown.find("\n---", 3)
        if end != -1:
            return markdown[end + 4:]
    return markdown


def extract_sections(markdown: str) -> dict[str, list[str]]:
    """{節名: [正規化済みの段落, ...]}。節が無ければ KeyError にせず空で返し、呼び出し側が判断する。"""
    body = split_front_matter(markdown)
    chunks: dict[str, list[str]] = {}
    name: str | None = None
    buf: list[str] = []

    def close() -> None:
        if name is not None:
            chunks[name] = normalize_paragraphs("\n".join(buf))

    for line in body.splitlines():
        if line.startswith("## "):
            close()
            heading = line[3:].strip()
            name = next((s for s in SECTIONS if heading.startswith(s)), None)
            buf = []
        elif name is not None:
            buf.append(line)
    close()
    return chunks


def sections_text(sections: dict[str, list[str]]) -> str:
    return "\n".join(f"【{n}】\n" + "\n".join(sections.get(n, [])) for n in SECTIONS)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def body_sha256(markdown: str) -> str:
    return sha256_text(sections_text(extract_sections(markdown)))


def request_body(sections: dict[str, list[str]], max_bytes: int = BODY_MAX_BYTES) -> str:
    """依頼に入れる本文。段落単位（長い段落は文単位）で max_bytes 以内に切る。"""
    out: list[str] = []
    used = 0

    def take(piece: str) -> bool:
        nonlocal used
        cost = len(piece.encode("utf-8")) + 1
        if used + cost > max_bytes:
            return False
        out.append(piece)
        used += cost
        return True

    for name in SECTIONS:
        if not take(f"【{name}】"):
            break
        for paragraph in sections.get(name, []):
            if take(paragraph):
                continue
            kept = ""
            for sentence in re.findall(r".*?(?:。|$)", paragraph):
                if not sentence:
                    continue
                if len((kept + sentence).encode("utf-8")) + used + 1 > max_bytes:
                    break
                kept += sentence
            if kept:
                take(kept)
            break  # 入りきらなかった段落以降は出さない
    return "\n".join(out)


# --- 依頼・答えの契約（schemas/ の複製に従う） --------------------------------------

def _validate(instance, schema, path="$") -> list[str]:
    """schemas/*.json が使っている JSON Schema の部分集合だけを評価する（外部依存なし）。"""
    errors: list[str] = []
    if "oneOf" in schema:
        matches = sum(1 for s in schema["oneOf"] if not _validate(instance, s, path))
        if matches != 1:
            errors.append(f"{path}: oneOf に{matches}件一致")
        return errors
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: const {schema['const']!r} ではない")
    kind = schema.get("type")
    checker = {"object": dict, "string": str, "integer": int, "array": list, "boolean": bool, "null": type(None)}
    if kind:
        ok = isinstance(instance, checker[kind]) and not (kind == "integer" and isinstance(instance, bool))
        if not ok:
            return errors + [f"{path}: type {kind} ではない"]
    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}: minLength")
        if len(instance) > schema.get("maxLength", 10**9):
            errors.append(f"{path}: maxLength")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: pattern")
    if isinstance(instance, int) and not isinstance(instance, bool) and instance < schema.get("minimum", -10**18):
        errors.append(f"{path}: minimum")
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: {key} が無い")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            errors += [f"{path}: 未知のキー {k}" for k in instance if k not in props]
        for key, sub in props.items():
            if key in instance:
                errors += _validate(instance[key], sub, f"{path}.{key}")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: minItems")
        if schema.get("uniqueItems") and len({json.dumps(i, sort_keys=True) for i in instance}) != len(instance):
            errors.append(f"{path}: uniqueItems")
        if "items" in schema:
            for i, item in enumerate(instance):
                errors += _validate(item, schema["items"], f"{path}[{i}]")
    return errors


def validate_message(message: dict, kind: str) -> list[str]:
    schema = json.loads((SCHEMA_DIR / f"element-{kind}.schema.json").read_text(encoding="utf-8"))
    return _validate(message, schema)


# --- 値の確認（すべてプログラム） ---------------------------------------------------

def reference_token(value: str) -> str | None:
    if re.search(r"https?://|www\.", value):
        return "URL"
    if re.search(r"\b[PQ]\d+\b", value):
        return "ID"
    if re.search(r"\[[^\]]*\]\(|\*\*|`|^\s*>|\|", value):
        return "Markdown記法"
    return None


def check_value(value, request: dict) -> list[dict]:
    """落ちた確認を [{check, reason}] で返す。通れば空。"""
    failures: list[dict] = []
    fmt = request["answer_format"]
    if not isinstance(value, str) or not value.strip():
        return [{"check": "non_empty", "reason": "空でない値を返してください。"}]
    if "\n" in value or "\r" in value:
        failures.append({"check": "single_line", "reason": "改行を含めず、1行で返してください。"})
    if len(value) < fmt.get("min_chars", 1):
        failures.append({"check": "min_chars", "reason": f"{fmt['min_chars']}字以上で返してください。"})
    if len(value) > fmt["max_chars"]:
        failures.append({"check": "max_chars", "reason": f"{fmt['max_chars']}字以内で返してください。"})
    for spec in request["checks"]:
        name, _, arg = spec.partition(":")
        if name == "exact_input_excerpt":
            if value not in request["inputs"][arg]:
                failures.append({"check": spec, "reason": "入力の本文にある文字列を、一字も変えずにそのまま抜き書きしてください。"})
        elif name == "exact_input_excerpt_or_none":
            if value == NO_MORE:
                continue
            if not QUOTE_MIN <= len(value) <= QUOTE_MAX:
                failures.append({"check": spec, "reason": f"{QUOTE_MIN}〜{QUOTE_MAX}字の抜き書きか、「{NO_MORE}」だけを返してください。"})
            elif value not in request["inputs"][arg]:
                failures.append({"check": spec, "reason": "入力の本文にある文字列を、一字も変えずにそのまま抜き書きしてください。"})
        elif name == "distinct_from_input":
            other = request["inputs"][arg]
            if value != NO_MORE and (value in other or other in value):
                failures.append({"check": spec, "reason": f"{arg} と重ならない別の箇所を選んでください。"})
        elif name == "no_reference_tokens":
            kind = reference_token(value)
            if kind:
                failures.append({"check": spec, "reason": f"{kind}を含めず、本文の文章だけを抜き書きしてください。"})
        elif name == "forbidden":
            bad = [t for t in arg.split(",") if t in value]
            if bad:
                failures.append({"check": spec, "reason": f"「{bad[0]}」を含む部分は選ばないでください。"})
        else:
            raise ValueError(f"unknown check: {spec}")
    return failures


# --- 依頼の生成 ---------------------------------------------------------------------

def element_id(slug: str, index: int) -> str:
    return f"K1.card.trend.{slug}.{index}"


def build_request(run_id: str, slug: str, index: int, attempt: int, body: str,
                  first_quote: str | None, previous_failure: list[dict] | None) -> dict:
    if index == 1:
        instruction, inputs = INSTRUCTION_FIRST, {"body": body}
        answer_format = {"type": "text", "min_chars": QUOTE_MIN, "max_chars": QUOTE_MAX}
        checks = ["exact_input_excerpt:body", "no_reference_tokens", "forbidden:" + ",".join(FORBIDDEN_IN_QUOTE)]
    else:
        instruction, inputs = INSTRUCTION_SECOND, {"body": body, "first_quote": first_quote}
        answer_format = {"type": "text", "min_chars": len(NO_MORE), "max_chars": QUOTE_MAX}
        checks = ["exact_input_excerpt_or_none:body", "distinct_from_input:first_quote",
                  "no_reference_tokens", "forbidden:" + ",".join(FORBIDDEN_IN_QUOTE)]
    request = {
        "contract_version": REQUEST_CONTRACT,
        "run_id": run_id,
        "element_id": element_id(slug, index),
        "attempt": attempt,
        "instruction": instruction,
        "inputs": inputs,
        "answer_format": answer_format,
        "checks": checks,
        "previous_failure": previous_failure or None,
    }
    errors = validate_message(request, "request")
    if errors:
        raise ValueError("request が契約に合わない: " + "; ".join(errors))
    return request


# --- 保存 ---------------------------------------------------------------------------

def load_state(path: Path = STATE_PATH) -> dict:
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"contract_version": STATE_VERSION, "request_contract": REQUEST_CONTRACT,
            "answer_contract": ANSWER_CONTRACT, "entries": {}}


def save_state(state: dict, path: Path = STATE_PATH) -> None:
    text = json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".card-excerpts.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


# --- git の固定 commit から本文を読む ------------------------------------------------

def git_blob(commit: str, path: str, root: Path = ROOT) -> bytes:
    return subprocess.run(["git", "-C", str(root), "show", f"{commit}:{path}"],
                          capture_output=True, check=True).stdout


def head_commit(root: Path = ROOT) -> str:
    return subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.strip()


def trend_files(root: Path = ROOT) -> dict[str, str]:
    """{entity_id: リポジトリ相対パス}。"""
    out = {}
    for path in sorted((root / "entities" / "trends").glob("*.md")):
        out[f"trend/{path.stem}"] = f"entities/trends/{path.name}"
    return out


def locate(quote: str, sections: dict[str, list[str]]) -> str | None:
    for name in SECTIONS:
        if any(quote in paragraph for paragraph in sections.get(name, [])):
            return name
    return None


def build_card(entity_path: str, quotes: list[str], markdown_bytes: bytes) -> list[dict] | None:
    """保存済みの抜き書きが本文に一字一句あるときだけ card を返す。一つでも無ければ None。"""
    sections = extract_sections(markdown_bytes.decode("utf-8"))
    source_sha = hashlib.sha256(markdown_bytes).hexdigest()
    card = []
    for quote in quotes:
        where = locate(quote, sections)
        if where is None:
            return None
        card.append({"text": quote, "source_locator": f"{entity_path}#{where}", "source_sha256": source_sha})
    return card


def entry_quotes(entry: dict | None) -> list[str] | None:
    """両要素が受理済みなら抜き書きの並び（「これ以上なし」は除く）。未完了なら None。"""
    if not entry:
        return None
    elements = entry.get("elements", {})
    accepted = [elements.get(i, {}).get("accepted") for i in ("1", "2")]
    if accepted[0] is None or accepted[1] is None:
        return None
    return [q for q in accepted if q != NO_MORE]


def export_card(entity_id: str, entity_path: str, commit: str, state: dict | None = None,
                root: Path = ROOT) -> list[dict]:
    """export_signals 用。固定 commit の本文と照合できた card、できなければ空。"""
    state = state if state is not None else load_state()
    entry = state["entries"].get(entity_id)
    quotes = entry_quotes(entry)
    if not quotes:
        return []
    try:
        blob = git_blob(commit, entity_path, root)
    except subprocess.CalledProcessError:
        return []
    if body_sha256(blob.decode("utf-8")) != entry["body_sha256"]:
        return []
    return build_card(entity_path, quotes, blob) or []


# --- 答え手 ---------------------------------------------------------------------------

class AnswererError(RuntimeError):
    pass


def command_answerer(argv: list[str], timeout: int = 600):
    """stdin に依頼1件、stdout に答え1件を返す外部コマンドを答え手にする。"""
    def answer(request: dict) -> dict:
        try:
            result = subprocess.run(argv, input=json.dumps(request, ensure_ascii=False),
                                    capture_output=True, text=True, encoding="utf-8",
                                    timeout=timeout, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise AnswererError(f"answerer が応答しない: {exc}") from exc
        if result.returncode:
            raise AnswererError(f"answerer が終了コード {result.returncode}: {result.stderr.strip()[:200]}")
        try:
            message = json.loads(result.stdout)
        except ValueError as exc:
            raise AnswererError("answerer の stdout が JSON 1件ではない") from exc
        errors = validate_message(message, "answer")
        if errors:
            raise AnswererError("answer が契約に合わない: " + "; ".join(errors))
        if any(message[k] != request[k] for k in ("run_id", "element_id", "attempt")):
            raise AnswererError("answer が依頼と対応しない")
        return message
    return answer


# --- 生成（1件ずつ、要素ごとに保存） ---------------------------------------------------

class ElementBlocked(Exception):
    def __init__(self, element: str, failures: list[dict]):
        super().__init__(f"{element}: {MAX_ATTEMPTS}回で確認に通らない: {failures}")
        self.element = element
        self.failures = failures


def pending_entities(state: dict, files: dict[str, str], commit: str, root: Path = ROOT) -> list[str]:
    """本文の sha256 が保存と違う、または要素が揃っていない trend。"""
    todo = []
    for entity_id, path in files.items():
        markdown = git_blob(commit, path, root).decode("utf-8")
        entry = state["entries"].get(entity_id)
        if not entry or entry.get("body_sha256") != body_sha256(markdown) or entry_quotes(entry) is None:
            todo.append(entity_id)
    return todo


def run_element(state: dict, entity_id: str, index: int, body: str, first_quote: str | None,
                answerer, run_id: str, save) -> str:
    slug = entity_id.split("/", 1)[1]
    element = state["entries"][entity_id]["elements"].setdefault(str(index), {"attempts": [], "accepted": None})
    if element["accepted"] is not None:
        return element["accepted"]
    transport_errors = 0
    while True:
        attempts = element["attempts"]
        if len(attempts) >= MAX_ATTEMPTS:
            raise ElementBlocked(element_id(slug, index), attempts[-1]["failures"])
        previous = attempts[-1]["failures"] if attempts else None
        request = build_request(run_id, slug, index, len(attempts) + 1, body, first_quote, previous)
        try:
            message = answerer(request)
        except AnswererError:
            transport_errors += 1
            if transport_errors >= 3:
                raise
            continue
        transport_errors = 0
        value = message["value"]
        failures = check_value(value, request)
        attempts.append({"attempt": request["attempt"], "value": value, "failures": failures})
        if not failures:
            element["accepted"] = value
            element["accepted_sha256"] = sha256_text(value)
        save()
        if not failures:
            return value


def generate(answerer, *, entities: list[str] | None = None, limit: int = 0, root: Path = ROOT,
             state_path: Path = STATE_PATH, run_id: str = "card-excerpts", log=print) -> dict:
    commit = head_commit(root)
    dirty = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--", "entities"],
                           capture_output=True, text=True, check=True).stdout.strip()
    if dirty:
        raise SystemExit("entities/ に未コミットの変更がある。固定 commit の本文と食い違うため中止する:\n" + dirty)
    state = load_state(state_path)
    files = trend_files(root)
    if entities:
        unknown = [e for e in entities if e not in files]
        if unknown:
            raise SystemExit(f"そのIDは無い: {unknown}")
        files = {e: files[e] for e in entities}
    todo = pending_entities(state, files, commit, root)
    if limit:
        todo = todo[:limit]
    blocked: dict[str, str] = {}
    for n, entity_id in enumerate(todo, 1):
        path = files[entity_id]
        markdown_bytes = git_blob(commit, path, root)
        markdown = markdown_bytes.decode("utf-8")
        sections = extract_sections(markdown)
        missing = [s for s in SECTIONS if not sections.get(s)]
        if missing:
            blocked[entity_id] = f"節が無い: {missing}"
            continue
        digest = body_sha256(markdown)
        entry = state["entries"].get(entity_id)
        superseded = (entry or {}).get("superseded", [])
        if entry and entry.get("body_sha256") != digest:
            superseded = superseded + [{k: v for k, v in entry.items() if k != "superseded"}]
            entry = None
        if entry is None:
            state["entries"][entity_id] = {
                "body_sha256": digest, "source_commit": commit,
                "source_sha256": hashlib.sha256(markdown_bytes).hexdigest(), "elements": {},
                **({"superseded": superseded} if superseded else {})}
        body = request_body(sections)
        save = lambda: save_state(state, state_path)  # noqa: E731
        try:
            first = run_element(state, entity_id, 1, body, None, answerer, run_id, save)
            run_element(state, entity_id, 2, body, first, answerer, run_id, save)
        except (ElementBlocked, AnswererError) as exc:
            blocked[entity_id] = str(exc)
            save()
            log(f"[{n}/{len(todo)}] {entity_id}: BLOCKED {exc}")
            continue
        quotes = entry_quotes(state["entries"][entity_id])
        log(f"[{n}/{len(todo)}] {entity_id}: {len(quotes)}件")
    save_state(state, state_path)
    return {"commit": commit, "processed": len(todo), "blocked": blocked}


# --- 検証 -----------------------------------------------------------------------------

def verify(commit: str | None = None, state: dict | None = None, root: Path = ROOT) -> list[str]:
    """全 trend にカードがあり、すべての抜き書きが固定 commit の本文に一字一句あることを確かめる。"""
    commit = commit or head_commit(root)
    state = state if state is not None else load_state()
    problems: list[str] = []
    for entity_id, path in trend_files(root).items():
        entry = state["entries"].get(entity_id)
        quotes = entry_quotes(entry)
        if not quotes:
            problems.append(f"{entity_id}: カードが無い")
            continue
        blob = git_blob(commit, path, root)
        markdown = blob.decode("utf-8")
        if body_sha256(markdown) != entry["body_sha256"]:
            problems.append(f"{entity_id}: 本文が保存時から変わっている（再生成が必要）")
            continue
        sections = extract_sections(markdown)
        for q in quotes:
            if not QUOTE_MIN <= len(q) <= QUOTE_MAX:
                problems.append(f"{entity_id}: 長さが{QUOTE_MIN}〜{QUOTE_MAX}字でない: {q!r}")
            if locate(q, sections) is None:
                problems.append(f"{entity_id}: 本文に一字一句ない: {q!r}")
            if reference_token(q) or any(t in q for t in FORBIDDEN_IN_QUOTE):
                problems.append(f"{entity_id}: 未確認・URL・IDを含む: {q!r}")
        if len(quotes) == 2 and (quotes[0] in quotes[1] or quotes[1] in quotes[0]):
            problems.append(f"{entity_id}: 2つの抜き書きが重なる")
        if hashlib.sha256(git_blob(entry["source_commit"], path, root)).hexdigest() != entry["source_sha256"]:
            problems.append(f"{entity_id}: source_sha256 が保存の commit の blob と合わない")
    return problems


# --- CLI ------------------------------------------------------------------------------

DEFAULT_ANSWERER = [sys.executable, str(ROOT / "tools" / "haiku_answerer.py")]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="やり直しが要る trend の数を出す")
    nxt = sub.add_parser("next", help="次の依頼を1件、標準出力へ出す")
    nxt.add_argument("--entity", required=True)
    gen = sub.add_parser("generate", help="答え手に1件ずつ依頼して保存する")
    gen.add_argument("--entity", action="append", help="対象を絞る（複数可）")
    gen.add_argument("--limit", type=int, default=0)
    gen.add_argument("--answerer", nargs="+", default=DEFAULT_ANSWERER,
                     help="stdin に依頼1件、stdout に答え1件を返すコマンド（既定: tools/haiku_answerer.py）")
    gen.add_argument("--timeout", type=int, default=600)
    sub.add_parser("verify", help="全 trend のカードを固定 commit の本文と照合する")
    args = ap.parse_args(argv)

    if args.command == "status":
        commit = head_commit()
        todo = pending_entities(load_state(), trend_files(), commit)
        print(json.dumps({"commit": commit, "trends": len(trend_files()), "pending": len(todo)}, ensure_ascii=False))
        return 0
    if args.command == "next":
        files = trend_files()
        if args.entity not in files:
            print(f"ERROR: そのIDは無い: {args.entity}", file=sys.stderr)
            return 1
        state = load_state()
        entry = state["entries"].get(args.entity) or {}
        sections = extract_sections(git_blob(head_commit(), files[args.entity]).decode("utf-8"))
        slug = args.entity.split("/", 1)[1]
        elements = entry.get("elements", {})
        first = elements.get("1", {}).get("accepted")
        index = 1 if first is None else 2
        attempts = elements.get(str(index), {}).get("attempts", [])
        previous = attempts[-1]["failures"] if attempts else None
        print(json.dumps(build_request("card-excerpts", slug, index, len(attempts) + 1, request_body(sections),
                                       first, previous), ensure_ascii=False, indent=2))
        return 0
    if args.command == "generate":
        report = generate(command_answerer(args.answerer, args.timeout), entities=args.entity, limit=args.limit)
        print(json.dumps(report, ensure_ascii=False))
        return 1 if report["blocked"] else 0
    problems = verify()
    for line in problems:
        print(line, file=sys.stderr)
    print(f"trend {len(trend_files())} 件、問題 {len(problems)} 件")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
