---
id: trend/telework-stabilization
uri: urn:mtn:trend/telework-stabilization
type: trend
kind: demand-shift
stage: growing
market: saas-b2b
geo: japan
label_ja: テレワークの定着
label_en: Stabilization of telework
authority:
  wikidata: null
  none_reason: "「テレワークの定着」「telework stabilization」で検索したが、日本の実施率が再上昇する現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "感染症流行後の減少を経て、2025年度にテレワーク実施率が再び上向いた局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: テレワーク実施率の安定・再上昇
  note: "「テレワークの定着」は、国土交通省の実施率調査を要約するための記述的なラベルであり、全職種の働き方が固定化したことを意味しない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/report/press/toshikankyoteleworkr7.html", certainty: independent, retrieved: primary, as_of: "2025年度"}
  - {field: stage, source: "https://www.mlit.go.jp/report/press/toshikankyoteleworkr7.html", certainty: independent, retrieved: primary, as_of: "2025年度"}
  - {field: time, source: "https://www.mlit.go.jp/report/press/toshikankyoteleworkr7.html", certainty: independent, retrieved: primary, as_of: "2020-2025年度"}
predictions:
  - {claim: "次回の同調査でテレワーク実施率が2025年度の16.8％を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/report/press/toshikankyoteleworkr7.html
status: verified
updated: 2026-08-11
---

# テレワークの定着

## 何が変わったか

テレワークは感染症流行期の一時的な働き方から、実施率が一定水準で続く業務設計上の選択肢へ移っている。国土交通省の2025年度調査では、直近1年間のテレワーク実施率は16.8％で、2024年度から1.2ポイント上昇した。雇用型テレワーカーの割合も25.2％で、0.6ポイント上昇している。

同省は、感染症流行後に低下していた実施率が2025年度に上向き、安定した傾向に転じたと整理している。調査は全国約4万人のWeb調査であり、全労働者・全職種が同じようにテレワーク化したことを示すものではない。

## kind と stage の判定

**kind: demand-shift とした。** 観測されたのは、企業と就業者が働く場所・頻度を選ぶ行動の変化であり、特定ベンダーの機能導入数ではない。SaaSや業務ツールへの需要に影響しうるが、同調査だけで特定製品の需要は断定しない。

**stage: growing とした。** 2025年度に実施率が前年度から上昇し、国土交通省も安定傾向への転換を説明している。一方、実施率は16.8％で、職種・地域・企業規模による差が残るため、全面的な主流化とは判定しない。

## 時間

感染症流行期を含む実施率の変化を追うため `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定のツールや広告媒体が発生チャネルだとは置かない。雇用制度、職種の遠隔可能性、オフィス方針、通勤時間、上司・同僚との協働、通信・業務ソフトの整備が組み合わさって実施率に表れる。

## 反証（これが偽なら何が観測されるか）

- 次回以降の同一調査で実施率が複数年連続して低下する
- 雇用型テレワーカーの割合が減り、企業方針としての継続運用が確認できなくなる
- 職種や企業規模を分けた複数の調査で、2025年度の上昇が標本構成だけによると分かる

## 未着手

- 業種・企業規模・地域・頻度別に実施率を分解する
- テレワーク継続と業務ツール費用、採用、離職、成果指標の関係を独立データで確認する
- 次回調査で予測を答え合わせする
