---
id: trend/redelivery-reduction
uri: urn:mtn:trend/redelivery-reduction
type: trend
kind: regulation-driven
stage: growing
market: retail-commerce
geo: japan
label_ja: 宅配便の再配達削減
label_en: Redelivery reduction in parcel delivery
authority:
  wikidata: null
  none_reason: "「宅配便の再配達削減」「redelivery reduction in Japan」で検索したが、日本の再配達率と受取方法の政策的変化そのもののWikidata項目は確認できない"
time:
  start: "2022~"
  end: ".."
  display: "宅配ボックス・置き配など多様な受取方法を通じて、宅配便の再配達率を下げる局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 宅配便再配達率の削減
  note: "「宅配便の再配達削減」は、国土交通省の再配達率調査と受取方法の推進を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html", certainty: independent, retrieved: primary, as_of: "2025-04"}
  - {field: stage, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html", certainty: independent, retrieved: primary, as_of: "2022-10-2025-04"}
  - {field: time, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html", certainty: independent, retrieved: primary, as_of: "2022-2025"}
predictions:
  - {claim: "2026年10月の宅配便再配達率が2025年4月の8.4％を上回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    ECの注文画面、配送通知、日時指定、宅配ボックス、置き配、店舗受取、配送先変更、返品受付を通じて、購入後の受取体験へ伝わる。再配達率の低下が購入頻度や顧客満足を改善する因果は未確認である。
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html
status: verified
updated: 2026-08-12
---

# 宅配便の再配達削減

## 何が変わったか

宅配便の取扱量が大きいまま、受取方法を多様化して再配達を減らすことが、物流の持続可能性と購買体験の両方の課題になっている。国土交通省は宅配ボックスや置き配などを推進し、2025年4月の再配達率は8.4％となった。2024年10月の9.0％、2022年10月の10.6％から低下している。

この調査は大手宅配事業者6社をベースにしたサンプルであり、全配送の再配達率や個別事業者の効果を直接示すものではない。都市部は9.3％、都市部近郊は7.9％、地方は7.0％で、地域差も残っている。

## kind と stage の判定

**kind: regulation-driven とした。** 受取方法の普及だけでなく、国土交通省が再配達削減を政策課題として調査・推進し、物流の担い手不足への対応と結び付けているためである。

**stage: growing とした。** 2022年から2025年にかけて率は低下したが、再配達はなお発生しており、受取方法・通知・配送事業者・住宅環境をまたぐ改善余地が残るためである。

## 時間

比較可能な国土交通省の調査基準である `2022~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

ECの注文画面、配送通知、日時指定、宅配ボックス、置き配、店舗受取、配送先変更、返品受付を通じて、購入後の受取体験へ伝わる。再配達率の低下が購入頻度や顧客満足を改善する因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 受取方法の多様化が定着しているなら、再配達率が複数回の調査で上昇し続けることはないはず
- 再配達削減が物流負荷を軽くするなら、配送事業者の再訪問件数や配送時間にも改善が現れるはず
- 受取方法の選択肢だけで十分なら、地域・住宅条件別の差は縮小するはず

## 未着手

- 受取方法、注文導線、住宅条件、配送地域別に再配達率を比較する
- 再配達削減と配送費、返品、顧客満足、購入継続の関係を確認する
- 2026年以降の4月・10月調査で予測を答え合わせする
