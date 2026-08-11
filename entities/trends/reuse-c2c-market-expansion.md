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
  - {field: kind, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2023"}
  - {field: stage, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2023"}
  - {field: time, source: "https://www.env.go.jp/content/000327691.pdf", certainty: independent, retrieved: primary, as_of: "2022-2023"}
predictions:
  - {claim: "次回公表されるCtoC-EC推計市場規模が2023年の2兆4,817億円を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.env.go.jp/recycle/circul/reuse/
  - https://www.env.go.jp/content/000327691.pdf
status: verified
updated: 2026-08-11
---

# リユース・CtoC市場の拡大

## 何が変わったか

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

- 次回の環境省報告書で同じ定義のCtoC-EC推計を確認する
- 中古品のカテゴリ別、販売経路別、個人・事業者別の構成を同じ定義で比較する
- リユース需要に応答するpracticeの採用率と、価格・環境配慮・品質保証のどれが選択理由になるかを確認する
