---
id: practice/single-person-service-design
uri: urn:mtn:practice/single-person-service-design
type: practice
label_ja: 単独世帯向け小容量・個別配送・継続利用設計
label_en: Small-pack, individual-delivery, and retention design for single-person households
authority:
  wikidata: null
  none_reason: "Wikidataで「単独世帯向け小容量・個別配送・継続利用設計」「single-person service design」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2020~"
  end: ".."
  display: "単独世帯の増加を前提に、容量・配送・契約単位を個人生活に合わせる運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2020"}
channels: []
relations:
  - {type: responds_to, target: trend/single-person-household-expansion, certainty: hypothesis, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf"}
sources:
  - https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf
status: draft
updated: 2026-08-11
---

# 単独世帯向け小容量・個別配送・継続利用設計

## 何をするか

一人で使い切れる容量、受取やすい配送、少量でも成立する価格、個人単位の契約・解約、必要なときだけ追加できる継続利用を設計する。家族世帯向けのまとめ買いを単純に小さくするのではなく、保管、調理、受取、廃棄、支払いの負担を分解して見る。

## どのトレンドへの応答か

[trend/single-person-household-expansion](../trends/single-person-household-expansion.md)（単独世帯の拡大）への応答とみる。単独世帯が増えるほど、世帯人数を前提にした容量・配送・契約設計と、個人の生活時間に合う接点を見直す余地が広がるためである。ただし、このpracticeが単独世帯の購買や継続率を改善するとは確認していないため、関係の確度は`hypothesis`とした。

## 成立条件・失敗条件

**効果未確認**: 小容量商品、個別配送、個人契約を対象事業で比較運用していない。購入頻度、使い切り率、配送不在、解約率、客単価、粗利は未測定である。

## 飽和度の判定

`spreading` とした。単独世帯の増加は確認できるが、全業種で小容量・個別配送・継続利用設計が標準化したとは言えない。

## 利用上の注意

**効果未確認**: 一つの商品またはサービスだけで、通常容量と小容量、通常配送と受取しやすい配送を比較し、購入継続、廃棄、不在、問い合わせを分けて記録する。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
