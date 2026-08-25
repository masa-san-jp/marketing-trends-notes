---
id: trend/single-person-household-expansion
uri: urn:mtn:trend/single-person-household-expansion
type: trend
kind: demand-shift
stage: growing
market: consumer-goods
geo: japan
label_ja: 単独世帯の拡大
label_en: Expansion of single-person households
authority:
  wikidata: null
  none_reason: "「単独世帯の拡大」「single-person household expansion」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2005~"
  end: ".."
  display: 2005年から2020年にかけて単独世帯数と構成比が上昇した局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 単独世帯の増加
  note: "「単独世帯の拡大」は、国勢調査の家族類型別世帯数を要約するための記述的なラベル。世帯主がこの語を自称することは確認していない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2005-2020"}
  - {field: stage, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2020"}
  - {field: time, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2005-2020"}
predictions:
  - {claim: "2025年国勢調査の家族類型別集計でも単独世帯の構成比が2020年の38.1%を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定チャネルから発生した変化ではない。家族形成、人口構成、居住形態などの社会構造が、食品、日用品、住居、金融、外食などの需要単位に影響しうる。ただし、カテゴリ別の影響は別の統計で確認する必要がある。
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf
status: verified
updated: 2026-08-11
---

# 単独世帯の拡大

## 何が変わったか

日本の一般世帯に占める単独世帯の数と比率が上昇している。
総務省統計局の2020年国勢調査では、単独世帯は2,115万1,042世帯で、一般世帯の38.1％を占めた。2015年と比べて単独世帯数は14.8％増え、構成比も34.6％から38.1％へ上昇している。2005年から2020年の系列でも、単独世帯の構成比は29.5％、32.4％、34.6％、38.1％と上昇している。

これは世帯単位で商品・サービスの需要を考えるときに、家族世帯の平均だけでは捉えにくい生活単位が増えていることを示す。ただし、単独世帯が増えたことだけから、特定の商品カテゴリや購買チャネルの伸長までは言えない。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は世帯構成という需要側の基盤変化であり、広告施策や制度の導入ではない。

**stage: growing とした。** 2005年から2020年に単独世帯の実数と構成比が連続して増加している。2025年国勢調査の詳細な家族類型別集計がまだ揃っていないため、直近の伸び率は未確認として残す。

## 時間

国勢調査で同じ家族類型の系列を比較できる2005年から `2005~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定チャネルから発生した変化ではない。家族形成、人口構成、居住形態などの社会構造が、食品、日用品、住居、金融、外食などの需要単位に影響しうる。ただし、カテゴリ別の影響は別の統計で確認する必要がある。

## 反証（これが偽なら何が観測されるか）

- 2025年国勢調査の家族類型別集計で単独世帯の構成比が38.1％を下回る
- 単独世帯の実数・構成比が次回以降の公的統計で減少する
- 単独世帯の増加が統計上の分類変更による見かけだけだと判明する

## 未着手

- 2025年国勢調査の家族類型別詳細集計で予測を答え合わせする
- 単独世帯の年齢・性別・地域構成と、カテゴリ別支出の違いを接続する
- 単独世帯の増加が購買頻度、容量、配送、外食、サブスクリプションにどう影響したかを独立統計で分解する
