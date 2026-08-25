# 1件の調査のやり方（この手順だけで1件が終わる）

**この手順書は Sonnet が単独で1件を完了できる粒度で書いてある。** 設計の判断は済んでいるので、
調査する側は判断しない。判定に迷ったら手順内の判定表を引き、表で決まらなければ「未確認」と書いて
次へ進む。**空欄を推測で埋めない。**

対象は原則 **trend 1件 または practice 1件**。1件＝1タスク。

---

## 手順

### 1. 重複を確かめる

```bash
ls entities/trends/ entities/practices/ | grep -i <slug の一部>
grep -ril "<日本語名>" entities/
python3 tools/bundle.py --search "<日本語名>"
```

既にあれば、新規作成ではなく**そのファイルを埋める**（または鮮度を更新する）タスクに変える。

### 2. trend か practice かを決めてから、雛形を作る

判定は1行: **需要側で観測される変化なら trend、供給側の打ち手の型なら practice。**
迷ったら「マーケターが全員消えても起きているか」——起きるなら trend。

```bash
python3 tools/new_entity.py trend <slug> --ja "<日本語名>" --stage growing
python3 tools/new_entity.py practice <slug> --ja "<日本語名>"
```

`slug` は英語のケバブケース（例 `short-video-mainstream`、`retail-media`）。**一度決めた slug は
変えない**（ID になる）。`--stage` を渡すと `freshness.recheck_by` が正しく埋まる。

### 3. 出典を取る（最初にこれをやる）

**[sources-directory.md](sources-directory.md) の層の順に当たる。** 上の層で取れたら下は補助に回す。

1. **官公庁統計・公的調査**（`independent`）— 総務省・経産省・e-Stat
2. **決算・IR・規約・仕様**（`attested`）— 当事者の一次言明。数字の主張ではなく事実の言明
3. **業界団体・学術**（`independent`）
4. **プラットフォーム・ベンダーの公式発表**（`vendor`）— 使ってよいが、必ず vendor と明記する
5. **個別の投稿・記事・事例**（`anecdotal`）

**Wikidata QID は同一性のハブとしてだけ使う**（channel・player・確立した concept には大抵ある。
トレンド現象そのものには無いことが多い）。分類・数字の典拠にはしない。

```bash
curl -s -H "User-Agent: marketing-trends-notes/0.1" \
  "https://www.wikidata.org/w/api.php?action=wbsearchentities&search=<名前>&language=ja&format=json&limit=5" \
  | python3 -c "import json,sys;[print(d['id'],d.get('label'),'|',d.get('description')) for d in json.load(sys.stdin)['search']]"
```

**1つも見つからないとき**: `authority.none_reason` に「何を検索して見つからなかったか」を書く。
それでよい。空にしたまま進めると検証で落ちる。

**出典を読むときに必ず確かめる3点**（マーケの出典はここで嘘をつく）:

- **誰が出したか。その記述で誰が得をするか** — 得をする側なら `vendor`
- **いつ時点の数字か** — evidence の `as_of` に入れる。発表日ではなく調査時点
- **n と取り方** — n=200 のアンケートと官公庁の全数調査を同じ重さで扱わない。怪しければ本文に書く

### 4. frontmatter を埋める

| 項目 | 埋め方 |
|---|---|
| `kind` | 下の判定表で1つ選ぶ。**迷ったら本文にその迷いを書いてから選ぶ** |
| `stage` | 下の判定表で1つ選ぶ |
| `market` / `geo` | `config/markets.yaml` のバケットから1つずつ。カテゴリを選ばない変化は `cross-category` |
| `naming.self_identified` | 当事者（消費者・実践者）がその名を使うか。`true` / `false` |
| `naming.named_by` / `named_when` | 名付けたのは誰か・いつか。不明なら `null` にして `note` に経緯 |
| `freshness.valid_as_of` | 実データを確認した今日の日付 |
| `freshness.recheck_by` | `new_entity.py --stage` が埋めた値のまま。stage を変えたら検証が再計算を要求する |
| `time.start` / `end` | EDTF。`2021` / `202X`（2020年代）/ `2020~`（およそ）/ `..`（継続中）/ `null`（不明） |
| `time.display` | 原表記（「コロナ禍以降」等）をそのまま |
| `channels` | `originated_on`（発生チャネル）を最優先で特定。特定できないなら**書かない** |
| `evidence` | `verified` を名乗るときだけ必須。`{field, source, certainty, retrieved, as_of}`。**`retrieved` は書くなら全行必須** |
| `status` | `stub`（枠だけ）/ `draft`（書いたが根拠が薄い）/ `verified`（利害のない根拠で裏が取れた） |

