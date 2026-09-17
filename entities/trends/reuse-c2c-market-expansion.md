---
id: trend/reuse-c2c-market-expansion
uri: urn:mtn:trend/reuse-c2c-market-expansion
type: trend
kind: demand-shift
stage: growing
market: retail-commerce
geo: japan
label_ja: リユース・CtoC市場の拡大
label_en: Expansion of reuse and C2C markets
authority:
  wikidata: null
  none_reason: "「リユース・CtoC市場の拡大」「reuse C2C market Japan」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: 2022年以降のCtoC-EC・リユース関連市場の拡大局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: リユース市場・CtoC-EC市場の拡大
  note: "「リユース・CtoC市場の拡大」は、環境省の調査報告書が整理するCtoC-ECとリユース市場の数字を要約するための記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2023", tense: completed}
  - {field: stage, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2023", tense: completed}
  - {field: time, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2022-2023", tense: completed}
  - {field: current-status, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2025-01", tense: intended}
predictions:
  - {claim: "次回公表されるCtoC-EC推計市場規模が2023年の2兆4,817億円を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "環境省の次回リユース市場規模調査で、「書籍」の中古品購入意向（今後新たに必要になったとき購入しても良いと考える割合）が令和6年度調査の63.5%を大きく下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    フリマアプリ、ネットオークション、リユースショップなどが取引接点になる。環境省は、CtoC-ECの推計にはフリマアプリとネットオークションが含まれると説明しているが、アプリ別のシェアや利用者属性まではこの資料からは言えない。
channels: []
relations: []
sources:
  - https://www.env.go.jp/recycle/circul/reuse/
  - https://www.env.go.jp/content/000327691.pdf
status: verified
updated: 2026-09-17
---

# リユース・CtoC市場の拡大

## 見出している未来（何に向かって動いているか）

生活者は、新たに何かが必要になったとき、新品ではなく中古品で購入してもよいという意向を、
品目によっては過半数が持っている。環境省「令和6年度リユース市場規模調査報告書」の消費者
アンケート（事前調査n=50,337人、2025年1月9日〜28日実施）は、22品目について「今後新たに
必要になったとき、中古品（新古品を除く）で購入しても良いと考えますか？」と尋ねている。
中古品の購入意向は「書籍」が63.5％と最も高く、次いで「ソフト・メディア類」53.4％、
「自動車」41.5％、「ゲーム機器」39.1％だった。

同じ報告書は、国内のリユース市場規模（消費財の販売額）が2023年の3兆1,227億円から、
2030年には4兆円に達すると見込んでいる。これは環境省の委託調査による推計であり、個々の
消費者の購入意向がそのまま市場規模の実現を保証するものではない。

## 足元の根拠（完了した事実）

中古品を個人間または事業者経由で再流通させる市場が、オンラインを含めて拡大している。
環境省の2024年度リユース市場規模調査報告書は、経済産業省の電子商取引市場調査などを整理し、2023年のCtoC-EC推定市場規模を2兆4,817億円、前年比5.0％増としている。また、同報告書が紹介する業界推計では、2023年のリユース市場規模は3兆1,227億円、2022年比7.8％増で、ネット販売は1兆9,313億円だった。

ただし、報告書はリユース市場全体や個人間取引を把握する公的統計が十分に存在しないこと、業態・推計方法によって捕捉範囲が異なることも明記している。したがって、これらを日本の中古品購買者全体の利用率とはみなさない。

## kind と stage の判定

**kind: demand-shift とした。** 観測しているのは、再使用品・個人間取引・ネット販売の市場規模の変化であり、特定の事業者の施策ではない。

**stage: growing とした。** CtoC-EC推定市場規模と、報告書が紹介するリユース市場推計が直近比較で増えている。ただし、前者は市場全体、後者は業界推計を含むため、同じ系列として接続しない。

## 時間

報告書で比較可能な2022年から `2022~` とした。終点は `..`（継続中）。

## チャネルと伝播

フリマアプリ、ネットオークション、リユースショップなどが取引接点になる。環境省は、CtoC-ECの推計にはフリマアプリとネットオークションが含まれると説明しているが、アプリ別のシェアや利用者属性まではこの資料からは言えない。

## 反証（これが偽なら何が観測されるか）

- 次回の同じ定義によるCtoC-EC推計が2兆4,817億円を下回る
- ネット販売・店頭販売の複数推計で市場規模が減少する
- 増加が推計方法や対象範囲の変更だけで、取引金額の実質的な増加ではないと判明する

## 未着手

- 2026年9月17日、環境省「令和6年度リユース市場規模調査報告書」の消費者アンケート部分を実読して見出している未来を追記した。22品目全ての購入意向データのうち、本文で確認できたのは上位4品目のみで、残り18品目は未確認
- 次回の環境省報告書で同じ定義のCtoC-EC推計を確認する
- 中古品のカテゴリ別、販売経路別、個人・事業者別の構成を同じ定義で比較する
- リユース需要に応答するpracticeの採用率と、価格・環境配慮・品質保証のどれが選択理由になるかを確認する
- 「書籍」等の中古品購入意向が、実際の購入経験率（同調査の本調査n=3,365人パート）にどう転換しているかを確認する
