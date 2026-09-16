---
id: trend/single-person-household-expansion
uri: urn:mtn:trend/single-person-household-expansion
type: trend
kind: demand-shift
stage: growing
market: consumer-goods
geo: japan
label_ja: 単独世帯の拡大
label_en: Expansion of single-person households
authority:
  wikidata: null
  none_reason: "「単独世帯の拡大」「single-person household expansion」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2005~"
  end: ".."
  display: 2005年から2020年にかけて単独世帯数と構成比が上昇した局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 単独世帯の増加
  note: "「単独世帯の拡大」は、国勢調査の家族類型別世帯数を要約するための記述的なラベル。世帯主がこの語を自称することは確認していない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2005-2020", tense: completed}
  - {field: stage, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2020", tense: completed}
  - {field: time, source: "https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf", certainty: independent, retrieved: primary, as_of: "2005-2020", tense: completed}
  - {field: current-status, source: "https://www.ipss.go.jp/ps-doukou/j/doukou16/JNFS16gaiyo.pdf", certainty: independent, retrieved: primary, as_of: "2021", tense: intended}
predictions:
  - {claim: "2025年国勢調査の家族類型別集計でも単独世帯の構成比が2020年の38.1%を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "国立社会保障・人口問題研究所の次回（第17回）出生動向基本調査で、18〜34歳未婚者のうち「一生結婚するつもりはない」と回答する割合が第16回調査（2021年、男性17.3%・女性14.6%）を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定チャネルから発生した変化ではない。家族形成、人口構成、居住形態などの社会構造が、食品、日用品、住居、金融、外食などの需要単位に影響しうる。ただし、カテゴリ別の影響は別の統計で確認する必要がある。
channels: []
relations: []
sources:
  - https://www.stat.go.jp/data/kokusei/2020/kekka/pdf/outline_01.pdf
  - https://www.ipss.go.jp/ps-doukou/j/doukou16/JNFS16gaiyo.pdf
status: verified
updated: 2026-09-16
---

# 単独世帯の拡大

## 見出している未来（何に向かって動いているか）

18〜34歳の未婚者は、結婚をより不確実なもの・より遠いものとして見るようになっている。国立
社会保障・人口問題研究所「第16回出生動向基本調査」（独身者調査、2021年実施、18〜34歳未婚者
対象、男性n=2,033・女性n=2,053）では、「いずれ結婚するつもり」と考えている未婚者の割合が、
男性81.4％（前回・第15回調査2015年は85.7％）、女性84.3％（同89.3％）と、男女とも前回から
減少した。一方、「自分の一生を通じて考えた場合」の設問に「一生結婚するつもりはない」と答え
た未婚者は、男性17.3％、女性14.6％で、2000年代に入って増加傾向が続いている。

結婚意思を持つ未婚者の中でも、「理想的な相手が見つかるまでは結婚しなくてもかまわない」と
考える割合が前回調査より高まり、男性48.6％、女性51.7％となった。これは、結婚の時期を「年齢」
ではなく「相手次第」に委ねる意向が強まっていることを示す。

これらは18〜34歳という特定年齢層の結婚に対する意向調査であり、単独世帯の構成比そのものの
予測ではない。ただし、結婚意向の低下・後ろ倒しは、若年層の単独世帯としての生活期間が延びる
方向と整合する。

## 足元の根拠（完了した事実）

日本の一般世帯に占める単独世帯の数と比率が上昇している。
総務省統計局の2020年国勢調査では、単独世帯は2,115万1,042世帯で、一般世帯の38.1％を占めた。2015年と比べて単独世帯数は14.8％増え、構成比も34.6％から38.1％へ上昇している。2005年から2020年の系列でも、単独世帯の構成比は29.5％、32.4％、34.6％、38.1％と上昇している。

これは世帯単位で商品・サービスの需要を考えるときに、家族世帯の平均だけでは捉えにくい生活単位が増えていることを示す。ただし、単独世帯が増えたことだけから、特定の商品カテゴリや購買チャネルの伸長までは言えない。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は世帯構成という需要側の基盤変化であり、広告施策や制度の導入ではない。

**stage: growing とした。** 2005年から2020年に単独世帯の実数と構成比が連続して増加している。2025年国勢調査の詳細な家族類型別集計がまだ揃っていないため、直近の伸び率は未確認として残す。

## 時間

国勢調査で同じ家族類型の系列を比較できる2005年から `2005~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定チャネルから発生した変化ではない。家族形成、人口構成、居住形態などの社会構造が、食品、日用品、住居、金融、外食などの需要単位に影響しうる。ただし、カテゴリ別の影響は別の統計で確認する必要がある。

## 反証（これが偽なら何が観測されるか）

- 2025年国勢調査の家族類型別集計で単独世帯の構成比が38.1％を下回る
- 単独世帯の実数・構成比が次回以降の公的統計で減少する
- 単独世帯の増加が統計上の分類変更による見かけだけだと判明する

## 未着手

- 2026年9月16日、国立社会保障・人口問題研究所「第16回出生動向基本調査」の独身者調査結果概要を実読して見出している未来を追記した。本調査は18〜34歳の未婚者に限定されるため、単独世帯全体（高齢単身世帯を含む）の意向を代表しない
- 2025年国勢調査の家族類型別詳細集計で予測を答え合わせする
- 単独世帯の年齢・性別・地域構成と、カテゴリ別支出の違いを接続する
- 単独世帯の増加が購買頻度、容量、配送、外食、サブスクリプションにどう影響したかを独立統計で分解する
- 結婚意向の低下・後ろ倒しが、実際の生涯未婚率・単独世帯構成比にどう反映されるかを次回の出生動向基本調査・国勢調査で確認する