#### kind の判定表（上から順に当てる。最初に当たったものを採る）

| 順 | 問い | yes なら |
|---|---|---|
| 1 | 規制・制度の施行日・条文を指せるか | `regulation-driven` |
| 2 | 特定の技術・機能のローンチが先行し、それ無しで成立しないか | `tech-enabled` |
| 3 | 名付けた者がその概念で儲かる側（ベンダー・コンサル・媒体）で、需要側の独立した数字がまだ無いか | `vendor-pushed` |
| 4 | 需要側の数字（利用率・支出・行動）が独立した出典で動いているか | `demand-shift` |

どれにも yes と言えない＝数字が取れていない。`kind` は最も疑わしいものを選び、本文の
`## kind と stage の判定` に迷いを書く。**Wikidata や媒体の分類に引っ張られない**——実体で決める。

#### stage の判定表

| stage | 目安 |
|---|---|
| `emerging` | 数字はまだ小さいか無い。観測は特定チャネル・特定クラスタに限られる |
| `growing` | 独立した出典で数字が伸びている。一般紙・地上波にはまだ薄い |
| `peak` | 主流化した。一般紙・地上波が説明なしで使う。数字は高原状態 |
| `declining` | 数字が落ちている（出典を `evidence` に）。「もう古い」記事が出る |
| `dead` | 終わった。**何が殺したかを `killed_by` で指す**（audit が要求する） |

#### certainty の判定表（evidence と解釈系の関係に使う）

| 問い | certainty |
|---|---|
| 公開された再現可能な外部観測か | `measured` |
| 利害のない第三者か（官公庁・学術・業界団体） | `independent` |
| 当事者の一次言明か（仕様・規約・決算。**自分に不利でも成り立つ事実**） | `attested` |
| その記述で発行者が得をするか（ベンダーレポート・代理店調査・プラットフォームの効果自慢） | `vendor` |
| 個別の事例・証言・投稿か | `anecdotal` |
| 自分の見立てか | `hypothesis` |

**発行元ではなく「その記述で誰が得をするか」で判定する。** 同じ Apple でも、ATT の仕様説明は
`attested`、自社広告の効果主張は `vendor`。

#### retrieved の判定表（certainty と独立に、全 evidence 行で決める）

| 問い | retrieved |
|---|---|
| その数字を、原典のファイル（PDF・統計表・規約・決算）の中で自分の目で見たか | `primary` |
| 検索結果の要約・二次記事・他者のまとめ・記憶から書いたか | `summary` |

**迷ったら `summary`。** 「たぶんそのページに書いてある」は読んだことにならない。原典を開いたが
目的の数字が見つからなかった場合も `summary`（読めたのは別の部分）。

`independent` と `primary` は別物。官公庁統計のURLを検索結果から拾って貼れば
`certainty: independent` かつ `retrieved: summary` になる。**利害のない出典であることと、
自分が読んだことは独立している。**

原典を開くための実務（この環境で通る手順）:

```bash
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
curl -s -L --max-time 30 -A "$UA" "<PDFのURL>" -o /tmp/src.pdf && pdftotext -layout /tmp/src.pdf /tmp/src.txt
grep -n "<探す語>" /tmp/src.txt
```

- **素の curl で 400 / 403 が返ってもサイトが死んでいるとは限らない**（bot フィルタ）。上記のように
  ブラウザ UA を付けて1回試す（`meti.go.jp` は素の curl で403・UA 付きで200）
