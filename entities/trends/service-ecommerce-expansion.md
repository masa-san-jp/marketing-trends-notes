---
id: trend/service-ecommerce-expansion
uri: urn:mtn:trend/service-ecommerce-expansion
type: trend
kind: demand-shift
stage: growing
market: retail-commerce
geo: japan
label_ja: サービスECの拡大
label_en: Expansion of service e-commerce
authority:
  wikidata: null
  none_reason: "「サービスECの拡大」「service e-commerce expansion Japan」で検索したが、調査上のサービス系BtoC-EC市場の拡大現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2023~"
  end: ".."
  display: "旅行・チケット等を含むサービス系BtoC-EC市場規模が増加する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: サービス系分野のBtoC-EC市場拡大
  note: "「サービスECの拡大」は、経済産業省のBtoC-EC分野別市場規模を要約する記述的なラベルで、すべてのサービス需要を意味しない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2024"}
  - {field: stage, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2023-2024"}
  - {field: time, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2022-2024"}
predictions:
  - {claim: "2025年のサービス系BtoC-EC市場規模が2024年の8兆2,256億円を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf
status: verified
updated: 2026-08-11
---

# サービスECの拡大

## 何が変わったか

旅行、チケットなどを含むサービス系の消費者向け電子商取引市場が拡大している。経済産業省の令和6年度電子商取引市場調査では、2024年のサービス系BtoC-EC市場規模は8兆2,256億円で、2023年の7兆5,169億円から前年比9.43％増となった。

この数字は調査上のサービス分野のBtoC-EC市場規模であり、サービス産業全体の売上や、すべての予約・決済のオンライン化率ではない。旅行需要の回復、チケット販売、金融・保険など、内訳ごとに動きが異なる可能性がある。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象はサービス購入の電子取引額であり、特定企業の広告費やEC機能の導入数ではない。

**stage: growing とした。** 2023年から2024年に市場規模が9.43％増えたためである。ただし、サービス分野の合算値なので、すべてのサービスカテゴリが同じ方向に増えたとは判定しない。

## 時間

サービス分野の同一定義の比較値を確認できる2022年以降を `2023~` とした。終点は `..`（継続中）。

## チャネルと伝播

予約サイト、チケット販売、事業者直販、アプリ、決済サービスなど複数の取引接点が含まれうるが、調査は個別チャネル別の寄与を示していない。

## 反証（これが偽なら何が観測されるか）

- 次回の同じ定義の調査でサービス系BtoC-EC市場規模が8兆2,256億円を下回る
- 市場規模が増えても、主要なサービス分野のオンライン取引額が増えておらず、一部区分だけの名目増と分かる
- サービス産業全体の売上や利用者数が減少し、EC市場規模の増加が需要拡大を示さないと確認される

## 未着手

- サービス分野の内訳別市場規模と成長率を分解する
- 予約件数、利用者数、単価、キャンセル、オフライン併用を同じ定義で比較する
- 2025年公表値で予測を答え合わせする
