---
id: trend/electrified-vehicle-adoption
uri: urn:mtn:trend/electrified-vehicle-adoption
type: trend
kind: tech-enabled
stage: growing
market: consumer-goods
geo: japan
label_ja: 乗用車の電動化拡大
label_en: Expansion of electrified passenger vehicles
authority:
  wikidata: null
  none_reason: "「乗用車の電動化拡大」「electrified vehicle adoption Japan」で検索したが、日本の乗用車販売構成の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "HEV・PHEV・BEV・FCVを含む電動車の新車販売比率が高まる局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 電動車の普及拡大
  note: "「乗用車の電動化拡大」は、資源エネルギー庁・経済産業省の電動車定義と販売比率を要約する記述的なラベル。BEVだけの拡大とは区別する"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.enecho.meti.go.jp/about/special/johoteikyo/xev_cev_2024.html?ui_medium=lpene", certainty: attested, retrieved: primary, as_of: "2024-06-24"}
  - {field: stage, source: "https://www.enecho.meti.go.jp/about/energytrends/202506/html/s-1-3.html", certainty: independent, retrieved: summary, as_of: "2024"}
  - {field: time, source: "https://www.enecho.meti.go.jp/about/special/johoteikyo/xev_cev_2024.html?ui_medium=lpene", certainty: independent, retrieved: primary, as_of: "2023年度-2024"}
predictions:
  - {claim: "次回の資源エネルギー庁または自動車関連公的統計で、乗用車新車販売に占める電動車比率が2024年の57％を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定の広告媒体が発生チャネルだとは置かない。車両価格、補助金、燃費・航続距離、充電インフラ、販売店・整備網、法人車両更新、環境意識が購入構成に影響する。
channels: []
relations: []
sources:
  - https://www.enecho.meti.go.jp/about/special/johoteikyo/xev_cev_2024.html?ui_medium=lpene
  - https://www.enecho.meti.go.jp/about/energytrends/202506/html/s-1-3.html
status: verified
updated: 2026-08-11
---

# 乗用車の電動化拡大

## 何が変わったか

乗用車の新車販売で、電動車の構成比が高まっている。資源エネルギー庁は電動車を、電気自動車（EV）、燃料電池自動車（FCV）、プラグインハイブリッド（PHEV）、ハイブリッド（HEV）と定義している。同庁の2024年記事では、2023年度の国内乗用車新車販売でHEVが約50％、EV・FCV・PHEV合計が約3.5％だった。

さらに、資源エネルギー庁の「エネルギー動向（2025年6月版）」は、2024年の乗用車新車販売に占める電動車比率を57％としている。この数値はBEVだけの販売比率ではなく、HEV等を含むため、「EVが57％」とは解釈しない。充電、価格、航続距離、整備・中古車流通などの課題も残る。

## kind と stage の判定

**kind: tech-enabled とした。** 電動車という車両技術がなければ成立しない販売構成の変化であり、政策補助や需要の変化だけでは現象を説明できないためである。

**stage: growing とした。** 2023年度の構成比と2024年の電動車比率が高い水準にあり、資源エネルギー庁も普及拡大と整理している。ただし、電動車内部ではHEVとBEV等の構成が異なるため、単一のEV市場が主流化したとは判定しない。

## 時間

電動車の販売構成が政策・補助制度とともに追える2020年代を `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定の広告媒体が発生チャネルだとは置かない。車両価格、補助金、燃費・航続距離、充電インフラ、販売店・整備網、法人車両更新、環境意識が購入構成に影響する。

## 反証（これが偽なら何が観測されるか）

- 同じ定義の統計で電動車の新車販売比率が複数年連続して低下する
- HEVを含む電動車比率は高くても、BEV・PHEV・FCVが増えず、電動化の範囲が一部技術に固定されたままと分かる
- 補助制度や充電インフラの整備後も、購入・保有・利用の公的指標が増えない

## 未着手

- HEV、PHEV、BEV、FCVを分けた年次販売・保有台数を同じ定義で整理する
- 充電器設置、走行距離、車両価格、中古車価格、法人保有の関係を確認する
- 2025年以降の電動車比率と、電動車内部の構成変化を一次資料で答え合わせする
