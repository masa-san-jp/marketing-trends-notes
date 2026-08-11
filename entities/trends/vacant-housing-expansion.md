---
id: trend/vacant-housing-expansion
uri: urn:mtn:trend/vacant-housing-expansion
type: trend
kind: demand-shift
stage: growing
market: consumer-goods
geo: japan
label_ja: 空き家の増加
label_en: Expansion of vacant housing in Japan
authority:
  wikidata: null
  none_reason: "「空き家の増加」「vacant housing expansion in Japan」で検索したが、日本の住宅・土地統計に基づく空き家の変化そのもののWikidata項目は確認できない"
time:
  start: "1993~"
  end: ".."
  display: "総住宅数が増える中で空き家が過去最多となり、管理・流通・改修・地域活用の課題が拡大する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 空き家数の増加
  note: "「空き家の増加」は、総務省統計局の住宅・土地統計調査を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "2023"}
  - {field: stage, source: "https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "1993-2023"}
  - {field: time, source: "https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "1978-2023"}
predictions:
  - {claim: "次回の住宅・土地統計調査で空き家率が2023年の13.8％を下回らない", by: "2029-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/jyutaku/index.htm
  - https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf
status: verified
updated: 2026-08-12
---

# 空き家の増加

## 何が変わったか

住宅ストックが増える一方、居住者のいない住宅が増え、管理、相続、賃貸・売却、改修、解体、地域活用を別々に扱えない課題になっている。2023年の住宅・土地統計調査では、空き家は900万2千戸で過去最多、空き家率は13.8％で過去最高となった。空き家数は1993年から2023年までの30年間で約2倍に増えた。

賃貸・売却用および二次的住宅を除く空き家は385万6千戸で、2018年より36万9千戸増加した。空き家数の増加は直ちに流通可能な住宅や改修需要を意味せず、所有者不明、老朽化、立地、権利関係によって活用可能性は異なる。

## kind と stage の判定

**kind: demand-shift とした。** 住宅ストックと居住世帯のずれが広がる人口・世帯構造の変化を観測しており、単一の住宅サービスの導入ではないためである。

**stage: growing とした。** 空き家数と空き家率が過去最高を更新し、非流通空き家も増えているためである。ただし、地域差と物件状態が大きく、全国一律の市場としてpeakとは判定しない。

## 時間

1993年から2023年まで一貫した増加が示されるため `1993~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

相続、自治体の空き家対策、不動産仲介、賃貸、リフォーム、解体、住宅ローン、地域交通、見守りを通じて、住宅と地域サービスへ伝わる。空き家の解消が地域の人口回復や不動産価格を改善する因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 空き家の増加が続くなら、次回調査で空き家数・空き家率が大きく減少することはないはず
- 空き家が事業機会になるなら、管理契約、流通、改修、解体、活用の件数が地域別に増えるはず
- 非流通空き家の増加が問題の中心なら、賃貸・売却用と分けても増加が確認されるはず

## 未着手

- 所有関係、種類、築年、地域、管理状態、相続、流通可能性を分解する
- 管理、改修、解体、賃貸、売却、地域活用の案件化率と費用を追う
- 次回の住宅・土地統計調査で予測を答え合わせする
