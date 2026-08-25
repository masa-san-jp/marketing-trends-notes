# スキーマ v1 — このナレッジベースの骨格

1エンティティ = 1 markdown。**frontmatter が唯一の正**で、グラフ・被覆マップ・バンドルはすべて生成物。
生成物を手で編集しない。

調査の手順は [investigation-task.md](investigation-task.md)。鮮度の運用は [freshness.md](freshness.md)。
要件の正本は issue #1。

設計は [art-history-notes](https://github.com/masa-san-jp/art-history-notes) のスキーマ v2 をフォークした。
共通の判断（単一型＋必須 kind、閉じた関係語彙、EDTF、claims 方式）の根拠はあちらの
`docs/schema.md` と `docs/design-fable-draft.md` にある。この文書は差分を中心に書く。

## なぜこの形か

マーケティングの変化は3つの軸で同時に動く。**時間**（いつ始まりどの段階か）・**チャネル**
（どこで起きてどこへ伝播したか）・**関係**（何への応答か、何が可能にし、何が殺したか）。
年表だけでは「同じ年に TikTok と店頭で別々に何が起きていたか」が見えない。施策のリストだけでは
「その打ち手がどの変化への応答で、いつ飽和したか」が見えない。だから3軸すべてを構造化して持つ。

そのうえで、美術史との決定的な違いが1つある。**美術史の事実は固まるが、マーケティングの事実は腐る。**
新印象派の1886年は永久に1886年だが、「Z世代の主要チャネル」の2024年の検証済み記述は2026年には
偽でありうる。だからこのKBは鮮度（`freshness`）を一級市民にする。加えてマーケ固有の穴が2つ——
**出典の過半が利害を持つ側から来る**こと、**主張が規範的**（何が効くか）で反証を書かないと
占いになること。スキーマの差分はすべてこの3点への対処である。

## エンティティ型（8）

| 型 | 置き場 | 何を書くか |
|---|---|---|
| `trend` | `entities/trends/` | **主役**。需要側・社会側の変化。`kind`・`stage`・`market`・`geo`・`naming`・`freshness` が必須 |
| `practice` | `entities/practices/` | 施策の型。供給側の応答（リテールメディア・UGC起点・ABM） |
| `channel` | `entities/channels/` | プラットフォーム・媒体。**伝播の結節点**（空間軸） |
| `case` | `entities/cases/` | 個別の事例・キャンペーン。分解して読む対象 |
| `player` | `entities/players/` | 企業・ブランド・人。運営者・提唱者・実践者・命名者 |
| `concept` | `entities/concepts/` | 概念・フレームワーク（CEP・JTBD・ダブルジョパディ） |
| `event` | `entities/events/` | 時間軸の釘。規制施行・アルゴリズム変更・機能ローンチ・値上げ |
| `source` | `entities/sources/` | 一次資料そのもの。**誰が出したか＝利害を記録する場所** |

ID は `<型>/<slug>`。**ID は変えない**（表記を変えたいときは `label_*` を直す）。
`uri` は `urn:mtn:<型>/<slug>`。slug を変えたら旧 id を `aliases` に残す。

**trend と practice の境界の判定は1行**: **需要側で観測される変化なら trend、供給側の打ち手の型なら
practice**。迷ったら「マーケターが全員消えても起きているか」——起きるなら trend。
（例: ショート動画視聴の主流化は trend、ショート動画広告は practice。「推し活」は trend、
推し活グッズの受注生産は practice。）

**practice と concept の境界**: 実行の手順まで落ちるものが practice、説明の枠組みが concept。
リテールメディアは practice、カテゴリーエントリーポイントは concept。

## frontmatter（trend の例）

```yaml
---
id: trend/short-video-mainstream
uri: urn:mtn:trend/short-video-mainstream
type: trend
kind: tech-enabled            # trend 必須（4値）
stage: peak                   # trend 必須（5値）
market: entertainment-content # trend 必須（config/markets.yaml の categories）
geo: japan                    # trend 必須（同 geographies）
label_ja: ショート動画の主流化
label_en: Short-form video mainstreaming
authority:
  wikidata: null
  none_reason: 「短尺動画」「short-form video」で検索したが現象そのものの項目は無い
time:
  start: "2021"               # EDTF。202X＝2020年代／2021~＝およそ／..＝継続中／null＝不明
  end: ".."
  display: コロナ禍の在宅時間拡大期から
naming:                       # trend 必須
  self_identified: false      # 当事者（視聴者）が「ショート動画」と自称するか
  named_by: null
  named_when: null
  original_label: ショート動画
  note: 業界側の呼称が一般化した型。視聴者側の自称は「TikTok見てる」で媒体名
freshness:                    # trend 必須（stage: dead を除く）
  valid_as_of: "2026-08-10"   # 最後に実データで確認した日
  recheck_by: "2027-02-10"    # stage から導出。手計算しない（--stage 付き new_entity.py が埋める）
evidence:                     # verified を名乗るときは time / kind / stage に必要
  - {field: stage, source: "https://...", certainty: independent, retrieved: primary, as_of: "2026-06"}
predictions:                  # 任意。答え合わせをするための予測
  - {claim: "...", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: mapped              # mapped / not-applicable / unresolved
  note: null                  # mapped は null。その他は適用判断・未確定理由を書く
channels:
  - {role: originated_on, target: channel/tiktok}
  - {role: spread_to, target: channel/youtube}
relations:
  - {type: enabled_by, target: event/..., certainty: independent, source: "https://..."}
sources:
  - https://...               # 本文で使った出典。1本以上
status: draft                 # stub | draft | verified
updated: 2026-08-10
---
```

### `channel_scope` — チャネル軸の適用範囲

すべての trend は、チャネル軸を `channel_scope.status` で明示する。`mapped` は `channels` を1件以上持つ。
特定チャネル発ではない trend は `not-applicable` とし、本文の `## チャネルと伝播` を `note` に折りたたんで
適用対象外の理由を残す。調査未完了の `unresolved` は `status: stub` に限る。`not-applicable` と
`unresolved` の `channels` は空配列にする。

### `kind`（trend 必須・4値）— これは何によって起きたか

| kind | 意味 | 例 |
|---|---|---|
| `demand-shift` | 消費者・社会の側で実際に起きた変化 | 推し活、静かな退職、中古志向 |
| `tech-enabled` | 技術・プラットフォームの変化が可能にした | ショート動画、生成AI活用 |
| `regulation-driven` | 規制・制度が強制した | ポストクッキー、ステマ規制対応 |
| `vendor-pushed` | **供給側が名付けて売り込んだ括り**（カテゴリ創造） | 多くのバズワード |

4つ目が肝。マーケの「トレンド」の相当数はベンダーのカテゴリ創造で、これを `demand-shift` と
同じ棚に置いた瞬間に体系が壊れる。**`vendor-pushed` は「偽」を意味しない**——後から実需が付く
ことがある。その時は kind を訂正し、経緯を本文に残す（訂正が1行の diff で済むのが、型を分けずに
kind にする理由。art-history-notes が Wikidata の型分離の破綻を実測して同じ判断をしている）。

### `stage`（trend 必須・5値）— いまどの段階か

`emerging`（観測され始めた）／`growing`（数字が伸びている）／`peak`（主流化・一般紙到達）／
`declining`（数字が落ちている）／`dead`（終わった）。

**kind と stage は独立に動く。** vendor-pushed のまま peak に行くものがあり（バズワードの一般化）、
demand-shift のまま emerging で消えるものがある。この2軸の組が「いま乗るべきか」の判断材料になる。

`dead` の trend は鮮度管理から外れる——もう動かないので、美術史と同じ「確定した過去」の扱いに
合流する。ただし audit が「何が殺したか」（`killed_by`）を要求する。死因は次のトレンドの寿命を
測る材料だから。

### `naming`（trend 必須）— 名前は誰のものか

マーケティングは名付けの産業なので、命名の来歴は美術史より強く効く。**名前の存在と現象の存在を
混同しない**ためにこのブロックがある。

- `self_identified` — 当事者（消費者・実践者）がその名を使うか。「Z世代」を当事者は名乗らない
- `named_by` — 最初に付けたのは誰か（媒体・コンサル・ベンダー。player の id）
- `named_when` — EDTF
- `rejected_by`（任意）— 当事者がその括りを拒んだ場合、誰が拒んだか（例: 「悟り世代」）

`named_by` がベンダーで `kind: demand-shift` を主張する trend は疑う——名付けた側の利害と
現象の実在は別に検証する（audit の vendor-only 検査がこの疑いを機械化している）。

### `freshness`（trend 必須・stage: dead を除く）— この記述はいつまで有効か

```yaml
freshness:
  valid_as_of: "2026-08-10"   # 最後に実データで確認した日
  recheck_by: "2027-02-10"    # 再検証の期限。stage から機械が導出する
```

`recheck_by` は stage が決める: `emerging` 1ヶ月／`growing` 3ヶ月／`peak` 6ヶ月／`declining`
6ヶ月／`dead` なし。**手で計算しない**——`new_entity.py --stage` が埋め、`build_graph.py` が
stage と食い違う値（導出より遅い期限)を落とす。早める分は許す。運用の詳細は
[freshness.md](freshness.md)。

