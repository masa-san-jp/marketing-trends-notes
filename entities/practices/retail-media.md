---
id: practice/retail-media
uri: urn:mtn:practice/retail-media
type: practice
label_ja: リテールメディア広告
label_en: Retail media advertising
saturation: spreading
authority:
  wikidata: null
  none_reason: 執筆環境からWikidata APIに到達できず未確認（retail media で項目がある可能性がある）
time:
  start: "2019~"
  end: ".."
  display: 米国でAmazon広告の急成長期から。日本は数年遅れとされる
evidence:
  - {field: time, source: "https://www.dentsu.co.jp/knowledge/ad_cost/", certainty: vendor, retrieved: summary, as_of: "2025"}
relations:
  - {type: responds_to, target: trend/tracking-restrictions, certainty: hypothesis, source: "https://developer.apple.com/app-store/user-privacy-and-data-use/"}
  - {type: responds_to, target: trend/japan-btoc-ec-expansion, certainty: hypothesis, source: "https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html"}
sources:
  - https://www.dentsu.co.jp/knowledge/ad_cost/
  - https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html
status: draft
updated: 2026-08-11
---

# リテールメディア広告

## 何をするか

小売事業者（EC・ドラッグストア・コンビニ等）が、自社の購買データと売場（サイト内検索・アプリ・
店頭サイネージ）を広告枠として外部の広告主に販売する。広告主から見れば、購買という結果データに
最短距離で繋がった配信面を買う施策。

## どのトレンドへの応答か

[trend/tracking-restrictions](../trends/tracking-restrictions.md)（広告トラッキング制約の常態化）への
応答とみる——サードパーティデータでユーザーを追えなくなるほど、購買データを**自前で**持つ小売の
配信面の相対価値が上がる。ただしこの因果は**私の仮説**（`certainty: hypothesis`）で、制約が無くても
EC の成長だけでリテールメディアは伸びた可能性がある。仮説の根拠側として、制約の実在は
[Apple の一次文書](https://developer.apple.com/app-store/user-privacy-and-data-use/)で確認済み。
**未確認**: この因果を主張する独立した研究・調査。

同時に、[trend/japan-btoc-ec-expansion](../trends/japan-btoc-ec-expansion.md)への応答ともみる。
EC取引が拡大すると、小売事業者が持つデジタル購買接点と購買データを広告面として設計する余地が広がる、
という仮説である。経済産業省の公式発表本文はEC市場規模とEC化率の拡大を示すが、リテールメディアの成長との因果までは示していない。
**未確認**: EC拡大がリテールメディアの採用・広告費を押し上げたことを示す独立した研究・調査。

## 効いた条件・効かない条件

**未実施**（自分の事業で試していない）。効いた・効かないを書ける段階にない。

**未確認**: 国内の市場規模。電通「[日本の広告費](https://www.dentsu.co.jp/knowledge/ad_cost/)」系の
推計が定番の出典だが、発行元は広告を売る側なので `vendor`（ベンダー調べ）としてしか使えない。
かつ執筆環境から実読できていない。独立した規模の出典は見つかっていない。

## 飽和度の判定

`saturation: spreading` とした。国内では参入する小売・対応する広告主が増えている局面という
定性判断で、**定量の裏づけは未確認**。commoditized（参加が前提になり超過収益が消える）の判定には
主要小売の広告事業の粗利か、広告主側の入札単価の推移が要る。

## 自分の事業にどう使うか

**未実施。** 小規模事業者にとっては「買う側」より「自社の顧客接点を広告面として設計する側」の
発想（自社サイト・メルマガ・同梱物の面としての価値づけ）に転用できる可能性があるが、これは
まだ思いつきの段階で、試すとしたら何を測るかから設計が要る。