- 官公庁の HTML は **cp932** のことがある。UTF-8 で decode に失敗したら cp932 → euc-jp の順に試す
- **PDF のグラフ部分は `pdftotext -layout` でも列と数値の対応が崩れる。** 崩れた表から数字を読み取って
  書かない。読めた断面だけを採り、残りは「未確認」として `## 未着手` に送る

#### 関係語彙（この中から選ぶ）

構造的（出典なしで書ける）: `practiced_by` `example_of` `part_of` `precedes` `targets`
`documented_in` `operated_by`

解釈を含む（`certainty` と `source` が必須）: `responds_to` `enabled_by` `killed_by`
`derives_from` `substitutes` `reacts_against` `grouped_as` `diffused_to` `influenced_by`

- **practice を書いたら `responds_to` でどの trend への応答かを必ず張る**（張れない practice は
  「なぜやるのか」が無い。それでも置くなら本文に理由を書く）
- 総称（「◯◯マーケティング」）への所属は `grouped_as`
- **同時代の並行関係は書かない。** 時間とチャネルから機械が出す

### 5. 本文を書く

見出しは固定（`docs/schema.md` の「本文の型」）。trend は:

`## 何が変わったか` → `## kind と stage の判定` → `## 時間` → `## チャネルと伝播` →
`## 反証（これが偽なら何が観測されるか）` → `## 未着手`

- **出典URLを本文に置く。** 手元の知識だけで書いた行は書かない
- **`## 反証` は必須**（検証が見出しの存在を落とす）。「これが本物のトレンドでないなら、
  ◯◯の数字が△△になっているはずだ」という**観測可能な**条件を最低1つ。書けないなら
  status を stub に留めて理由を `## 未着手` に書く
- 確定できないことは **`**未確認**:` で始める行**にして残す。空欄で隠さない
- ベンダー由来の数字を本文で使うときは「（ベンダー調べ）」を添える
- **本文は主題のことだけを書く。KB の内部事情を混ぜない。** 「このKBで最初の1件」「stub として
  置いた」等は書かない。判断の根拠は主題の事実として書く（✗「vendor-pushed が必要だったので」→
  ○「命名者は◯◯を販売する□□社で、需要側の独立した数字は2026-08時点で見つからない」）

### 6. 検証を通す

```bash
python3 tools/build_graph.py --check     # 落ちたらメッセージのとおりに直す
python3 tools/build_graph.py             # 通ったらグラフと被覆マップを更新
```

落ちる主な理由: TODO が残っている／典拠ゼロで `none_reason` が空／`kind`・`stage`・`market`・
`geo` 未設定／`recheck_by` が stage と食い違う／EDTF の形式違反／解釈系の関係に `certainty` か
`source` が無い／参照先のエンティティが存在しない／trend 本文に `## 反証` が無い／
evidence 行に `retrieved` が無い（`primary` か `summary`）／`verified` なのに
`retrieved: primary` の根拠が1本も無い。

**`retrieved: yes` と書くと YAML が真偽値として読むので語彙外で落ちる。** `primary` / `summary` の
どちらかをそのまま書く。

**YAML で必ず踏む罠**: `note:` や `display:` の説明文に**半角コロン＋スペース**（`: `）が入ると、
YAML がそこを新しい項目の区切りだと解釈して落ちる。長い説明を書くときは値全体を `"` で囲む。
全角コロン（`：`）に替えるのでもよい。

**`git checkout` / `git restore` / `git stash` を使わない。** 生成物を元に戻したくなっても使わない
——他のエージェントの**未コミットの編集を消す**。生成物がおかしくなったら、**そのまま報告して止まる**。

**自分のファイル以外の理由で落ちたとき**（他の調査が同時に走っていて、その未完成ファイルが検証に
引っかかる場合）は、**他のファイルを動かさない・直さない**。自分のファイルだけを完成させ、
「他の未完成ファイルのために全体の検証が通らない」と報告して終わる。

**参照先が無い**と言われたら、その参照先を先に作る（`new_entity.py` で `channel` や `event` を
stub で置く）。ただし**孤児 stub を量産しない**——今回の1件に必要なものだけ。

