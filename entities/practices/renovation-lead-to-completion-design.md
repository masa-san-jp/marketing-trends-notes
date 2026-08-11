---
id: practice/renovation-lead-to-completion-design
uri: urn:mtn:practice/renovation-lead-to-completion-design
type: practice
label_ja: リフォーム相談から完工までの一貫設計
label_en: Renovation lead-to-completion experience design
authority:
  wikidata: null
  none_reason: "「リフォーム相談から完工までの一貫設計」「renovation lead-to-completion design」で検索したが、この運用の型そのもののWikidata項目は確認できない"
time:
  start: "2020~"
  end: ".."
  display: "リフォームの相談・現地調査・見積・補助制度・施工・検査・保守を一つの顧客導線にする運用"
saturation: novel
evidence:
  - {field: time, source: "https://www.mlit.go.jp/report/press/content/002005995.pdf", certainty: independent, retrieved: primary, as_of: "2025年度"}
channels: []
relations:
  - {type: responds_to, target: trend/building-renovation-market-expansion, certainty: hypothesis, source: "https://www.mlit.go.jp/report/press/joho04_hh_001375.html"}
sources:
  - https://www.mlit.go.jp/report/press/joho04_hh_001375.html
  - https://www.mlit.go.jp/report/press/content/002005995.pdf
status: draft
updated: 2026-08-12
---

# リフォーム相談から完工までの一貫設計

## 何をするか

相談、現地調査、見積、工事内容、補助・税制、契約、施工、検査、保証、保守を一つの案件IDでつなぐ。受注高だけでなく、相談から成約、工期、追加費用、完工、再工事、設備性能、顧客満足を工事種類・発注者別に記録する。

## どのトレンドへの応答か

[trend/building-renovation-market-expansion](../trends/building-renovation-market-expansion.md)（建築物リフォーム・リニューアル需要の拡大）への応答とみる。国土交通省の調査で住宅・非住宅の受注高が増えている一方、受注高だけでは完工品質や顧客価値が分からないため、相談から完工後までを測る必要がある。この一貫設計が利益や満足を改善する効果は未確認のため、関係の確度は`hypothesis`とした。

## 効いた条件・効かない条件

**未実施。** 発注者、工事種類、建物用途、業者、補助制度別に成約率、工期、追加費用、再工事、性能を比較していない。相談窓口だけを増やしても、現地調査、見積、職人手配、保証情報がつながらなければ離脱や手戻りが増える。

## 飽和度の判定

`novel` とした。施工会社・住宅設備ごとの個別導線はあるが、相談から保守までを案件単位で統合し、工事後の価値まで測る運用の普及度は未確認である。

## 自分の事業にどう使うか

**未実施。** 一つの工事商品で相談、現地調査、見積、契約、施工、検査、保証、再工事を同じ案件IDに結び、工期・追加費用・満足度を記録する。
