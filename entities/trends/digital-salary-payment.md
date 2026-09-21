---
id: trend/digital-salary-payment
uri: urn:mtn:trend/digital-salary-payment
type: trend
kind: regulation-driven
stage: emerging
market: finance
geo: japan
label_ja: 賃金デジタル払いの制度化
label_en: Institutionalization of digital salary payments
authority:
  wikidata: null
  none_reason: "「賃金デジタル払いの制度化」「digital salary payments in Japan」で検索したが、日本の賃金支払制度の変化そのもののWikidata項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: "指定資金移動業者の口座を賃金の受取方法として選べる制度が整備される局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 資金移動業者口座への賃金支払い
  note: "「賃金デジタル払いの制度化」は、厚生労働省が説明する制度と導入手続を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-09-15"
  recheck_by: "2026-10-15"
evidence:
  - {field: kind, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/newpage_55437.html", certainty: independent, retrieved: primary, as_of: "2024-08", tense: completed}
  - {field: stage, source: "https://www.mhlw.go.jp/content/11200000/001478565.pdf", certainty: independent, retrieved: primary, as_of: "2025-03-31", tense: completed}
  - {field: time, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/newpage_55437.html", certainty: independent, retrieved: primary, as_of: "2024-2026", tense: completed}
  - {field: prediction, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/03_00028.html", certainty: independent, retrieved: primary, as_of: "2026-07-01", tense: completed}
  - {field: current-status, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/03_00028.html", certainty: independent, retrieved: primary, as_of: "2026-09-15", tense: completed}
  - {field: current-status, source: "https://www.mhlw.go.jp/content/11200000/001690304.pdf", certainty: independent, retrieved: primary, as_of: "2026-03", tense: intended}
predictions:
  - {claim: "指定資金移動業者の数が2025年3月31日時点の83事業者を下回らない", by: "2027-12", resolved: "2026-08-12", outcome: miss}
  - {claim: "厚生労働省の次回同種調査で、労働者の賃金デジタル払い「今後利用したい」割合が令和7年度調査の13.8%を大きく下回らない", by: "2028-03", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    給与計算、労務管理、労使協定、スマートフォン決済、資金移動業者、金融教育、福利厚生を通じて、雇用と決済の接点へ伝わる。給与のデジタル受取が消費額や家計管理を変える因果は未確認である。
channels: []
relations: []
sources:
  - https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/newpage_55437.html
  - https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/zigyonushi/shienjigyou/03_00028.html
  - https://www.mhlw.go.jp/content/11200000/001478565.pdf
  - https://www.mhlw.go.jp/content/11200000/001690304.pdf
status: verified
updated: 2026-09-21
---

# 賃金デジタル払いの制度化

## 見出している未来（何に向かって動いているか）

労働者の多くは、現時点では賃金のデジタル払いを利用したいと思っていない。厚生労働省が委託した
「令和7年度賃金のデジタル払いに関するニーズ調査」（2026年3月、労働者調査n=10,000）は、賃金の
デジタル払いの利用意向を尋ね、「利用したくない」が42.4％で最多、「どちらとも言えない」が42.3％、
「今後利用したい」は13.8％、「既に利用している」は1.5％だったとしている。制度の名前・内容を
理解している層では「今後利用したい」が28.5％と、認知度が高い層ほど利用意向も高い傾向が見られた。

これは厚生労働省が労働者本人に直接尋ねた意向調査であり（`independent`）、事業者側の導入意向とは
別の数字である。既存の足元の根拠にある指定資金移動業者数の減少（83社→4社）に加え、労働者側の
「今後利用したい」も13.8%にとどまっており、供給側・需要側の双方でまだ利用が広がっていない
段階にあることを示している。

## 足元の根拠（完了した事実）

給与を銀行口座だけでなく、厚生労働大臣が指定する資金移動業者の口座で受け取れる制度が整備され、給与・決済・福利厚生の接点に新しい選択肢が加わっている。2025年3月31日時点では83事業者全てが対象とされたが、厚生労働省の2026年7月1日現在の一覧では指定業者は4社であり、83事業者を下回った。このため、事業者数の継続拡大を見込む予測はmissと判定した。

導入には、指定業者の確認、サービス選定、労使協定、労働者への説明、個別同意、事務処理の確認が必要である。労働者への強制はできず、現金・銀行口座・証券総合口座も引き続き選択できるため、事業者数の増加は利用定着や利用者満足を直接意味しない。

## kind と stage の判定

**kind: regulation-driven とした。** 利用可能な資金移動業者、資金保全、不正引出し補償、労使協定、個別同意が法令・指定制度によって定義されているためである。

**stage: emerging とした。** 受取方法として制度と指定業者は整ったが、導入企業数、労働者の選択率、給与全体に占める比率がまだ別途確認を要するためである。

## 時間

制度上の賃金支払方法として運用・導入手続が公表された `2023~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

給与計算、労務管理、労使協定、スマートフォン決済、資金移動業者、金融教育、福利厚生を通じて、雇用と決済の接点へ伝わる。給与のデジタル受取が消費額や家計管理を変える因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 制度が拡大しているなら、指定業者や導入事業場が継続的に減少し続けることはないはず
- 受取方法の選択肢が利用価値を持つなら、労働者属性・業種・給与日・利用目的別に選択率の差が現れるはず
- 制度整備が利用定着を意味するなら、指定業者数だけでなく導入企業数と個別同意率も上昇するはず

## 未着手

- 2026年9月21日、厚生労働省委託「令和7年度賃金のデジタル払いに関するニーズ調査」（001690304.pdf）を実読し、労働者の利用意向（今後利用したい13.8%等）を見出している未来として追記した
- 2026年9月15日に指定資金移動業者一覧を再確認した。指定業者数は4社（PayPay、リクルートMUFGビジネス、楽天Edy、auフィナンシャルサービス）のまま変化なし。5社目の新規指定情報も確認できなかった
- 指定業者数の減少後に、指定取消・申請・導入企業数・個別同意率・利用額がどう推移するかを同じ定義で追う
- 給与計算・同意取得・不正補償・解約時の実務負担を比較する
- 事業者と労働者の属性別に、銀行振込との使い分けを確認する
