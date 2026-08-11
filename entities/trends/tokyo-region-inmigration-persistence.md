---
id: trend/tokyo-region-inmigration-persistence
uri: urn:mtn:trend/tokyo-region-inmigration-persistence
type: trend
kind: demand-shift
stage: peak
market: cross-category
geo: japan
label_ja: 東京圏への転入超過の持続
label_en: Persistence of net in-migration to the Tokyo region
authority:
  wikidata: null
  none_reason: "「東京圏への転入超過の持続」「persistent net in-migration to Tokyo region」で検索したが、日本の住民基本台帳に基づく東京圏人口移動の変化そのもののWikidata項目は確認できない"
time:
  start: "1995~"
  end: ".."
  display: "東京圏への日本人の転入超過が長期継続し、地域別の雇用・消費・住居設計を分ける局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 東京圏の転入超過
  note: "「東京圏への転入超過の持続」は、総務省統計局の住民基本台帳人口移動報告を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: stage, source: "https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html", certainty: independent, retrieved: primary, as_of: "1995-2025"}
  - {field: time, source: "https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025all.pdf", certainty: independent, retrieved: primary, as_of: "1954-2025"}
predictions:
  - {claim: "2026年の東京圏における日本人移動者が転入超過となり、2025年の11万2738人を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/idou/2025np/jissu/youyaku/index.html
  - https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025all.pdf
status: verified
updated: 2026-08-12
---

# 東京圏への転入超過の持続

## 何が変わったか

東京圏への人口移動が一時的な景気や通学の変化だけでなく、長期的な雇用・教育・住宅・サービス配置の前提になっている。2025年の住民基本台帳人口移動報告では、日本人移動者の東京圏は11万2738人の転入超過で、30年連続となった。大阪圏は3年連続の転入超過、名古屋圏は13年連続の転出超過だった。

2025年の東京圏の転入超過は前年より6599人縮小しており、長期継続は毎年同じ規模での集中を意味しない。外国人移動者の動きや、東京圏内の自治体差も日本人移動者とは分けて見る必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 観測しているのは、住民の移動による地域別の人口・需要配置の変化であり、特定の企業やサービスの導入ではないためである。

**stage: peak とした。** 東京圏への日本人転入超過が30年連続しており、地域配置の前提として既に成熟した長期パターンだからである。ただし、規模縮小や大阪圏の転入超過など、内部の変化は継続している。

## 時間

2025年時点で30年連続とされる `1995~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

就職・転職、進学、住宅、通勤、店舗、医療、教育、行政、物流を通じて地域別の需要へ伝わる。転入超過が一人当たり消費や生活満足を直接押し上げる因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 東京圏集中が持続するなら、日本人移動者の転入超過が複数年連続で解消することはないはず
- 地域需要の差が人口移動に由来するなら、年齢、移動目的、雇用、住宅の地域差にも同方向の変化が現れるはず
- 東京圏が一方的に優位なら、大阪圏や地方中核都市の転入超過への転換は観測されないはず

## 未着手

- 年齢、性別、移動前住所、移動理由、在留資格、就業を分けて追う
- 東京圏内の自治体差と、大阪圏・地方中核都市とのサービス需要を比較する
- 次回の住民基本台帳人口移動報告で予測を答え合わせする
