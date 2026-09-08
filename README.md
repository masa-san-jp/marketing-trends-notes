# marketing-trends-notes

外部のマーケティング・トレンドと施策を、時間・チャネル・関係の3軸で蓄積する
Markdown + Git のナレッジベースです。自社の計測値や施策実績を保存するリポジトリではありません。

## Agentic Art全体との関係と利用方法

8リポジトリ全体の人間向け案内は、親repoの[repository map](https://github.com/masa-san-jp/agentic-art-orchestration/blob/main/docs/repository-map.md)を正本とします。このREADMEにも、役割と利用入口を次の通り表示します。

```text
self-model-notes ─┐
art-history-notes ├─ normalized research signal ─┐
marketing-trends ┘                               │
                                                 ▼
viewer-response-notes ─ feedback ─→ agentic-art-orchestration
                                                 │
                                                 ▼
                                       agentic-art-research
                                                 │ production-handoff
                                                 ▼
                                       agentic-art-production
                                                 │ canonical plan
                                                 ▼
                                       agentic-art-project
                                           公開カタログ
```

| リポジトリ | 役割 |
|---|---|
| [agentic-art-orchestration](https://github.com/masa-san-jp/agentic-art-orchestration) | 全体のcontrol plane。workspace、pin、retrieval、実行、再開、検証 |
| [self-model-notes](https://github.com/masa-san-jp/self-model-notes) | 本人の明示的・同意済みの自己モデル |
| [art-history-notes](https://github.com/masa-san-jp/art-history-notes) | 美術史上の作品、技法、関係、根拠 |
| [marketing-trends-notes](https://github.com/masa-san-jp/marketing-trends-notes) | 社会・市場の変化と鮮度付きの根拠 |
| [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research) | 入力知識を使った調査、仮説、要件、判断 |
| [agentic-art-production](https://github.com/masa-san-jp/agentic-art-production) | handoffを受けた制作プラン、試作、制作結果 |
| [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes) | 鑑賞者反応の集計と保守的な評価 |
| [agentic-art-project](https://github.com/masa-san-jp/agentic-art-project) | 検証済みの公開プラン、作品、制作記録のカタログ |

### 利用者の入口

- 制作を始める: [OrchestrationのREADME](https://github.com/masa-san-jp/agentic-art-orchestration#利用者向けの最短ルート)と[agent-runtime-guide](https://github.com/masa-san-jp/agentic-art-orchestration/blob/main/docs/agent-runtime-guide.md)から始める。個別repoを順番に手操作しない。
- 知識を更新する: 更新対象repoのREADME、Issue、schema、validatorを正本として使い、親へ本文をコピーしない。
- Research/Productionを確認する: [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research)と[agentic-art-production](https://github.com/masa-san-jp/agentic-art-production)の各入口を読む。
- 公開プランや作品を見る: [agentic-art-projectのplans/とworks/](https://github.com/masa-san-jp/agentic-art-project)を開く。
- 鑑賞者反応を戻す: [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes)で集計し、次回Researchで再検証する。

各repoは独立した正本を持ち、内部log、会話、prompt、credential、PRIVATE_RAW、RESTRICTEDを兄弟repoへ渡しません。

### このrepoの使い方

このrepoは外部マーケティング情報の入力KBです。trendとpracticeの鮮度、出典の利害、反証を保持し、research-signal-export/v1などの明示契約でResearchへ渡します。自社実績や他repoの本文をこのrepoの事実へ混ぜません。


## まずこれだけ

### 初回セットアップ

```bash
make setup
make preflight
make test
```

基準Pythonは [`.python-version`](.python-version) に従います。依存関係は `.venv` に入り、以後の
検証は `.venv/bin/python` を使うため、シェルのPython環境に左右されません。

### 読む

```bash
.venv/bin/python tools/bundle.py --search リテールメディア
.venv/bin/python tools/bundle.py trend/<slug>
```

全体の空白・鮮度・出典未読は [overviews/coverage.md](overviews/coverage.md) と
`data/coverage.json` を見ます。

### エージェントとして動かす

1. [AGENTS.md](AGENTS.md) を読む
2. GitHub issue の契約を確認する
3. `.venv/bin/python tools/agent_task.py next --json` で次の issue を探す
4. `claim` → 実装 → `make agent-verify ISSUE=N NOW=YYYY-MM-DD` の順に進める
5. 完了証跡を issue / PR に残す

このハーネスはローカルで動作し、エージェントモデル自身を起動しません。GitHub Actions は補助機能であり、
エージェント実行の前提ではありません。現在は全 workflow を `disabled_manually` にしているため、push・PR・
issueイベントでrunnerや課金対象処理は起動しません。バックグラウンドで調査やRSS取得を始める処理もありません。

**要件の正本は issue #1、repository-side agent harness の正本は issue #78 です。**
この README は現状の説明であり、要件と食い違う場合は issue を正とします。

**俯瞰と細部を同じ形式で持ち、時間・チャネル・関係の3軸で構造化します。** トレンドの箇条書きだけでは
「その変化がどの段階で、どこで起きていて、どの打ち手がそれに応答しているか」が見えないためです。

構造は [art-history-notes](https://github.com/masa-san-jp/art-history-notes) のフォーク。ただし
**美術史の事実は固まるが、マーケティングの事実は腐る**——この一点のために、鮮度（`freshness`）・
出典の利害（`certainty: vendor`）・反証と予測の答え合わせを一級市民にしている。詳しくは
[docs/schema.md](docs/schema.md) と [docs/freshness.md](docs/freshness.md)。

## 関連リポジトリと関係性

このリポジトリは、マーケティングの外部情報を蓄積する「入力ナレッジベース」です。兄弟リポジトリを
submoduleや実行時依存として取り込まず、他repoのデータを自動で同期もしません。連携が必要な場合は、
[tools/export_signals.py](tools/export_signals.py) が出力する `research-signal-export/v1` のような、
明示された境界契約を使います。

| リポジトリ | 役割 | このrepoとの関係 |
|---|---|---|
| [art-history-notes](https://github.com/masa-san-jp/art-history-notes) | 美術史の入力KB | 構造とスキーマの先行例。このrepoはマーケティング向けに分岐した独立KBで、データを共有する依存先ではない。 |
| [self-model-notes](https://github.com/masa-san-jp/self-model-notes) | 自己モデルの入力KB | 別領域の並列KB。根拠・claims・パターンの正本は独立しており、このrepoの必須依存ではない。 |
| [viewer-response-notes](https://github.com/masa-san-jp/viewer-response-notes) | 視聴者反応の入力KB | 隣接する研究入力。反応データをこのrepoのトレンド事実へ自動で混ぜず、必要な連携は契約経由で行う。 |
| [agentic-art-research](https://github.com/masa-san-jp/agentic-art-research) | research runtime | 入力KBの根拠を研究要件・判断・出力へ扱う下流の実行系。このrepoのマーケティング事実の正本ではない。 |
| [agentic-art-production](https://github.com/masa-san-jp/agentic-art-production) | production runtime | research側のproduction handoffを受けて制作・実行・結果を扱う。マーケティングKBの更新や事実認定は担わない。 |
| [agentic-art-orchestration](https://github.com/masa-san-jp/agentic-art-orchestration) | control plane | 兄弟repoの関係、契約、quality gateを束ねる調整系。このrepoのデータ置き場でも実行時の必須依存でもない。 |
| [Thug-Fugu](https://github.com/masa-san-jp/Thug-Fugu) | 任意のローカルLLM実行基盤 | ローカルLLMの役割分担・並列実行を担う別repo。このrepoはモデルやThug-Fuguを自動起動せず、必須依存にもしていない。 |

関係を一言で言えば、`marketing-trends-notes` は「根拠付きのマーケティング入力」を持ち、research / production / orchestration
系が必要なときだけ境界契約を通じて利用します。したがって、利用者がこのrepoだけをcloneしてもKBの閲覧・編集・ローカル検証は完結し、
兄弟repoやGitHub Actionsへの登録を追加で要求されません。

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
  run_atmosphere_pipeline.py 空気感観測の検証・X環境確認・任意のRSS取得を一括実行
  bundle.py          知識のまとまりを1文書として取り出す
  linkcheck.py       出典URLの死活確認（ネットワークに出るので別枠）
  record_searched.py 調べたが該当が無かったカテゴリを1行残す（空欄と区別する）
Makefile             setup / preflight / test の安定した入口
AGENTS.md            実行エージェントの入口と停止条件
data/              生成物（graph.json / coverage.json / audit.json）と追記ログ（queries.jsonl / searched.jsonl /
                  social-observations.jsonl）
```

## 3軸をどう持っているか

- **時間** — `time.start` / `end` は **EDTF**（`202X`＝2020年代／`2020~`＝およそ／`..`＝継続中／
  `null`＝不明）。加えて **`stage`**（emerging → growing → peak → declining → dead）と
  **`freshness`**（いつ確認したか・いつまでに再検証するか）。期限は stage から機械が導出する。
- **チャネル** — `channels` に役割付きの参照（`originated_on` / `spread_to` / `commoditized_on` /
  `observed_on`）。「TikTok 発の形式が Shorts に伝播した」を後から引ける。カテゴリ（`market`）と
  地理（`geo`）は `config/markets.yaml` のバケット。trend の適用範囲は `channel_scope` で明示する。
- **関係** — 閉じた語彙。**`responds_to`（施策→トレンド）が背骨**で、**`killed_by`（→イベント）が
  マーケ固有**（ATT が何を殺したかを機械可読に持つ）。解釈を含む関係は確度と出典が必須。

主役は `trend`。**必須の `kind`**（需要変化／技術起点／規制起点／**ベンダーが売り込んだ括り**）で
成因を、`stage` で段階を、独立に持つ。名付けの来歴は `naming` で分けて持つ——名前の存在と現象の
存在を混同しないため。

**出典は2つの独立した軸で持つ。** `certainty` ＝ 誰が出したか・利害があるか（`measured` /
`independent` / `attested` / `vendor` / `anecdotal` / `hypothesis`）、`retrieved` ＝ **自分が原典を
開いたか**（`primary` / `summary`）。権威あるURLは読まずにも貼れるので、後者が無いと未読の資料が
出典付きのまま入る。**verified を名乗るには vendor 以外の根拠が1本、かつ `retrieved: primary` の
根拠が1本**——どちらも検証が強制する。

## 日常操作

エンティティを追加・更新するときは、入力のMarkdownを直してから生成物を更新する。
`data/` と `overviews/coverage.md` の生成ブロックは手で編集しない。

```bash
.venv/bin/python tools/new_entity.py trend <slug> --ja "<名前>" --stage growing
.venv/bin/python tools/build_graph.py             # 検証 + グラフ・被覆マップの生成
.venv/bin/python tools/audit.py                   # 次に調べることを出す
.venv/bin/python tools/observe_social.py --check  # SNS空気感ログの形式検証
.venv/bin/python tools/observe_social.py --summary
.venv/bin/python tools/bundle.py --search リテールメディア
.venv/bin/python tools/bundle.py trend/<slug>
```

外部の公開検索関心やSNSを観測するときだけ、対応する観測コマンドを実行する。X tokenが無い場合は
X観測をスキップできる。RSS取得は `--collect-rss` を明示したときだけ行われる。

`make preflight` はネットワークへ接続せず、Python、固定依存、git、hooksPathを検査する。
GitHub issueを扱う作業で `gh` を必須にする場合は `.venv/bin/python tools/preflight.py --require-gh` を使う。
`make agent-verify` は issue契約、KB検証、strict audit、export契約、生成物整合性、worktree不変性を
まとめて判定する読み取り専用の統合完了ゲートである。

1件の調査は [docs/investigation-task.md](docs/investigation-task.md) の手順だけで進める。
読み手向けの入口は [docs/for-other-personas.md](docs/for-other-personas.md) にまとめている。

## 検証

検査は2層。**`build_graph.py --check` は「壊れているか」**（必須項目・参照先・語彙・EDTF・
鮮度の整合・反証見出し）を見て commit を止める。**`audit.py` は「噛み合っていないか」**
（鮮度切れ・vendor 単独根拠・答え合わせしていない予測・応答なきトレンド・単一チャネル観測）を見て、
止めずに**次に調べることとして出す**。形が正しいだけの体系は、機械が黙っているうちに静かに腐る。

`.githooks/pre-commit` が commit のたびに `build_graph.py --check` と生成物の整合性を検査し、通らないものを止める。
生成物（`data/` と被覆マップ）が古いままの commit も止める。

GitHub Actionsのworkflow定義は補助機能として残しているが、現在はすべて自動実行を無効にしている。
必要な検証と完了判定は、エージェントがローカルで `make agent-verify` と
`.venv/bin/python tools/validate_agent_completion.py` を実行して行う。workflowを再有効化しない限り、
GitHub Actions、GitHub Actionsへの登録、GitHubの課金設定は不要である。

**clone した直後に1回だけ**（これをしないとフックは動かない）:

```bash
git config core.hooksPath .githooks
```

忘れても気づけるようにしてある——設定されていない状態で `build_graph.py` を走らせると警告が出る。

## 書くときの規律

- 出典URLを本文に置く。手元の知識だけで書いた行は書かない。
- **ベンダー発の数字は `vendor` と明記し、断定に使わない。** その主張で儲かる側の数字は
  「調査レポート」の顔で来る。
- **公開された外部観測を最優先する。** 書き手自身の実施有無や自社数値はこのKBに記録しない。
- **外部資料で効果が確認できない施策は「効果未確認」と明記する。**
- 確定できないことは `**未確認**:` として残す。空欄で隠さない。
- **トレンドには反証を書く**——「これが偽なら何が観測されるか」を最低1つ。書けないなら、
  それはトレンドではなく感想（検証が見出しの存在を落とす）。
- 「バズっている」を規模の出典にしない。

詳細は [docs/schema.md](docs/schema.md)。

## いま入っているもの

`python3 tools/build_graph.py` の出力が正確な現在地（件数をここに書き写すと必ず古くなる）。
空白の全体像は [overviews/coverage.md](overviews/coverage.md)。

## Research観測の保存と再利用

AAK-07の候補取込・履歴・鮮度再検証・明示knowledge snapshotからのexportは[research-knowledge-intake](docs/research-knowledge-intake.md)を参照。既存のnative schema/validatorを使用し、code checkoutとowner知識Gitを分離する。