### `evidence` — 主張ごとの根拠と、`certainty` の語彙

art-history の `claims` に当たる。**`certainty` の語彙だけを「誰が測ったか・利害があるか」に
差し替えた**。マーケの出典は誰かの売り物であることが多く、「研究の通説か仮説か」という美術史の軸
より先に、まず利害の軸で切る必要がある。

| certainty | 意味 |
|---|---|
| `measured` | **再現可能な外部観測**（公開された計測・統計・ログ。書き手の自社数値は含めない） |
| `independent` | 利害のない第三者（官公庁統計・学術研究・査読論文） |
| `attested` | 当事者の一次言明（仕様・規約・決算開示。**自分に不利でも成り立つ事実**） |
| `vendor` | **その主張で儲かる側が出す市場の数字・効果の主張**（ベンダーレポート・代理店調査） |
| `anecdotal` | 事例・証言・個別の観測（バズった投稿のURLはここ） |
| `hypothesis` | 自分の仮説。俯瞰の生成から除外する |

`attested` と `vendor` の線引き: **同じ発行元でも、事実の言明と利害のある主張は別**。
Apple が「ATT は許可を必須にする」と書く開発者文書は attested（仕様の一次言明）。
プラットフォームが「当社広告のROASは平均◯倍」と書くブログは vendor（その主張で儲かる）。
発行元ではなく**その記述で誰が得をするか**で判定する。

