---
id: trend/foodservice-demand-recovery
uri: urn:mtn:trend/foodservice-demand-recovery
type: trend
kind: demand-shift
stage: growing
market: food-beverage
geo: japan
label_ja: 外食・飲食サービス需要の回復
label_en: Recovery of foodservice demand
authority:
  wikidata: null
  none_reason: "「外食・飲食サービス需要の回復」「foodservice demand recovery Japan」で検索したが、この日本の飲食サービス需要の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: "コロナ禍後に飲食店・飲食サービス業が上昇し、フード・ビジネス全体が3年連続で上昇した局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 飲食店・飲食サービス業の回復と単価上昇
  note: "「外食・飲食サービス需要の回復」は、経済産業省のフード・ビジネス指数分析を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html", certainty: independent, retrieved: primary, as_of: "2024"}
  - {field: stage, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html", certainty: independent, retrieved: primary, as_of: "2022-2024"}
  - {field: time, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html", certainty: independent, retrieved: primary, as_of: "2022-2024"}
predictions:
  - {claim: "2025年のフード・ビジネス指数が2024年の96.3を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html
status: verified
updated: 2026-08-11
---

# 外食・飲食サービス需要の回復

## 何が変わったか

飲食店・飲食サービス業を含むフード・ビジネスが、コロナ禍の落ち込みから回復し、価格・客単価の上昇も伴う局面にある。経済産業省の2024年分析では、フード・ビジネス指数（FBI）は96.3で前年比0.3％上昇し、3年連続の上昇となった。飲食店・飲食サービス業は前年比3.5％上昇し、FBI全体を押し上げた。

分析では、食堂・レストラン・専門店、パブ・居酒屋、ファーストフードなど業態による寄与が異なり、インバウンド需要や物価上昇も影響している。指数上昇を実質的な来店者数の増加や全業態の繁盛と同一視しない。

## kind と stage の判定

**kind: demand-shift とした。** 変化しているのは飲食サービスの活動指数と売上・需要の結果であり、特定店舗の広告施策ではない。

**stage: growing とした。** 2022年以降の回復を経て、2024年までFBIが3年連続で上昇したためである。ただし、価格上昇と客数の寄与、業態・地域差が残るため、実利用が一方向に増えたとは判定しない。

## 時間

同じ分析で回復と2024年の上昇が確認できる2022年以降を `2022~` とした。終点は `..`（継続中）。

## チャネルと伝播

店舗、テイクアウト、配達、予約、外食モール、インバウンド、ファーストフード、レストラン、居酒屋など複数の接点がある。業態別の来店・注文経路の因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回の同じ指数でFBIが低下し、飲食店・飲食サービス業も複数業態で下落する
- 指数上昇が物価・客単価だけで、来店者数、注文数、稼働店舗が増えていないと分かる
- インバウンドや一部業態を除くと、外食・飲食サービスの回復が再現されない

## 未着手

- 客数、客単価、店舗数、業態、地域、価格要因を分解する
- 店舗、テイクアウト、配達、予約、外食ECの利用経路を同じ期間で比較する
- 2025年の指数で予測を答え合わせする
