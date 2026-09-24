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
  - {field: kind, source: "https://www.mlit.go.jp/kankocho/page01_00056.html", certainty: independent, retrieved: primary, as_of: "2025", tense: completed}
  - {field: stage, source: "https://www.mlit.go.jp/policy/shingikai/content/001986335.pdf", certainty: independent, retrieved: primary, as_of: "2025", tense: completed}
  - {field: time, source: "https://www.mlit.go.jp/policy/shingikai/content/001986335.pdf", certainty: independent, retrieved: primary, as_of: "2019-2025", tense: completed}
  - {field: current-status, source: "https://www.mlit.go.jp/kankocho/news02_00077.html", certainty: attested, retrieved: primary, as_of: "2026-03-27", tense: intended}
predictions:
  - {claim: "2026年の日本人海外旅行者数が2025年の1,473万人を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "第5次観光立国推進基本計画の計画期間（2026〜2030年度）で、パスポート手数料の引下げ等の施策を受けて日本人海外旅行者数が2025年の1,473万人を上回る方向で推移する", by: "2028-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定の広告媒体が発生チャネルだとは置かない。航空便、渡航費、為替、休暇、訪問先の安全認識、旅行会社・予約サービスなどの複合要因が出国者数に反映される。
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/kankocho/page01_00056.html
  - https://www.mlit.go.jp/policy/shingikai/content/001986335.pdf
  - https://www.mlit.go.jp/kankocho/news02_00077.html
status: verified
updated: 2026-09-21
---

# 海外旅行需要の回復

## 見出している未来（何に向かって動いているか）

国は、パスポート手数料の引下げなどを通じて、日本人の海外旅行（アウトバウンド）需要をさらに拡大
させることを2026年度からの政策方針としている。2026年3月27日に閣議決定された「観光立国推進基本
計画」（第5次、計画期間2026〜2030年度）は、施策の柱の一つとして「国内交流・アウトバウンド拡大
（休暇の分散・旅行需要の平準化などによる国内交流拡大、パスポート手数料の引下げなどによるアウト
バウンド拡大 等）」を掲げている。

これは国土交通省・観光庁が示した政策方針であり（`attested`）、旅行者自身が「今後どこまで海外旅行を
したいか」に答えた意向調査ではない。既存の足元の根拠にある2025年の出国日本人数1,473万人は
2019年の約7割にとどまっており、この施策がどの程度回復を加速させるかはこの記録では確認できていない。

## 足元の根拠（完了した事実）

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

- 2026年9月21日、観光庁「観光立国推進基本計画」（第5次、2026年3月27日閣議決定）の報道発表を実読し、パスポート手数料引下げ等のアウトバウンド拡大施策を見出している未来として追記した
- 方面別、年齢別、旅行目的別に回復速度を分解する
- 出国者数と旅行消費額、航空座席供給、平均旅行費用を同じ期間で比較する
- 2026年の公的統計で予測を答え合わせする
