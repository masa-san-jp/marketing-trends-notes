---
id: trend/women-employment-expansion
uri: urn:mtn:trend/women-employment-expansion
type: trend
kind: demand-shift
stage: growing
market: cross-category
geo: japan
label_ja: 女性就業の拡大
label_en: Expansion of women’s employment
authority:
  wikidata: null
  none_reason: "「女性就業の拡大」「women employment expansion Japan」で検索したが、日本の女性就業者数・就業率の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "女性就業者数と女性就業率が上昇し、働き方・購買・サービス利用の前提が変化する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 女性就業者数・就業率の上昇
  note: "「女性就業の拡大」は、総務省統計局の労働力調査を要約する記述的なラベルで、就業者の消費行動を一様に推定するものではない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.stat.go.jp/data/roudou/sokuhou/nen/ft/pdf/youyaku.pdf", certainty: independent, retrieved: primary, as_of: "2025年平均"}
  - {field: stage, source: "https://www.stat.go.jp/data/roudou/sokuhou/nen/ft/pdf/youyaku.pdf", certainty: independent, retrieved: primary, as_of: "2020-2025年平均"}
  - {field: time, source: "https://www.stat.go.jp/data/roudou/sokuhou/nen/ft/pdf/youyaku.pdf", certainty: independent, retrieved: primary, as_of: "2020-2025年平均"}
predictions:
  - {claim: "2026年平均の女性就業者数が2025年の3,126万人を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/roudou/
  - https://www.stat.go.jp/data/roudou/sokuhou/nen/ft/pdf/youyaku.pdf
status: verified
updated: 2026-08-11
---

# 女性就業の拡大

## 何が変わったか

女性の就業者数と就業率が上昇し、働く人の時間、所得、家庭内役割、通勤、購買、サービス利用の前提が変わっている。総務省統計局の2025年平均労働力調査では、女性就業者数は3,126万人で前年比44万人増、15歳以上女性の就業率は55.1％で0.9ポイント上昇した。就業者数は全体でも5年連続で増加している。

就業者数の増加だけから所得増、管理職比率、家事負担の軽減、特定商品の需要を断定しない。雇用形態、産業、年齢、世帯、子育て、労働時間、賃金の内訳を分ける必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は就業という生活・経済行動の変化であり、特定企業の採用広告や制度利用だけではない。

**stage: growing とした。** 2025年平均でも女性就業者数・就業率が前年より上昇し、長期にも増加局面が確認できるためである。ただし、職種・雇用形態・所得・家事負担の差が残るため、就業者が一様に同じ購買力を持つとは判定しない。

## 時間

2020年代の就業者数・就業率の上昇を同じ調査系列で追うため `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

雇用、通勤、保育・介護、勤務時間、在宅勤務、家事・外食、金融、教育、住宅、購買など生活の複数接点へ伝わる。女性就業と特定市場の需要の因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回以降の労働力調査で女性就業者数・就業率が複数年連続で低下する
- 増加が人口構成や短時間就業だけで、労働時間・賃金・継続就業が同じ方向に動いていないと分かる
- 産業・年齢・雇用形態を分けると、女性就業の増加が一部層だけで全国的な前提変化ではないと判明する

## 未着手

- 産業、年齢、雇用形態、労働時間、賃金、世帯、子育て・介護を分解する
- 女性就業の変化と外食、保育、金融、住宅、EC、学習サービスの利用を接続する
- 2026年平均の労働力調査で予測を答え合わせする
