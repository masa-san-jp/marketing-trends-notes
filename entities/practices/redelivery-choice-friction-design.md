---
id: practice/redelivery-choice-friction-design
uri: urn:mtn:practice/redelivery-choice-friction-design
type: practice
label_ja: 再配達抑制・受取選択設計
label_en: Redelivery-friction and delivery-choice design
authority:
  wikidata: null
  none_reason: "「再配達抑制・受取選択設計」「redelivery-friction and delivery-choice design」で検索したが、この運用の型そのもののWikidata項目は確認できない"
time:
  start: "2022~"
  end: ".."
  display: "再配達が発生しやすい注文に、受取方法・通知・変更手段を先回りして組み込む運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html", certainty: independent, retrieved: primary, as_of: "2022-2025"}
channels: []
relations:
  - {type: responds_to, target: trend/redelivery-reduction, certainty: hypothesis, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html"}
sources:
  - https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html
status: draft
updated: 2026-08-12
---

# 再配達抑制・受取選択設計

## 何をするか

注文時と発送後に、宅配ボックス、置き配、日時指定、店舗受取、配送先変更を選びやすくし、受取失敗の可能性が高い注文には通知と変更導線を先に提示する。受取方法、受取成功、再配達、配送費、返品、問い合わせを同じ注文単位で記録する。

## どのトレンドへの応答か

[trend/redelivery-reduction](../trends/redelivery-reduction.md)（宅配便の再配達削減）への応答とみる。国土交通省が多様な受取方法を推進し、再配達率と地域差を継続的に測定しているためである。この設計が特定事業者の再配達をどれだけ下げるかは未確認のため、関係の確度は`hypothesis`とした。

## 効いた条件・効かない条件

**未実施。** 受取方法を顧客・住宅・商品温度帯・配送地域別に出し分けておらず、選択率と再配達率の差を検証していない。選択肢を増やしても、補償、荷姿、通知のタイミング、住宅環境が合わなければ使われない。

## 飽和度の判定

`spreading` とした。宅配ボックス・置き配・日時指定は普及しているが、注文単位で受取選択と再配達を一貫して測る運用の普及度は未確認である。

## 自分の事業にどう使うか

**未実施。** 一つの配送商品で受取方法を比較可能にし、選択、受取成功、再配達、費用、返品、問い合わせを同じ注文単位で記録する。