`case` / `player` を作ってよいのは次の3つのどれかに当たるときだけ（`docs/schema.md` が正本）:

1. その trend / practice の kind / time / stage の**根拠になる**
2. **2つ以上の trend / practice を繋ぐ**
3. **事例として実際に分解して読んだ**

どれにも当たらないものは、本文に名前を書いて終わりにする。名簿を作らない。

### 7. 取り出して読み返す

```bash
python3 tools/bundle.py trend/<slug>
```

1文書として読んで、周辺との繋がりが見えるか確かめる。関係が1本も無ければ、それは体系に
載っていない。trend なら「どの practice が応答するか」、practice なら「どの trend への応答か」が
見えるかを確かめる。

### 8. commit する

```bash
git add entities/ overviews/coverage.md data/ && git commit -m "<なぜこの1件を置いたか>"
```

コミットメッセージは「何をしたか」ではなく**なぜこれを置いたか**を書く。

---

## 鮮度の更新タスク（新規作成と並ぶ、もう1つの定型タスク）

audit が「鮮度切れ」を指した trend の再検証は、新規1件と同じく1タスク。手順:

1. `evidence` と本文の数字を、元の出典の**最新版**で引き直す（sources-directory.md）
2. 変わっていなければ `freshness.valid_as_of` を今日にし、`recheck_by` を stage から引き直す
3. 数字が動いていたら `stage` を判定表で引き直す。**stage を変えたら理由を本文に追記する**
4. `dead` にしたら `killed_by` を張る（何が殺したかを event で特定する）
5. `python3 tools/build_graph.py` → commit（メッセージに何が変わったか・変わらなかったかを書く）

## やらないこと

- 空欄を推測で埋める（`null` と「未確認」が正しい答え）
- 設計を変える（型を増やす・関係語彙を足す・閾値を動かす・stage の月数を変える）。
  必要だと思ったら issue #1 にコメントして止まる
- 1タスクで複数の trend / practice を仕上げる（1件ずつ。周辺の stub は例外）
- **ベンダーの数字を independent に格上げする**（発行者がその主張で儲かるなら vendor）
- **「バズっている」を規模の出典にする**（投稿URLは anecdotal の evidence にはなる）
- レポートPDF・記事全文を repo に置く（リンクと引用で参照する）
- `data/`・`overviews/coverage.md` の生成ブロックを手で編集する

## 次に何を調べるか

`overviews/coverage.md` を見る。4つの材料が並んでいる。

1. **鮮度切れ**（audit の出力）— このKBで最優先。腐った記述は無いより悪い
2. **体系の食い違い**（audit の出力）— vendor 単独根拠／未判定の予測／応答なきトレンド／
   単一チャネル観測。体系が次に要求していること
3. **探されたが無かった語** — 他の人格が探して空振りした記録（需要のシグナル）
4. **被覆マップの空欄**

迷ったら 1 → 2 → 3 → 4 の順で選ぶ。**計が `0（調査済 n）` のカテゴリは 4 から外す**——
そこは既に調べて無かったところなので、ただの空欄より後回しでよい。

## 調べたが、載せるものが無かったとき

そのカテゴリを調べて、trend として置けるものが無いという結論に達したら、**手ぶらで終わらせずに記録する。**

```bash
python3 tools/record_searched.py --market <カテゴリ> --geo <地理> \
    --scope "何を、どの範囲で探したか" --source <当たった出典URL> --source <URL>
```

この1行が、被覆マップの空欄を「未着手」から「調査済み」に変える。**次に調べる人が同じ空振りを
繰り返さないための記録**なので、`scope` には検索語ではなく**探した範囲**を書く
（✗「ゲーム トレンド」→ ○「2024年以降の国内ゲーム市場で、需要側の変化を示す独立した統計」）。

- **「見つからなかった」と「探していない」を混ぜない。** 出典に1本も当たっていないなら、それは
  調査ではないので記録しない（`--source` 0本でも記録はできるが、その旨が被覆マップに太字で出る）
- trend が1件でも置けたなら、この記録は要らない（空欄ではなくなる）
