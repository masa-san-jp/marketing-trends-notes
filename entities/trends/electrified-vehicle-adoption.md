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
  - {field: kind, source: "https://www.enecho.meti.go.jp/about/special/johoteikyo/xev_cev_2024.html?ui_medium=lpene", certainty: attested, retrieved: primary, as_of: "2024-06-24", tense: completed}
  - {field: stage, source: "https://www.enecho.meti.go.jp/about/energytrends/202506/html/s-1-3.html", certainty: independent, retrieved: summary, as_of: "2024", tense: completed}
  - {field: time, source: "https://www.enecho.meti.go.jp/about/special/johoteikyo/xev_cev_2024.html?ui_medium=lpene", certainty: independent, retrieved: primary, as_of: "2023年度-2024", tense: completed}
  - {field: current-status, source: "https://www.jama.or.jp/release/news_release/2026/3582/", certainty: independent, retrieved: primary, as_of: "2025-09", tense: intended}
predictions:
  - {claim: "次回の資源エネルギー庁または自動車関連公的統計で、乗用車新車販売に占める電動車比率が2024年の57％を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "日本自動車工業会の次回（2026年度）乗用車市場動向調査で、次期購入車として電動車（HEV・PHEV・BEV・FCEV）を希望する割合が2025年度調査の「4割台半ば」を大きく下回らない", by: "2027-06", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定の広告媒体が発生チャネルだとは置かない。車両価格、補助金、燃費・航続距離、充電インフラ、販売店・整備網、法人車両更新、環境意識が購入構成に影響する。
channels: []
relations: []
sources:
  - https://www.enecho.meti.go.jp/about/special/johoteikyo/xev_cev_2024.html?ui_medium=lpene
  - https://www.enecho.meti.go.jp/about/energytrends/202506/html/s-1-3.html
  - https://www.jama.or.jp/release/news_release/2026/3582/
status: verified
updated: 2026-09-16
---

# 乗用車の電動化拡大

## 見出している未来（何に向かって動いているか）

乗用車保有者・購入検討者は、次の車で電動車を選ぶ方向に向かっている。日本自動車工業会の
「2025年度乗用車市場動向調査」（2025年9月5日〜9月22日実施、WEB法、単身世帯を含む一般世帯を
層化抽出）では、今後の保有・購入動向として「電動車意向は4割台半ば」と報告されている。環境
対応車の中で購入検討順位1位とした割合は「ハイブリッド車（HEV）」が最も高いが、「電気自動車
（BEV）」も2割強が検討順位1位としている。ただし、自宅充電器の設置は1割未満にとどまり、
「CEV補助金制度」の内容認知は1割台半ばに留まるなど、意向と実際の購入環境の整備には差がある。

これは次に車を買うときにどの動力方式を選びたいかという意向調査であり、実際の新車販売構成比
（既存のevidenceにある2023年度HEV約50％・EV等合計約3.5％、2024年の電動車比率57％）とは
別の指標である。意向が実際の購入にどこまで反映されるかは、次回以降の販売実績で確認する。

## 足元の根拠（完了した事実）

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

- 2026年9月16日、日本自動車工業会「2025年度乗用車市場動向調査」のプレスリリースを実読して見出している未来を追記した。「電動車意向4割台半ば」という表現の厳密な数値（45〜46％台のどこか）はプレスリリース本文に明記されておらず、報告書本体の該当ページには到達していない
- HEV、PHEV、BEV、FCVを分けた年次販売・保有台数を同じ定義で整理する
- 充電器設置、走行距離、車両価格、中古車価格、法人保有の関係を確認する
- 2025年以降の電動車比率と、電動車内部の構成変化を一次資料で答え合わせする
- 「電動車意向」（次期購入意向）と実際の新車販売構成比の差が、どの程度・どの期間で縮小するかを追う
