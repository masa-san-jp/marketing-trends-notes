---
id: trend/food-ecommerce-expansion
uri: urn:mtn:trend/food-ecommerce-expansion
type: trend
kind: demand-shift
stage: growing
market: food-beverage
geo: japan
label_ja: 食品・飲料・酒類ECの拡大
label_en: Expansion of food, beverage, and alcohol e-commerce
authority:
  wikidata: null
  none_reason: "「食品・飲料・酒類ECの拡大」「food e-commerce Japan market」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2023~"
  end: ".."
  display: 2022年以降の食品・飲料・酒類BtoC-EC市場規模の拡大局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 食品、飲料、酒類のBtoC-EC市場拡大
  note: "「食品・飲料・酒類ECの拡大」は、経済産業省の分野別市場規模を要約するための記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2024"}
  - {field: stage, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2023-2024"}
  - {field: time, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2023-2024"}
predictions:
  - {claim: "2025年の食品・飲料・酒類BtoC-EC市場規模が2024年の3兆1,163億円を下回らない", by: "2026-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    ECモール、食品宅配、メーカー直販、オンラインスーパーなど複数の取引接点が含まれうるが、資料は個別チャネル別の寄与を示していない。チャネル別の成長要因は別調査で確認する。
channels: []
relations: []
sources:
  - https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf
status: verified
updated: 2026-08-11
---

# 食品・飲料・酒類ECの拡大

## 何が変わったか

食品、飲料、酒類の消費者向け電子商取引の市場規模が拡大している。
経済産業省の令和6年度電子商取引市場調査では、2024年の同分野のBtoC-EC市場規模は3兆1,163億円で、2023年の2兆9,299億円から前年比6.36％増となった。EC化率は4.52％で、2023年の4.29％から上昇している。

市場規模は食品・飲料・酒類の全消費額ではなく、同調査のBtoC-ECの定義に基づく。したがって、実店舗からECへ移った購買の割合や、食品全体のオンライン購入者率をこの数字だけから断定しない。

## kind と stage の判定

**kind: demand-shift とした。** 変化しているのは、食品・飲料・酒類の消費者向け取引における電子取引の規模と比率であり、特定事業者の広告施策ではない。

**stage: growing とした。** 2023年から2024年に市場規模が6.36％増え、EC化率も上昇した。食品・飲料・酒類の全購買がECへ移行したという意味ではなく、対象市場の中で電子取引の比重が増えた局面として記録する。

## 時間

分野別の同一定義の比較値を確認できる2023年から `2023~` とした。国内EC全体の2022年値を食品・飲料・酒類の分野別値に流用してはいない。終点は `..`（継続中）。

## チャネルと伝播

ECモール、食品宅配、メーカー直販、オンラインスーパーなど複数の取引接点が含まれうるが、資料は個別チャネル別の寄与を示していない。チャネル別の成長要因は別調査で確認する。

## 反証（これが偽なら何が観測されるか）

- 次回の同じ定義の市場調査で食品・飲料・酒類のEC市場規模が3兆1,163億円を下回る
- 市場規模が増えてもEC化率が低下し、分母の変化だけで拡大していたと判明する
- 食品・飲料・酒類の分野定義や調査方法が変わり、2023年と2024年の比較が成立しないと判明する

## 未着手

- 2025年公表値で予測を答え合わせする
- 食品、飲料、酒類を分けた市場規模とEC化率を確認する
- 食品ECの利用者属性、購買頻度、配送・店舗受取などの行動変化を独立調査で補う
