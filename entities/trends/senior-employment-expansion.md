---
id: trend/senior-employment-expansion
uri: urn:mtn:trend/senior-employment-expansion
type: trend
kind: demand-shift
stage: growing
market: cross-category
geo: japan
label_ja: 高齢者就業の拡大
label_en: Expansion of senior employment
authority:
  wikidata: null
  none_reason: "「高齢者就業の拡大」「senior employment expansion in Japan」で検索したが、日本の65歳以上就業者の推移そのもののWikidata項目は確認できない"
time:
  start: "2004~"
  end: ".."
  display: "65歳以上の就業者が長期増加し、働き方・サービス設計の前提を変える局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 高齢者の就業者数の増加
  note: "「高齢者就業の拡大」は、総務省統計局の労働力調査を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.stat.go.jp/data/topics/pdf/topi146_02.pdf", certainty: independent, retrieved: primary, as_of: "2024"}
  - {field: stage, source: "https://www.stat.go.jp/data/topics/pdf/topi146_02.pdf", certainty: independent, retrieved: primary, as_of: "2004-2024"}
  - {field: time, source: "https://www.stat.go.jp/data/topics/pdf/topi146_02.pdf", certainty: independent, retrieved: primary, as_of: "2004-2024"}
  - {field: prediction, source: "https://www.stat.go.jp/data/roudou/sokuhou/nen/ft/pdf/gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "2025"}
predictions:
  - {claim: "次回公表される65歳以上の就業者数が2024年の930万人を下回らない", by: "2027-12", resolved: "2026-08-12", outcome: hit}
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/topics/topi1460.html
  - https://www.stat.go.jp/data/topics/pdf/topi146_02.pdf
  - https://www.stat.go.jp/data/roudou/sokuhou/nen/ft/pdf/gaiyou.pdf
status: verified
updated: 2026-08-12
---

# 高齢者就業の拡大

## 何が変わったか

65歳以上の就業者が増え、商品・サービス、職場、学習、移動、健康管理の設計で「引退後の消費者」だけではない生活者像を前提にする必要が高まっている。総務省統計局によると、2025年平均の65歳以上の就業者数は943万人で、2024年の930万人を上回り、過去最多を更新した。就業者総数に占める割合も13.8％で過去最高だった。

65歳以上の就業率は26.0％で、65～69歳、70～74歳、75歳以上のすべてで過去最高となった。一方、65歳以上の雇用者は非正規が76.9％であり、就業者数の増加は所得、勤務時間、雇用保障が一様に改善したことを意味しない。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は、人口・就業構造の変化に伴う働く生活者の増加であり、単一のサービスや企業の技術導入ではないためである。

**stage: growing とした。** 65歳以上の就業者数と就業率が過去最高を更新し続けている一方、雇用形態や年齢階級による差が大きく、全世代向けに一般化したpeakとは判定しない。

## 時間

統計局が21年連続増加の始点として示す `2004~` を採用した。終点は `..`（継続中）。

## チャネルと伝播

再雇用・継続雇用、短時間勤務、パート・アルバイト、地域就業、職場研修、健康・移動支援を通じて、雇用と生活サービスへ伝わる。就業継続が特定カテゴリの購買額をどの程度押し上げるかは未確認である。

## 反証（これが偽なら何が観測されるか）

- 高齢者就業の拡大が継続しているなら、次回統計で就業者数と就業率が同時に急減することはないはず
- 働く高齢者の増加が事業設計に影響するなら、勤務時間、移動、学習、健康管理を分けた利用差が現れるはず
- 就業者数の増加が生活の改善を意味するなら、非正規比率や所得分布だけでは説明できない改善が観測されるはず

## 未着手

- 年齢階級、雇用形態、所得、就業時間、地域別に生活者ニーズを分解する
- 高齢者就業と金融、健康、移動、学習、余暇サービスの利用を接続する
- 2025年平均結果で予測を答え合わせし、943万人（930万人以上）のhitを記録した
