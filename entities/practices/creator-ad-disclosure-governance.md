---
id: practice/creator-ad-disclosure-governance
uri: urn:mtn:practice/creator-ad-disclosure-governance
type: practice
label_ja: クリエイター案件の広告表示管理
label_en: Creator campaign ad disclosure governance
authority:
  wikidata: null
  none_reason: "Wikidataで「クリエイター案件の広告表示管理」「creator advertising disclosure governance」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: 令和5年10月1日のステマ規制施行以降
saturation: spreading
evidence:
  - {field: time, source: "https://www.caa.go.jp/policies/policy/representation/fair_labeling/faq/stealth_marketing/", certainty: attested, retrieved: primary, as_of: "2023-10-01"}
channels: []
relations:
  - {type: responds_to, target: trend/creator-ad-disclosure, certainty: hypothesis, source: "https://www.caa.go.jp/policies/policy/representation/fair_labeling/faq/stealth_marketing/"}
sources:
  - https://www.caa.go.jp/policies/policy/representation/fair_labeling/stealth_marketing/
  - https://www.caa.go.jp/policies/policy/representation/fair_labeling/faq/stealth_marketing/
status: draft
updated: 2026-08-11
---

# クリエイター案件の広告表示管理

## 何をするか

企業がインフルエンサー等に依頼する投稿を、依頼・報酬・内容への関与の有無で案件として判定し、案件に当たる
場合は、投稿・動画の受け手が広告であると判別できる表示を、公開前に確認する運用である。広告主側が、依頼内容、
表示方法、公開後の修正・削除依頼の記録を案件単位で残す。

消費者庁のQ&Aでは、規制対象は原則として表示内容の決定に関与した広告主であり、依頼を受けたインフルエンサー
自身は原則として規制対象外とされている。表示を明瞭にする方法として「広告」「宣伝」「プロモーション」「PR」
などが挙げられている。投稿本文・動画内で広告であることが分かるかを確認する、という広告主側の管理に落とす。

## どのトレンドへの応答か

[trend/creator-ad-disclosure](../trends/creator-ad-disclosure.md)（クリエイター広告表示の可視化）への応答とみる。
ステマ規制が広告主の表示管理を求め、消費者調査では表示を見た人の63.0％が広告であることを明示する投稿者を
信頼できると回答している。ただし、表示管理が信頼や売上を高める因果はこの資料では検証されていないため、
関係の確度は`hypothesis`とした。

## 効いた条件・効かない条件

**未実施**（自分の事業で案件管理を試していない）。表示の有無が信頼・成果に与える効果も測っていない。

この型が成立する条件は、広告主が第三者の投稿内容の決定に関与しているかを案件ごとに把握できること、対象投稿の
公開場所と表示方法を事前に確認できることである。企業の依頼に応じない自主的な投稿は、消費者庁Q&A上、事業者の
表示に当たらず「PR」等の表示は必要ないため、すべての言及を広告扱いする運用は過剰になりうる。

**未確認**: 表示方法ごとの消費者理解、表示確認の工数、修正依頼が投稿成果に与える影響。

## 飽和度の判定

`spreading` とした。規制とQ&Aが公開され、広告主が案件管理に落とせる明示的なルールがあるため、運用の型は
広がり得る段階にある。ただし、広告主・代理店・クリエイターの採用率や、表示不備の発生率を示す独立した数字は
確認していないため、`commoditized`とは判定しない。

## 自分の事業にどう使うか

**未実施。** 試すなら、案件台帳に「広告主の関与」「表示文言」「掲載箇所」「公開後確認日」を記録し、表示漏れ
だけでなく、投稿の保存・修正履歴も確認できる最小運用から始める。法的な適否の最終判断は、案件の具体的な関与関係
と媒体仕様を確認して行う。
