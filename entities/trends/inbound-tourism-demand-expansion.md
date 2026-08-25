---
id: trend/inbound-tourism-demand-expansion
uri: urn:mtn:trend/inbound-tourism-demand-expansion
type: trend
kind: demand-shift
stage: growing
market: cross-category
geo: japan
label_ja: 訪日観光需要の拡大
label_en: Expansion of inbound tourism demand
authority:
  wikidata: null
  none_reason: "「訪日観光需要の拡大」「inbound tourism demand expansion」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2019~"
  end: ".."
  display: 2019年を基準に回復・拡大が進み、2025年に過去最高を更新した局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 訪日外国人旅行者数・訪日旅行消費額の増加
  note: "「訪日観光需要の拡大」は、観光庁の旅行者数と旅行消費額を要約するための記述的なラベル。訪日客がこの語を自称することは確認していない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/kankocho/page01_00056.html", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: stage, source: "https://www.mlit.go.jp/kankocho/page01_00056.html", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: time, source: "https://www.mlit.go.jp/kankocho/tokei_hakusyo/shutsunyukokushasu.html", certainty: independent, retrieved: primary, as_of: "2025"}
predictions:
  - {claim: "2026年の訪日外国人旅行者数が2025年の4,268万人を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定の広告媒体が発生チャネルだとは置かない。航空便、国・地域別の旅行需要、滞在日数、観光コンテンツ、地方誘客などが複合して旅行者数と消費額に反映される。観光庁は欧米豪・中東などからの旅行者増加や平均泊数の増加を要因として挙げている。
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/kankocho/page01_00056.html
  - https://www.mlit.go.jp/kankocho/tokei_hakusyo/shutsunyukokushasu.html
status: verified
updated: 2026-08-11
---

# 訪日観光需要の拡大

## 何が変わったか

訪日外国人の人数と旅行消費額が、コロナ禍前の水準を回復した後も拡大している。
観光庁によると、2025年の訪日外国人旅行者数は約4,268万人で、初めて4,000万人を超え、過去最高となった。
同年の訪日外国人旅行消費額も約9.5兆円で、2019年の約4.8兆円からおよそ2倍になったと説明されている。

これは観光関連だけでなく、宿泊、飲食、小売、交通、娯楽など複数の接点にまたがる需要の変化である。
ただし、国・地域別には増減があり、2025年12月は中国からの訪日客が前年同月比で減少したとされるため、訪日需要を一様な増加とみなしてはいけない。

## kind と stage の判定

**kind: demand-shift とした。** 観光庁が測っているのは、広告施策の供給量ではなく、訪日旅行者数と旅行消費額という需要側の変化である。

**stage: growing とした。** 2025年に旅行者数と旅行消費額が過去最高となり、観光庁もインバウンド全体を成長軌道と説明している。ただし、地域集中、オーバーツーリズム、人手不足など供給制約があり、すべての地域・事業者が同じ成長を享受しているとは言えない。

## 時間

2019年の水準を比較基準に置き、コロナ禍による落ち込みからの回復を含む `2019~` とした。2025年に過去最高を更新しており、終点は `..`（継続中）。

## チャネルと伝播

特定の広告媒体が発生チャネルだとは置かない。航空便、国・地域別の旅行需要、滞在日数、観光コンテンツ、地方誘客などが複合して旅行者数と消費額に反映される。観光庁は欧米豪・中東などからの旅行者増加や平均泊数の増加を要因として挙げている。

## 反証（これが偽なら何が観測されるか）

- 次回以降の公的統計で訪日外国人旅行者数と旅行消費額が複数年連続で減少する
- 旅行者数は増えても、訪日旅行消費額や平均泊数が同時に縮小し、需要拡大が一部の入国数だけに限られる
- 中国以外の地域を含む複数の主要市場で、航空便・予約・宿泊などの回復が止まる

## 未着手

- 国・地域別、目的別、訪問地別の消費構成を同じ定義で時系列比較する
- 訪日需要の増加が小売・飲食・宿泊の各業態にどの程度波及したかを独立統計で分解する
- 2026年の公的統計で予測を答え合わせする
