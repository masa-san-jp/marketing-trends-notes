---
id: trend/algorithmic-trust-erosion
uri: urn:mtn:trend/algorithmic-trust-erosion
type: trend
label_ja: おすすめ表示・アルゴリズムへの不信感の高まり
label_en: Rising distrust in algorithmic content curation
authority:
  wikidata: null
  none_reason: "「アルゴリズム不信」「algorithmic curation distrust Japan」で検索したが、この生活者の意識そのもののWikidata項目は確認できない（2026-09-16検索実施）"
time:
  start: "2025~"
  end: ".."
  display: "消費者庁 令和7年度消費者意識基本調査（2025年11月調査、2026年6月公表）で観測できる局面"
kind: demand-shift
stage: emerging
market: cross-category
geo: japan
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: インターネットの表示に関する意識
  note: "「おすすめ表示・アルゴリズムへの不信感の高まり」は、消費者庁の設問「インターネット上では、あなた向けの情報が優先的に表示されたり、『おすすめ』が表示されたりします」への回答を要約する記述的なラベル。生活者がこの複合語を自称するかは確認していない"
freshness:
  valid_as_of: "2026-09-16"
  recheck_by: "2026-10-16"
evidence:
  - {field: kind, source: "https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_260612_15.pdf", certainty: independent, retrieved: primary, as_of: "2025-11", tense: intended}
  - {field: stage, source: "https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_260612_15.pdf", certainty: independent, retrieved: primary, as_of: "2025-11", tense: intended}
  - {field: time, source: "https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_260612_14.pdf", certainty: independent, retrieved: primary, as_of: "2025-11", tense: completed}
  - {field: current-status, source: "https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_260612_15.pdf", certainty: independent, retrieved: primary, as_of: "2026-06-12", tense: completed}
predictions:
  - {claim: "消費者庁の次回（令和8年度）消費者意識基本調査で、「関心を引くために根拠のない情報、虚偽の情報が混ざっていると感じる」に当てはまると回答する割合が、令和7年度調査の68.6%を大きく下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "同調査で、「自分の情報が必要以上に収集されていると感じる」に当てはまると回答する割合が、令和7年度調査の56.1%を大きく下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    検索・SNS・EC・動画などインターネット上のあらゆる「おすすめ」表示・パーソナライズ機能が対象で、
    特定のチャネルの発生現象ではないため `channels` は張らない。
    **未確認**: この不信感が、特定のプラットフォーム（検索・SNS・EC）でどう違うか。
channels: []
relations: []
sources:
  - https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/
  - https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_260612_14.pdf
  - https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_260612_15.pdf
status: verified
updated: 2026-09-16
---

# おすすめ表示・アルゴリズムへの不信感の高まり

## 見出している未来（何に向かって動いているか）

インターネット利用者は、パーソナライズされた表示・「おすすめ」に対して、便利さよりも不信感を
強く感じており、透明性の低いアルゴリズム表示から距離を置きたいという方向を見せている。消費者庁の
令和7年度消費者意識基本調査（2025年11月10日〜26日実施、2026年6月12日公表）は、インターネット上の
パーソナライズ表示に関する意識を9項目で尋ねている。「当てはまる」（「とても当てはまる」＋
「ある程度当てはまる」）の割合は、「関心を引くために根拠のない情報、虚偽の情報が混ざっていると
感じる」が68.6%と最も高く、次いで「自分の情報が必要以上に収集されていると感じる（位置情報・履歴・
趣味嗜好など）」が56.1%、「自分に合った情報ではなく、他者の都合で情報が表示されていると感じる」が
50.6%だった。

一方、「当てはまらない」（＝おすすめ表示を肯定的に評価しない）の割合は、「『おすすめ』が表示される
ことで欲しいものを探す手間が省けていると感じる」が53.8%と最も高く、次いで「関心を引く情報が
提供されるため、視聴時間をコントロールできていないと感じる」に当てはまらないが51.6%だった。
これは、パーソナライズの利便性を実感する人よりも、その仕組みへの不信・懸念を持つ人の方が多いことを
示している。この意識は、生活者が今後どのような情報環境を求めるか（透明性、選択の主導権、
根拠のある情報）という方向性を示す先行指標として扱う。

## 足元の根拠（完了した事実）

**未確認**: 同一設問による過去の調査結果（経年比較）は、今回の調査環境では原典に到達・確認できて
いない。したがって、この不信感が「高まっている」かどうかは今回の1時点のデータからは判断できず、
令和7年度時点の断面値として置く。関連する既存 trend `trend/tracking-restrictions` は、GDPR・ATT・
WebKit・Privacy Sandbox 等の**供給側・規制側の技術的制約の常態化**を扱っており、本 trend が扱う
**生活者側の心理的な不信感**とは別の主張である。

## kind と stage の判定

**kind: demand-shift とした。** パーソナライズ・レコメンド機能という既存の技術基盤そのものの
ローンチが起点ではなく、その技術に対する生活者側の意識変化を、利害のない消費者庁の独立調査が
示しているためである。特定のベンダーが売り込んだ括りでもない。

**stage: emerging とした。** 不信感を示す割合自体は5〜7割に達しているが、経年での変化を示す
独立した時系列データがまだ確認できておらず、一般化した peak と判定する根拠は無い。

## 時間

始点は、この意識を確認できた `2025~`（令和7年度調査の実施年）とした。これは現象の始まりではなく、
今回確認できた観測時点である。終点は `..`（継続中）。

## チャネルと伝播

検索・SNS・EC・動画などインターネット上のあらゆる「おすすめ」表示・パーソナライズ機能が対象で、
特定のチャネルの発生現象ではないため `channels` は張らない。**未確認**: この不信感が、特定の
プラットフォーム（検索・SNS・EC）でどう違うか。

## 反証（これが偽なら何が観測されるか）

- 次回の消費者庁調査で「虚偽情報が混ざっている」「必要以上に情報収集されている」の割合が
  大きく低下し、不信感が一時的なものだったと分かる
- 不信感の水準が高いにもかかわらず、実際のパーソナライズ機能のオプトアウト率・プライバシー
  設定の変更率に変化が見られない（意識だけが先行し、行動に反映されていない可能性）
- 「おすすめ」表示の利便性を評価する回答が次回調査で明確に上回り、不信感より利便性評価が
  優勢になる

## 未着手

- 2026年9月16日、消費者庁の令和7年度消費者意識基本調査（2026年6月12日公表）の「2 調査結果の概要」
  PDFを実読して確認した。過去年度の同一設問による経年比較は、今回の調査環境では確認できていない
- この不信感が、実際のプライバシー設定変更・広告オプトアウト・特定プラットフォームの利用時間に
  結びついているかを確認する
- 年齢層・性別・利用頻度別の不信感の差を確認する
- 応答する practice（表示の透明性向上、パーソナライズの説明可能性、選択導線の設計）の採用状況を
  確認する
