---
id: trend/creator-ad-disclosure
uri: urn:mtn:trend/creator-ad-disclosure
type: trend
kind: regulation-driven
stage: emerging
market: creator-economy
geo: japan
label_ja: クリエイター広告表示の可視化
label_en: Creator advertising disclosure becoming visible
authority:
  wikidata: null
  none_reason: "Wikidataで「インフルエンサー広告表示」「クリエイターエコノミー」を確認したが、広告表示の可視化という日本の現象そのものの項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: 令和5年10月1日のステマ規制施行以降
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: null
  note: "「クリエイター広告表示の可視化」は、規制と消費者調査で観測される変化を要約するための記述的なラベル。原資料の固有名称ではない"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-09-12"
evidence:
  - {field: kind, source: "https://www.caa.go.jp/policies/policy/representation/fair_labeling/stealth_marketing/", certainty: attested, retrieved: primary, as_of: "2023-10-01"}
  - {field: stage, source: "https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_240614_15.pdf", certainty: independent, retrieved: primary, as_of: "2023-11"}
  - {field: time, source: "https://www.caa.go.jp/policies/policy/representation/fair_labeling/stealth_marketing/", certainty: attested, retrieved: primary, as_of: "2023-10-01"}
predictions:
  - {claim: "次回以降の消費者庁調査または同等の独立調査で、インフルエンサー投稿の広告表示を見た経験と、表示を信頼判断に使う割合が再計測される", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.caa.go.jp/policies/policy/representation/fair_labeling/stealth_marketing/
  - https://www.caa.go.jp/policies/policy/consumer_research/research_report/survey_002/assets/consumer_research_cms201_240614_15.pdf
status: verified
updated: 2026-08-12
---

# クリエイター広告表示の可視化

## 何が変わったか

インフルエンサーや著名人の投稿を広告として扱うとき、広告であることを隠さず、受け手が広告主の関与を
判別できるようにすることが、クリエイターを使ったマーケティングの実務要件として浮上した。

消費者庁は、広告であることを隠すステルスマーケティングについて、インフルエンサー等の第三者に企業が
依頼・指示する投稿も対象に含め、2023年10月1日から景品表示法違反として規制している。

同庁の令和5年度「消費者意識基本調査」（2023年11月調査、インターネット利用者4,439人）では、著名人や
インフルエンサーの投稿で「PR」「広告」等の表示を「見たことがある」が43.7％だった。そのうち表示を見た
1,941人では、広告であることを明示する投稿者を、明示しない投稿者より信頼できると答えた割合が63.0％だった。
この調査は表示の増加率や投稿全体に占める表示率を測っていないため、広告表示が増えたことや、表示が売上を
高めることまでは言えない。

## kind と stage の判定

**kind: regulation-driven とした。** 消費者の認知だけを見れば需要側の変化にも見えるが、このテーマの成立条件は
2023年10月1日のステマ規制である。広告主が関与する第三者投稿を、広告であると判別しにくい表示として規制する
制度変更が先にあり、クリエイターを使う広告実務の表示要件を変えた。

**stage: emerging とした。** 独立調査で、表示を見た経験と表示者への信頼判断は観測できる。一方で、同じ設問の
経年値、広告表示の実施率、規制後の違反・是正の推移はこの確認では取れていない。したがって「一般化した」と
断定せず、規制後の実務変化が測定され始めた段階に留める。

## 時間

始点は、ステマ告示が施行された2023年10月1日を含む `2023~` とした。これはクリエイター広告の始まりではなく、
広告表示を隠すことが法的な問題になった時点である。終点は `..`（継続中）。

## チャネルと伝播

特定のプラットフォームの機能ではなく、インフルエンサー等の第三者投稿に横断的に適用される表示要件なので、
発生・伝播チャネルは特定しない。消費者庁の説明もSNS投稿だけでなく、レビュー投稿、テレビ、新聞、ラジオ、
雑誌等を対象に含めている。

## 反証（これが偽なら何が観測されるか）

- クリエイター広告の表示可視化が実務上の変化でないなら、規制後の独立調査で「PR」「広告」表示を見た経験と、
  表示の有無を信頼判断に使う割合が、継続してごく小さいままになるはず
- 規制が表示要件を変えていないなら、広告主が関与する第三者投稿について、広告であることを明示する運用への
  移行や、表示不備に関する行政対応が観測されないはず
- 「表示が信頼を生む」という解釈が偽なら、表示を見た人のうち明示する投稿者を信頼できると答える割合が、
  明示しない投稿者を信頼できると答える割合を上回らないはず

## 未着手

- 2026年8月12日時点の消費者庁の現行ページを確認したが、同じ設問による新しい独立調査は確認できず、2023年調査の基準値を維持する
- 令和6年度・令和7年度の消費者庁調査で同じ設問が継続されているかを確認し、経年変化を取る
- 規制施行後の行政処分・情報提供件数と、事業者側の表示管理の実務を一次資料で確認する
- プラットフォームごとの表示機能・審査・保存要件は、各社の一次仕様を読んでから分ける
- 応答するpractice（表示管理、案件審査、クリエイター契約等）の採用率と、表示が成果に与える影響を確認する
