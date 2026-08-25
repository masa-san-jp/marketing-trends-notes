---
id: practice/digital-salary-choice-governance
uri: urn:mtn:practice/digital-salary-choice-governance
type: practice
label_ja: 賃金デジタル払いの選択・同意・保護設計
label_en: Digital salary choice, consent, and protection governance
authority:
  wikidata: null
  none_reason: "「賃金デジタル払いの選択・同意・保護設計」「digital salary choice consent governance」で検索したが、この運用の型そのもののWikidata項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: "給与の受取方法を強制せず、指定業者、同意、代替口座、不正補償、給与計算をつなぐ運用"
saturation: novel
evidence:
  - {field: time, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/newpage_55437.html", certainty: independent, retrieved: primary, as_of: "2024-2026"}
channels: []
relations:
  - {type: responds_to, target: trend/digital-salary-payment, certainty: hypothesis, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/newpage_55437.html"}
sources:
  - https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/newpage_55437.html
  - https://www.mhlw.go.jp/content/11200000/001478565.pdf
status: draft
updated: 2026-08-12
---

# 賃金デジタル払いの選択・同意・保護設計

## 何をするか

指定資金移動業者の保全・補償・換金性を確認し、労使協定、従業員への説明、個別同意、指定代替口座、給与計算、取消・退職時の処理を一つの運用として設計する。銀行口座や現金を選ぶ人を除外せず、選択率、処理失敗、不正、問い合わせ、解約を記録する。

## どのトレンドへの応答か

[trend/digital-salary-payment](../trends/digital-salary-payment.md)（賃金デジタル払いの制度化）への応答とみる。厚生労働省は指定業者の確認から個別同意、事務処理までの手続を示し、デジタル払いを強制しないことを明記しているためである。導入が従業員体験や給与業務を改善する効果は未確認のため、関係の確度は`hypothesis`とした。

## 成立条件・失敗条件

**効果未確認**: 同意取得、代替口座、不正補償、入金失敗、給与計算、従業員属性別の選択率を検証していない。決済サービスを用意するだけでは、制度理解、資金保全への不安、給与担当の事務負荷が解消されなければ定着しない。

## 飽和度の判定

`novel` とした。制度と指定業者は整備されつつあるが、選択・同意・保護・給与実務を一体で運用する企業側の普及度は未確認である。

## 利用上の注意

**効果未確認**: 一つの事業場で、従来の給与受取を維持したまま希望者だけを対象に説明、同意、代替口座、入金確認、問い合わせ、解約を記録する。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
