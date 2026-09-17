---
id: trend/cross-border-ecommerce-expansion
uri: urn:mtn:trend/cross-border-ecommerce-expansion
type: trend
kind: demand-shift
stage: growing
market: retail-commerce
geo: japan
label_ja: 越境ECの拡大
label_en: Expansion of cross-border e-commerce
authority:
  wikidata: null
  none_reason: "「越境ECの拡大」「cross-border e-commerce expansion Japan」で検索したが、日本発着の越境ECフローの拡大現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: "日本・中国・米国間の消費者向け越境EC取引額が増加する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 日米中間の越境EC市場規模拡大
  note: "「越境ECの拡大」は、経済産業省が推計する日米中3か国間の消費者向け越境EC市場規模を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2024", tense: completed}
  - {field: stage, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2023-2024", tense: completed}
  - {field: time, source: "https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf", certainty: independent, retrieved: primary, as_of: "2022-2024", tense: completed}
  - {field: current-status, source: "https://beenos.com/news-center/detail/20230907_bcr_pr/", certainty: vendor, retrieved: primary, as_of: "2023-07", tense: intended}
predictions:
  - {claim: "2025年の中国消費者による日本事業者からの越境EC購入額が2024年の2兆6,372億円を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "BEENOSグループの次回同種調査で、訪日後の旅アト・リピート購入経験がない海外顧客のうち、越境ECの利用意志があると回答する割合が2023年調査の43.7%を大きく下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    越境ECモール、国内事業者の越境対応サイト、海外マーケットプレイス、SNS・検索、決済、国際物流など複数の接点が関係する。ただし、調査は個別チャネルの寄与を特定していない。
channels: []
relations: []
sources:
  - https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf
  - https://beenos.com/news-center/detail/20230907_bcr_pr/
status: verified
updated: 2026-09-17
---

# 越境ECの拡大

## 見出している未来（何に向かって動いているか）

海外の消費者は、訪日旅行で気に入った日本の商品を、帰国後も越境ECを通じて買い続けたいという
意向を持っている。BEENOSグループ（越境EC購入サポート「Buyee」運営）が実施した「海外旅行
および訪日旅行における消費行動と越境ECに関するアンケート」（2023年7〜8月実施、アメリカ・
台湾・韓国・マレーシア・イギリスのBuyee利用者749名対象）では、訪日後に越境ECで現地の商品を
再購入した経験がある人は35.4％、経験が無い人のうち43.7％が「利用の意志はある」と回答した。
また、1年以内に訪日を予定しているユーザーは67％に上った。

これはBuyeeという越境EC事業者自身が実施した調査であり、同社の利用者に限定されている
（`vendor`）。海外消費者全体の意向を代表する数字ではない。同社の2025年1月公表の別調査
（1,345名対象）では、旅アト消費の経験者が44.0％（2023年の35.4％から8.6ポイント増）に
増えており、経験から実践への転換が進んでいる可能性がある。

## 足元の根拠（完了した事実）

日本・中国・米国の消費者が相互にオンラインで商品を購入する越境ECの取引額が増えている。経済産業省の2024年調査では、中国消費者による日本事業者からの購入額は2兆6,372億円で前年比8.5％増、米国消費者による日本事業者からの購入額は3兆1,397億円で前年比6.0％増だった。日本消費者による米国事業者からの購入額も2兆7,144億円で前年比7.3％増となっている。

これは日本の国内BtoC-EC全体ではなく、同調査が推計する日米中3か国間の消費者向けフローである。為替、国別の調査方法、商品カテゴリ、物流・関税の影響が混ざるため、海外売上や国内ECの成長率へそのまま置き換えない。

## kind と stage の判定

**kind: demand-shift とした。** 変化しているのは国境をまたぐ消費者の購入額であり、特定プラットフォームの広告機能の導入数ではない。

**stage: growing とした。** 2023年から2024年に、日米中3方向の推計取引額がいずれも増加したためである。ただし、3か国間フローに限った推計であり、すべての国・商品・事業者で同じ伸びが起きているとは言えない。

## 時間

同じ調査で日米中の比較ができる2022年以降を `2022~` とした。終点は `..`（継続中）。

## チャネルと伝播

越境ECモール、国内事業者の越境対応サイト、海外マーケットプレイス、SNS・検索、決済、国際物流など複数の接点が関係する。ただし、調査は個別チャネルの寄与を特定していない。

## 反証（これが偽なら何が観測されるか）

- 次回の同じ定義の推計で、日米中の複数フローが同時に減少する
- 取引額が増えても購入者数・注文数が増えず、為替や単価だけで見かけ上拡大していたと分かる
- 国別・商品別に見ると一部の大型取引だけが全体を押し上げ、越境ECの広がりが確認できない

## 未着手

- 2026年9月17日、BEENOSグループの2023年調査プレスリリースを実読して見出している未来を追記した。米国・中国を対象にした独立調査による同種の意向データは今回探せておらず、対象は米・台・韓・マレーシア・英に限られる
- 購入者数、注文数、客単価、商品カテゴリ、国別の内訳を同じ定義で比較する
- 為替・関税・物流費と取引額の変化を分けて確認する
- 2025年公表値で予測を答え合わせする
- 「利用の意志はある」43.7%が、実際の越境EC購入額の増加にどう転換したかを次回調査で確認する