### `retrieved` — もう1つの軸。**自分がそれを読んだか**

`certainty` が「誰が出したか」なら、`retrieved` は「自分が原典を開いたか」。**全 evidence 行で必須。**

| `retrieved` | 意味 |
|---|---|
| `primary` | **原典を開いた。** PDF・統計表・規約・決算そのものを取得して、使う数字をその中で見た |
| `summary` | **経由で得た。** 検索結果の要約・二次記事・他者のまとめ・過去の記憶から書いた |

この2軸は独立に動く。官公庁統計のURLを検索結果から拾って貼れば `independent` かつ `summary`——
**利害のない出典であることと、自分が読んだことは別**。権威あるURLは読まずにも貼れてしまうので、
この軸が無いと未読の資料が出典付きのまま体系に入る。

判定は1行で決まる: **その数字を、そのファイル（PDF・表・ページ本文）の中で自分の目で見たか。**
見ていないなら `summary`。「たぶん書いてある」は `summary`。原典を開いたが目的の数字が
見つからなかった場合も `summary`（読めたのは別の部分なので）。

## SNS上の空気感観測

トレンドの裏付けとは別に、特定プラットフォームで人を強く惹きつける話題、感情、言い回し、
模倣、参加衝動を `atmosphere_signal` として記録できる。これは社会全体の世論や普及率を推定
するための値ではなく、プラットフォーム、表示条件、クラスターの偏りを含む観測レイヤーである。
Xの観測範囲やサンプル、文化的なフックを記録する形式と検証方法は
[atmosphere-observation.md](atmosphere-observation.md) に定める。

### `status: verified` の2つの関門

**両方を満たさないと verified を名乗れない**（どちらも検証が強制する）。

1. `measured` / `independent` / `attested` の根拠が最低1本——vendor と anecdotal をいくら重ねても
   verified にならない（**誰が出したか**）
2. `retrieved: primary` の根拠が最低1本——原典を1本も開いていない主張は verified にしない
   （**自分が読んだか**）

