---
id: trend/sustainable-fashion-behavior
uri: urn:mtn:trend/sustainable-fashion-behavior
type: trend
kind: demand-shift
stage: emerging
market: fashion-beauty
geo: japan
label_ja: サステナブルファッションへの関心・循環行動
label_en: Interest in and circular behavior around sustainable fashion
authority:
  wikidata: null
  none_reason: "Wikidataで「サステナブルファッション」「sustainable fashion behavior」を確認したが、日本の生活者の関心・循環行動の変化そのものの項目は確認できない"
time:
  start: "2025~"
  end: ".."
  display: 環境省の令和7年度調査と2025年版衣類マテリアルフローで観測できる局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: サステナブルファッション
  note: "「サステナブルファッションへの関心・循環行動」は、環境省の調査項目と衣類の循環フローを要約するための記述的なラベル。生活者がこの複合語を自称するかは確認していない"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-09-12"
evidence:
  - {field: kind, source: "https://www.env.go.jp/policy/sustainable_fashion/about/", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: stage, source: "https://www.env.go.jp/policy/sustainable_fashion/resources/", certainty: independent, retrieved: primary, as_of: "2026-03"}
  - {field: time, source: "https://www.env.go.jp/content/000389225.pdf", certainty: independent, retrieved: primary, as_of: "2025"}
predictions:
  - {claim: "次回の同テーマ独立調査で、サステナブルファッションの認知・関心層が2025年調査の約6割・約4割を大きく下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.env.go.jp/policy/sustainable_fashion/about/
  - https://www.env.go.jp/policy/sustainable_fashion/resources/
  - https://www.env.go.jp/content/000389225.pdf
  - https://www.env.go.jp/press/press_03475.html
status: verified
updated: 2026-08-12
---

# サステナブルファッションへの関心・循環行動

## 何が変わったか

衣類を買う・使う・手放すときに、必要量、長期使用、回収、リユース、リペアを考慮する生活者の関心と意向が、
環境省の2025年調査でまとまった形で観測されている。

環境省のページに掲載された令和7年度調査では、サステナブルファッションを「知っている」層が約6割、関心があるか
具体的な取組を行っている層が約4割だった。具体的な項目では、「本当に必要かどうか考えて購入する」が85.7％、
「素材に適した手入れや洗濯を心掛け、長く着る」が77.4％、「衣料品販売店の店頭回収や回収ボックスに持っていく」が
65.7％、「リユースショップや古着屋に持っていく」が60.3％、「中古衣服を購入する」が41.5％だった。

ただし、これらの項目は「現在取り組んでいること」と「今後取り組みたいこと」を合わせた掲載値であり、実際に行った人の
割合だけではない。購入意向・回収意向をそのまま購買実績やリユース実績とみなさない。

同じ年度の環境省資料では、2025年版の衣類マテリアルフローとして、国内の衣類新規供給量82万トンに対し、約50万トンが
焼却・埋立等で処理されると推計されている。家庭から手放された衣類のうち、リユース35％とリサイクル7％を合わせた再活用は
42％で、残り58％は焼却等とされる。生活者の関心が、そのまま循環実績に転換しているわけではないことも同時に示している。

環境省は2026年3月に、家庭から廃棄される衣類を2030年度までに2020年度比25％削減するためのアクションプランを取りまとめた。
方針と目標が更新されても、生活者の関心が実際の回収・リユース・リペアへ転換したことまでは示さない。

## kind と stage の判定

**kind: demand-shift とした。** 観測しているのは、衣類の購入・使用・廃棄に関する生活者の認知、関心、行動意向と、家庭から
手放された衣類の行き先である。環境省の独立調査に基づくため、アパレル企業が売り込む市場カテゴリ（vendor-pushed）としては置かない。

**stage: emerging とした。** 認知・関心・循環行動の意向は一定規模で観測され、政府も2030年度までに家庭から廃棄される衣類を
2020年度比25％削減する目標と行動方針を示している。一方、同じ設問の経年値、実際の購入・回収・リペア率、ブランド選択への影響は
今回確認できていない。意向と実績の差が残るため、一般化したpeakではなくemergingに留める。

## 時間

始点は `2025~` とした。これはサステナブルファッションの始まりではなく、今回確認した令和7年度調査と2025年版マテリアルフローの
観測時点である。終点は `..`（継続中）。

## チャネルと伝播

特定のSNS・EC・店舗が発生チャネルではなく、生活者調査と衣類の循環フローで観測される変化なので、`channels` は張らない。
**未確認**: サステナブル情報が、検索、商品タグ、店頭回収、リユースショップ、フリマアプリなどのどの接点で行動に変わるか。

## 反証（これが偽なら何が観測されるか）

- 次回の独立調査で認知・関心・循環行動の意向が大きく低下し、2025年の約6割・約4割という観測が一時的なものと分かる
- 「関心・意向が実際の循環行動につながる」が偽なら、回収・リユース・リペアの実績や衣類マテリアルフローが改善せず、
  意向値と実績値の差が縮まらない
- ファッションの購買判断に影響していないなら、環境配慮素材・長期使用・リユース品に関する購入実績や選択理由に差が観測されない

## 未着手

- 調査の標本・設問・「実施」と「今後取り組みたい」の分解を原票で確認する
- 令和2年度以降の同種調査・マテリアルフローを並べ、関心と実績の経年変化をそろえる
- 新品購入、リユース、回収、リペアの各接点で、行動意向から実績への転換率を確認する
- 応答するpractice（回収・リペア・リユース連携、環境配慮情報の表示等）の採用率と行動転換率を確認する
