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
  - {field: kind, source: "https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "2023", tense: completed}
  - {field: stage, source: "https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "1993-2023", tense: completed}
  - {field: time, source: "https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "1978-2023", tense: completed}
  - {field: current-status, source: "https://www.mlit.go.jp/report/press/content/001907491.pdf", certainty: independent, retrieved: primary, as_of: "2024", tense: intended}
predictions:
  - {claim: "次回の住宅・土地統計調査で空き家率が2023年の13.8％を下回らない", by: "2029-12", resolved: null, outcome: null}
  - {claim: "国土交通省の次回の空き家所有者実態調査で、使用目的のない空き家の所有世帯のうち「空き家として所有しておく」意向の割合が令和6年調査の約41%を大きく下回らない", by: "2029-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    相続、自治体の空き家対策、不動産仲介、賃貸、リフォーム、解体、住宅ローン、地域交通、見守りを通じて、住宅と地域サービスへ伝わる。空き家の解消が地域の人口回復や不動産価格を改善する因果は未確認である。
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/jyutaku/index.htm
  - https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf
  - https://www.mlit.go.jp/report/press/content/001907491.pdf
status: verified
updated: 2026-09-16
---

# 空き家の増加

## 見出している未来（何に向かって動いているか）

使用目的のない空き家の所有者の多くは、今後5年間程度のうちに、空き家をそのまま所有し続ける
方向へ向かっている。国土交通省「令和6年空き家所有者実態調査結果」（令和7年8月公表、対象は
現在も空き家であると回答した住宅N=1,034千世帯）では、今後の利用意向について、「使用目的の
ない空き家」の所有世帯では「空き家として所有しておく」意向の割合が約41％と最も高く、次いで
「売却する」と「取り壊してさら地にする」がともに約2割ずつだった。空き家全体（種類を問わない）
では「空き家として所有しておく」が約32％、「売却する」が約20％、「別荘やセカンドハウスなど
として利用する」が約19％だった。

取得方法別では、相続により取得した世帯のうち「相続前に対策を講じていない」場合は「空き家と
して所有しておく」意向が約35％と、「相続前に対策を講じた」場合の約23％より高い。これは、
相続前の準備の有無が、その後の利用意向（放置か流通かの選択）に結びつくことを示唆する。

これは所有者の意向調査であり、実際に空き家が今後5年間でどう処分・活用されるかを保証するもの
ではない。

## 足元の根拠（完了した事実）

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

- 2026年9月16日、国土交通省「令和6年空き家所有者実態調査結果」（令和7年8月公表）を実読して見出している未来を追記した。図表の一部（今後の利用意向の種類別・取得方法別クロス集計の細目）は列と数値の対応が崩れており、本文の記述文からのみ数値を採用した
- 所有関係、種類、築年、地域、管理状態、相続、流通可能性を分解する
- 管理、改修、解体、賃貸、売却、地域活用の案件化率と費用を追う
- 次回の住宅・土地統計調査で予測を答え合わせする
- 「空き家として所有しておく」という意向が、次回の空き家所有者実態調査で実際に維持され続けるか、それとも売却・除却が進むかを追う