verified に evidence が要る field は trend が `time` / `kind` / `stage`、practice が `time`。
各行は `as_of`（いつ時点の数字か）が必須——数字の鮮度は記述の鮮度と別に動く。

### `predictions`（任意）— 答え合わせをするための予測

```yaml
predictions:
  - {claim: "2027年中に◯◯が△△を超える", by: "2027-12", resolved: null, outcome: null}
  - {claim: "...", by: "2026-06", resolved: "2026-07-01", outcome: miss}
```

`outcome` は `hit` / `miss` / `unresolvable`。`by` を過ぎて `resolved` が null のものは audit が
「答え合わせしていない予測」として出す。**当てることではなく、外したと記録することが価値**——
外れの記録だけが、自分の見立ての癖（早すぎる・国内を過大評価する等）を教える。

### `channels` — チャネルの役割語（空間軸）

`originated_on`（発生チャネル）／`spread_to`（伝播先）／`commoditized_on`（飽和したチャネル）／
`observed_on`（観測しただけ）。対象はすべて `channel` エンティティ。

トレンドの「発生地」は物理座標ではなくチャネルとカテゴリなので、art-history の `place`（座標必須）
に当たる結節点を `channel` が担う。地理は trend 直下の `geo`（`config/markets.yaml` の6バケット）
で持つ。「TikTok 発の型が Reels と Shorts に伝播した」は「浮世絵がパリに渡った」と同じ構造で引ける。

特定できないときは**書かない**——ただし audit が「単一チャネル観測」を指す。1つのチャネルでしか
観測していない現象は、世の中の変化ではなくプラットフォーム内の現象かもしれない。

### `relations` — 閉じた語彙と確度

構造的（出典なしで書ける）: `practiced_by` `example_of` `part_of` `precedes` `targets`
`documented_in` `operated_by`

解釈を含む（`certainty` と `source` を必須）: `responds_to` `enabled_by` `killed_by`
`derives_from` `substitutes` `reacts_against` `grouped_as` `diffused_to` `influenced_by`

- **`responds_to`（practice → trend）が体系の背骨。** 打ち手はどの変化への応答かを必ず持つ。
  応答先の無い practice は「なぜやるのか」が無い施策で、audit が逆側（応答されない trend）も指す
- **`killed_by`（→ event）はマーケ固有の必須語彙。** ATT が何を殺したか、ステマ規制が何を殺したか。
  美術史では様式は死因を問わず緩やかに終わるが、マーケの打ち手は特定のイベントで即死する
- `enabled_by`（→ event / channel / concept）— それ無しで成立しない前提
- `substitutes` — 置き換えの主張。「メールを Slack が殺した」型
- 後付けの括りへの所属は `grouped_as`（「◯◯マーケティング」という総称に括られる場合）
- **同時代の並行はエッジにしない**。時間×チャネルから生成する（手で張ると漏れと選別の恣意が入る）

逆向きの関係は書かない（ビルドが両方向に展開する）。

### `authority`

同一性のハブとして Wikidata QID を持つ（channel・player・確立した concept は大抵ある）。
**分類・数字の典拠には使わない。** 無いときは `none_reason` に「何を検索して無かったか」を書く
（トレンド現象そのものは無いことが多い。それでよい）。

## case / player / event をいつ作るか

**網羅しない。証拠として入れる。** 事例とプレイヤーを全部入れれば名簿になり、名簿は業界メディアが
既に持っている。ここが作るべきなのは「この主張はこの事例・この数字で裏が取れる」という接続の方。

`case` / `player` は、次のどれかに当たるときだけファイルを作る。

1. その trend / practice の **kind / time / stage の根拠になる**（evidence の source として使う）
2. **2つ以上の trend / practice を繋ぐ**（伝播・転用・複数トレンドの交点）
3. **事例として実際に分解して読んだ**（`## どう成立しているか` を書いた）

どれにも当たらないものは、trend / practice の本文に名前を書いて終わりにする（孤児 stub を
量産しない）。`event` は**時間軸の釘**——規制施行・アルゴリズム変更・機能ローンチ・値上げ。
複数のエンティティを同じ日付に固定したいときだけ作る。

**深さは揃えない。** 利用者の判断に直接関係する trend を深く掘り、隣は名前だけ、が正しい状態。

