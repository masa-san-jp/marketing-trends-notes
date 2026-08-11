---
id: trend/outbound-travel-recovery
uri: urn:mtn:trend/outbound-travel-recovery
type: trend
kind: demand-shift
stage: growing
market: cross-category
geo: japan
label_ja: 海外旅行需要の回復
label_en: Recovery of outbound travel demand
authority:
  wikidata: null
  none_reason: "「海外旅行需要の回復」「outbound travel recovery」で検索したが、この日本人海外旅行需要の回復現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "コロナ禍後に日本人の海外旅行者数が回復している局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 日本人海外旅行者数の回復
  note: "「海外旅行需要の回復」は、観光庁が公表する日本人出国者数の推移を要約するための記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/kankocho/page01_00056.html", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: stage, source: "https://www.mlit.go.jp/policy/shingikai/content/001986335.pdf", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: time, source: "https://www.mlit.go.jp/policy/shingikai/content/001986335.pdf", certainty: independent, retrieved: primary, as_of: "2019-2025"}
predictions:
  - {claim: "2026年の日本人海外旅行者数が2025年の1,473万人を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/kankocho/page01_00056.html
  - https://www.mlit.go.jp/policy/shingikai/content/001986335.pdf
status: verified
updated: 2026-08-11
---

# 海外旅行需要の回復

## 何が変わったか

日本人の海外旅行者数が、コロナ禍による落ち込みから回復している。観光庁の資料では、出国日本人数は2019年の2,008万人から2023年962万人、2024年1,301万人、2025年1,473万人へ増えた。

2025年は2019年の約7割まで戻ったが、まだ同水準には達していない。したがって、ここでいう回復は完全な復元ではなく、旅行・航空、宿泊、免税小売、決済、通信など複数の接点にまたがる回復局面である。円安、旅行費用、国際情勢、休暇取得などの制約も残っている。

## kind と stage の判定

**kind: demand-shift とした。** 観光庁が測っているのは広告供給ではなく、日本人の出国者数という旅行需要の結果である。

**stage: growing とした。** 2023年から2025年まで連続して増えた一方、2019年水準には未回復で、回復を妨げる要因も資料に残るため、peakや完全な回復とは判定しない。

## 時間

2019年を比較基準に、コロナ禍後の回復が数値で連続して確認できる `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定の広告媒体が発生チャネルだとは置かない。航空便、渡航費、為替、休暇、訪問先の安全認識、旅行会社・予約サービスなどの複合要因が出国者数に反映される。

## 反証（これが偽なら何が観測されるか）

- 次回以降の公的統計で出国日本人数が複数年連続して減少する
- 旅行者数が増えても、主要な方面への航空便・宿泊・旅行支出が同時に縮小し、回復が統計上の一時的な反発にとどまる
- 2026年以降も2019年比で回復率が改善せず、制約要因が需要を長期に抑え続ける

## 未着手

- 方面別、年齢別、旅行目的別に回復速度を分解する
- 出国者数と旅行消費額、航空座席供給、平均旅行費用を同じ期間で比較する
- 2026年の公的統計で予測を答え合わせする
