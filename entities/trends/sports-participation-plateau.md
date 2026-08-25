---
id: trend/sports-participation-plateau
uri: urn:mtn:trend/sports-participation-plateau
type: trend
kind: demand-shift
stage: peak
market: health-wellness
geo: japan
label_ja: スポーツ実施率の高原化と世代差
label_en: Plateauing sports participation with generational gaps
authority:
  wikidata: null
  none_reason: "「スポーツ実施率の高原化と世代差」「sports participation plateau Japan」で検索したが、日本の実施率の横ばいと世代差の組み合わせそのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: "週1日以上のスポーツ実施率が約52％で横ばいとなり、働き盛り世代・男女差が残る局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 成人スポーツ実施率の横ばいと実施格差
  note: "「スポーツ実施率の高原化と世代差」は、スポーツ庁の世論調査を要約する記述的なラベルで、参加者が自称する名称ではない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2027-02-10"
evidence:
  - {field: kind, source: "https://www.mext.go.jp/sports/b_menu/houdou/jsa_00234.html", certainty: independent, retrieved: primary, as_of: "2025年度"}
  - {field: stage, source: "https://www.mext.go.jp/sports/b_menu/houdou/jsa_00234.html", certainty: independent, retrieved: primary, as_of: "2022-2025年度"}
  - {field: time, source: "https://www.mext.go.jp/sports/b_menu/houdou/jsa_00234.html", certainty: independent, retrieved: primary, as_of: "2022-2025年度"}
predictions:
  - {claim: "次回のスポーツ庁調査で20歳以上の週1日以上のスポーツ実施率が2025年度の51.7％を下回らない", by: "2028-03", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    ジム・教室・競技場、学校・職場、家庭内運動、動画・アプリ、地域イベント、スポーツ観戦など複数の接点がある。実施率の差を生むチャネル別の因果は未確認である。
channels: []
relations: []
sources:
  - https://www.mext.go.jp/sports/b_menu/houdou/jsa_00234.html
status: verified
updated: 2026-08-11
---

# スポーツ実施率の高原化と世代差

## 何が変わったか

成人の運動・スポーツ実施は一定規模に広がった一方、週1日以上の実施率は高原状態にあり、世代・性別による差が残っている。スポーツ庁の2025年度調査では、20歳以上の週1日以上の実施率は51.7％で、2022年以降ほぼ横ばいとされた。男性は55.0％、女性は48.8％で、20代から50代の子育て・働き盛り世代は引き続き低い傾向にある。

これは「運動需要が全面的に伸びている」ことを意味しない。時間制約、仕事、子育て、費用、場所、身体状態などが参加を分けるため、健康サービスやスポーツ商品の市場を一つの平均値だけで設計しない。

## kind と stage の判定

**kind: demand-shift とした。** スポーツをする頻度と時間という生活行動を測っており、特定施設やブランドの広告効果を測る統計ではない。

**stage: peak とした。** 週1日以上の実施率は約52％で主流層を形成し、2022年以降は高原状態にある。一方、国の目標である70％程度には達しておらず、働き盛り世代など未充足の差が残るため、需要が消えたという意味ではない。

## 時間

同じ調査系列で横ばいが確認できる2022年以降を `2022~` とした。終点は `..`（継続中）。

## チャネルと伝播

ジム・教室・競技場、学校・職場、家庭内運動、動画・アプリ、地域イベント、スポーツ観戦など複数の接点がある。実施率の差を生むチャネル別の因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回以降の調査で実施率が大きく上昇し、横ばいではなく明確な成長局面へ移る
- 働き盛り世代と女性の実施率差が縮小せず、利用機会の設計が需要に届いていないと分かる
- 週あたり実施時間や継続者割合が低下し、平均実施率だけでは実態を表せないと確認される

## 未着手

- 種目、場所、費用、頻度、継続年数、年齢、性別、就業・子育て状況を分解する
- スポーツ用品、施設、アプリ、動画、イベントの利用実績と参加率を接続する
- 次回調査で予測を答え合わせする
