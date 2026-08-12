# marketing-trends-notes

マーケティング・トレンドのナレッジベース。事業と制作の**判断材料**として書き、積む。

**要件の正本は issue #1。**
この README は現状の説明であって、要件ではない。食い違ったら issue を正とする。

**俯瞰と細部を同じ形式で持ち、時間・チャネル・関係の3軸で構造化する。** トレンドの箇条書きだけでは
「その変化がどの段階で、どこで起きていて、どの打ち手がそれに応答しているか」が見えない。
だから3軸を最初から持つ。

構造は [art-history-notes](https://github.com/masa-san-jp/art-history-notes) のフォーク。ただし
**美術史の事実は固まるが、マーケティングの事実は腐る**——この一点のために、鮮度（`freshness`）・
出典の利害（`certainty: vendor`）・反証と予測の答え合わせを一級市民にしている。詳しくは
[docs/schema.md](docs/schema.md) と [docs/freshness.md](docs/freshness.md)。

## 構造

```
entities/          1エンティティ1ファイル。frontmatter が唯一の正
  trends/  practices/  channels/  cases/  players/  concepts/  events/  sources/
overviews/         俯瞰。coverage.md の表は生成物（手で書き換えない）
config/            markets.yaml = カテゴリ12・地理6バケットと受け入れ条件の閾値
docs/
  schema.md              型・必須項目・関係語彙・evidence・鮮度。書く前に読む
  investigation-task.md  1件の調査の手順（Sonnet が単独で1件を終えられる粒度）
  local-environment.md   X APIをローカルで使うための環境準備
  freshness.md           鮮度と再検証の運用（このKB固有の肝）
  sources-directory.md   出典カタログ（層別。確認済みと未確認を分けてある）
  for-other-personas.md  読み手向けの入口。引用してよい記述の区別
tools/
  kb.py              スキーマ定義と共通部品（1箇所）
  new_entity.py      必須項目が入った雛形を作る
  build_graph.py     検証 → data/graph.json・data/coverage.json・被覆マップ更新
  audit.py           噛み合っていないか（鮮度切れ・vendor単独・未判定の予測…）→ 次に調べること
  observe_social.py SNS上の高い引力を持つ空気感ログを検証・集計（世論推定ではない）
  observe_google_trends.py Google Trends Japan RSSの公開検索関心を取得・比較（SNS推定ではない）
  bundle.py          知識のまとまりを1文書として取り出す
  linkcheck.py       出典URLの死活確認（ネットワークに出るので別枠）
  record_searched.py 調べたが該当が無かったカテゴリを1行残す（空欄と区別する）
data/              生成物（graph.json / coverage.json / audit.json）と追記ログ（queries.jsonl / searched.jsonl /
                  social-observations.jsonl）
```

## 3軸をどう持っているか

- **時間** — `time.start` / `end` は **EDTF**（`202X`＝2020年代／`2020~`＝およそ／`..`＝継続中／
  `null`＝不明）。加えて **`stage`**（emerging → growing → peak → declining → dead）と
  **`freshness`**（いつ確認したか・いつまでに再検証するか）。期限は stage から機械が導出する。
- **チャネル** — `channels` に役割付きの参照（`originated_on` / `spread_to` / `commoditized_on` /
  `observed_on`）。「TikTok 発の形式が Shorts に伝播した」を後から引ける。カテゴリ（`market`）と
  地理（`geo`）は `config/markets.yaml` のバケット。
- **関係** — 閉じた語彙。**`responds_to`（施策→トレンド）が背骨**で、**`killed_by`（→イベント）が
  マーケ固有**（ATT が何を殺したかを機械可読に持つ）。解釈を含む関係は確度と出典が必須。

主役は `trend`。**必須の `kind`**（需要変化／技術起点／規制起点／**ベンダーが売り込んだ括り**）で
成因を、`stage` で段階を、独立に持つ。名付けの来歴は `naming` で分けて持つ——名前の存在と現象の
存在を混同しないため。

**出典は2つの独立した軸で持つ。** `certainty` ＝ 誰が測ったか・利害があるか（`measured` /
`independent` / `attested` / `vendor` / `anecdotal` / `hypothesis`）、`retrieved` ＝ **自分が原典を
開いたか**（`primary` / `summary`）。権威あるURLは読まずにも貼れるので、後者が無いと未読の資料が
出典付きのまま入る。**verified を名乗るには vendor 以外の根拠が1本、かつ `retrieved: primary` の
根拠が1本**——どちらも検証が強制する。

## 使う

初回は [ローカル環境の準備](docs/local-environment.md) に従って仮想環境と依存関係を用意する。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python3 tools/new_entity.py trend <slug> --ja "<名前>" --stage growing
python3 tools/build_graph.py --check     # 検証だけ（CI 用）
python3 tools/build_graph.py             # 検証 + グラフ・被覆マップの生成
python3 tools/audit.py                   # 鮮度切れ・食い違い → 次に調べること
python3 tools/observe_social.py --check  # SNS空気感ログの形式検証
python3 tools/observe_social.py --summary # SNS空気感ログの集計
python3 tools/observe_google_trends.py --summary # Google Trends RSSの現時点スナップショット
python3 tools/observe_google_trends.py \
  --compare /path/to/previous.json \
  --output /path/to/current.json --summary # 前回との差分付き保存
python3 tools/check_x_env.py                 # X未設定ならスキップして続行
python3 tools/audit.py --dry-run --now $(date +%F)   # 生きた時計で鮮度を見る
python3 tools/bundle.py --search リテールメディア     # 語で探す（IDを知らなくていい）
python3 tools/bundle.py trend/<slug>                 # 1件とその周辺を1文書で
python3 tools/bundle.py --category entertainment-content
```

1件の調査は [docs/investigation-task.md](docs/investigation-task.md) の手順だけで終わる
（判定に迷わないよう kind・stage・certainty の判定表がそこにある）。

**他の人格（アイコたち）が読むときは [docs/for-other-personas.md](docs/for-other-personas.md) から。**
引用してよい記述とだめな記述（特に**鮮度切れ**と**ベンダー数字**）の区別がそこに書いてある。

## 検証が自動で走る

検査は2層。**`build_graph.py --check` は「壊れているか」**（必須項目・参照先・語彙・EDTF・
鮮度の整合・反証見出し）を見て commit を止める。**`audit.py` は「噛み合っていないか」**
（鮮度切れ・vendor 単独根拠・答え合わせしていない予測・応答なきトレンド・単一チャネル観測）を見て、
止めずに**次に調べることとして出す**。形が正しいだけの体系は、機械が黙っているうちに静かに腐る。

`.githooks/pre-commit` が commit のたびに `build_graph.py --check` を走らせ、通らないものを止める。
生成物（`data/` と被覆マップ）が古いままの commit も止める。

**clone した直後に1回だけ**（これをしないとフックは動かない）:

```bash
git config core.hooksPath .githooks
```

忘れても気づけるようにしてある——設定されていない状態で `build_graph.py` を走らせると警告が出る。

## 書くときの規律

- 出典URLを本文に置く。手元の知識だけで書いた行は書かない。
- **ベンダー発の数字は `vendor` と明記し、断定に使わない。** その主張で儲かる側の数字は
  「調査レポート」の顔で来る。
- **自分で測った数字を最優先する**（一次情報の最上位は自分の計測）。
- **試していない施策は「未実施」と明記する。**
- 確定できないことは `**未確認**:` として残す。空欄で隠さない。
- **トレンドには反証を書く**——「これが偽なら何が観測されるか」を最低1つ。書けないなら、
  それはトレンドではなく感想（検証が見出しの存在を落とす）。
- 「バズっている」を規模の出典にしない。

詳細は [docs/schema.md](docs/schema.md)。

## いま入っているもの

`python3 tools/build_graph.py` の出力が正確な現在地（件数をここに書き写すと必ず古くなる）。
空白の全体像は [overviews/coverage.md](overviews/coverage.md)。
