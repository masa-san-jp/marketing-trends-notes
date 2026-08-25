---
id: practice/parcel-receiving-choice-design
uri: urn:mtn:practice/parcel-receiving-choice-design
type: practice
label_ja: 宅配の受取方法・再配達削減設計
label_en: Delivery-choice and redelivery-reduction design
authority:
  wikidata: null
  none_reason: "「宅配の受取方法・再配達削減設計」「parcel delivery choice redelivery reduction design」で検索したが、この運用の型そのもののWikidata項目は確認できない"
time:
  start: "2020~"
  end: ".."
  display: "宅配取扱量の拡大に合わせて、宅配ボックス・置き配・日時指定・店舗受取を選びやすくする運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html", certainty: independent, retrieved: primary, as_of: "2025-04"}
channels: []
relations:
  - {type: responds_to, target: trend/parcel-delivery-volume-expansion, certainty: hypothesis, source: "https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html"}
sources:
  - https://www.mlit.go.jp/report/press/jidosha04_hh_000341.html
  - https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html
status: draft
updated: 2026-08-11
---

# 宅配の受取方法・再配達削減設計

## 何をするか

購入・予約時に宅配ボックス、置き配、日時指定、店舗受取、配送先変更を選びやすくし、荷姿、納期、通知、変更、返品を一つの受取体験として設計する。再配達率、受取成功、配送遅延、問い合わせ、CO2、顧客満足を受取方法別に記録する。

## どのトレンドへの応答か

[trend/parcel-delivery-volume-expansion](../trends/parcel-delivery-volume-expansion.md)（宅配便取扱量の拡大）への応答とみる。国土交通省がEC拡大と宅配量の増加、再配達・担い手不足を同時に課題化しているため、配送量を増やすだけでなく受取成功率を設計するためである。practiceの効果は未確認のため、関係の確度は`hypothesis`とした。

## 成立条件・失敗条件

**効果未確認**: 受取方法別の選択、成功、再配達、配送費、返品、顧客満足を比較していない。選択肢を増やしても、説明、補償、荷姿、温度管理、住宅環境が合わなければ利用されない。

## 飽和度の判定

`spreading` とした。宅配ボックス・置き配・日時指定は普及しつつあるが、受取方法を購買導線・物流負荷・顧客体験で統合測定する運用の普及度は未確認である。

## 利用上の注意

**効果未確認**: 一つの配送商品で受取方法を比較可能にし、選択、成功、再配達、費用、返品、問い合わせを同じ注文単位で記録する。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