## 本文の型

検証が trend の反証見出しの存在を確認する。他は規律として固定する。

- **trend**: `## 何が変わったか` → `## kind と stage の判定` → `## 時間` → `## チャネルと伝播` →
  `## 反証（これが偽なら何が観測されるか）` → `## 未着手`
- **practice**: `## 何をするか` → `## どのトレンドへの応答か` → `## 成立条件・失敗条件` →
  `## 飽和度の判定` → `## 利用上の注意` → `## 未着手`
- **case**: `## 事実` → `## 当事者自身の言葉` → `## どう成立しているか` → `## 数字` →
  `## 外部事例から得られる示唆`
- **channel**: `## 事実（運営・規模・課金）` → `## アルゴリズムと分配の変遷` → `## このKBでの位置`
- **concept**: `## 定義の変遷` → `## 実装例` → `## 使える手`
- **source**: `## 所在` → `## 誰が出したか（利害）` → `## 数字の取り方`

**`## 反証` はこのKBの心臓部。** トレンドの主張は「これから◯◯になる」という規範的な形を取りがちで、
反証条件の無い主張は外れたことにすら気づけない。「これが偽なら何が観測されるか」を最低1つ書く。
書けないなら、それはトレンドではなく感想であり、draft に上げる段階にない。

## 書くときの規律

- **出典URLを本文に置く。** 手元の知識だけで書いた行は書かない
- **ベンダー発の数字は vendor と明記し、断定に使わない**
- **公開された外部観測を最優先する。** 書き手自身の実施有無や自社数値はこのKBに記録しない
- **外部資料で効果が確認できない施策は「効果未確認」と明記する**
- **確定できないことは `**未確認**:` として残す。** 空欄で隠さない
- **「バズっている」を出典にしない。** 投稿URLは anecdotal の evidence にはなるが、
  規模の主張には計測か統計が要る
- **本文は主題のことだけを書く。** KB の設計・運用・進捗を本文に混ぜない。`status` は
  frontmatter が持つ。判断の根拠は主題の事実として書く

## 道具

```bash
python3 tools/new_entity.py trend <slug> --ja "<名前>" --stage growing   # 雛形（期限も埋まる）
python3 tools/build_graph.py --check     # 検証のみ（CI 用）
python3 tools/build_graph.py             # 検証 + graph.json + coverage.json + 被覆マップ更新
python3 tools/audit.py                   # 噛み合っていないか → 次に調べること
python3 tools/audit.py --dry-run --now 2027-01-01   # 生きた時計で鮮度を見る
python3 tools/bundle.py trend/<slug>     # 知識のまとまりを1文書で取り出す
python3 tools/bundle.py --search <語>    # 語で探す（IDを知らなくていい）
python3 tools/linkcheck.py               # 出典URLの死活（ネットワークに出るので別枠）
```

検証が落とすもの: 必須項目の欠落／雛形の TODO 残り／ID・URI とパスの不一致／ID 重複／
存在しない参照／語彙外の型・関係・役割・確度／**関係とチャネルが指す相手の型違反**／EDTF 違反／
解釈系の関係の `certainty`・`source` 欠落／**verified なのに根拠が vendor・anecdotal だけ**／
evidence の `as_of` 欠落／trend の `market`・`geo`・`stage`・`kind`・`naming`・`freshness` 欠落／
**`recheck_by` が stage の導出期限より遅い**／**trend 本文に反証見出しが無い**／predictions の
形式違反／本文の相対リンク切れ／俯瞰の STALE／alias と id の衝突。

### 件数の数え方

- **`stub` は実績に数えない。** 受け入れ条件の件数は `draft` と `verified` だけを数える。
- **鮮度・予測の判定に時計を使わない。** 生成物の「いま」はデータの最新日（`updated` の最大値）。
  理由と運用は [freshness.md](freshness.md)。

### `aliases`（任意）

slug を変えたときは旧 id を `aliases: [trend/old-slug]` に残す。旧 id を指したままの
relations / channels は**ビルドが実IDに解決して**生成物（graph・派生エッジ・audit・bundle）に
載せるので、参照側の書き換えは急がなくてよい。検証は alias と既存 id の衝突、複数エンティティに
またがる alias の重複を落とし、`bundle.py` は alias でも引ける。
