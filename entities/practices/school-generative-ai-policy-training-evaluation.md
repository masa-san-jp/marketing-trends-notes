---
id: practice/school-generative-ai-policy-training-evaluation
uri: urn:mtn:practice/school-generative-ai-policy-training-evaluation
type: practice
label_ja: 学校向け生成AIの利用方針・研修・出力確認・評価設計
label_en: School generative AI policy, training, output review, and evaluation design
authority:
  wikidata: null
  none_reason: "Wikidataで「学校向け生成AIの利用方針・研修・出力確認・評価設計」「school generative AI policy training evaluation」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: "学校教育向けの生成AIガイドライン公表後、利用条件と学習・校務の評価をつなぐ運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.mext.go.jp/content/20241226-mxt_shuukyo02-000030823_001.pdf", certainty: attested, retrieved: primary, as_of: "2024-12-26"}
channels: []
relations:
  - {type: responds_to, target: trend/school-generative-ai-governance, certainty: hypothesis, source: "https://www.mext.go.jp/zyoukatsu/ai/about.html"}
sources:
  - https://www.mext.go.jp/zyoukatsu/ai/
  - https://www.mext.go.jp/zyoukatsu/ai/about.html
  - https://www.mext.go.jp/content/20241226-mxt_shuukyo02-000030823_001.pdf
status: draft
updated: 2026-08-11
---

# 学校向け生成AIの利用方針・研修・出力確認・評価設計

## 何をするか

学校または教育委員会が、教職員の校務、児童生徒の学習、教材作成、保護者との連絡などの用途ごとに、利用目的、入力してよい情報、
人が確認する範囲、著作権・個人情報・利用規約の確認方法を決める。教職員・児童生徒・保護者に向けて、生成AIの仕組みと限界、誤りや
偏りの確認、出力の引用・提出ルール、問題発生時の相談先を研修する。

導入時は一つの校務または学習場面に限定して試行し、生成AIの出力をそのまま採用せず、事実確認、教材としての妥当性、発達段階への適合、
個人情報・著作権上の問題を確認する。評価は「AIを使ったか」ではなく、当初の学習目的や校務目的に対して、時間、成果物の品質、情報活用
能力、教員負担、インシデントがどう変わったかを、利用しない場合との比較可能な形で設計する。

文部科学省のVer.2.0ガイドラインは、学校現場での生成AI利用を一律に禁止・義務付けるものではなく、人間中心の利活用と情報活用能力の
育成強化を基本に、教職員、児童生徒、教育委員会ごとの留意点を整理している。文部科学省はパイロット校、研修教材、実証事業も掲載して
いるため、このpracticeではツール購入だけで終わらず、方針・研修・出力確認・評価を一つの運用にする。

## どのトレンドへの応答か

[trend/school-generative-ai-governance](../trends/school-generative-ai-governance.md)（学校教育における生成AI利用の制度化）への応答とみる。
公的ガイドラインが、利用の可否だけでなく、主体・場面ごとの留意点、情報活用能力、リスク対策、実証・研修を扱うようになったためである。
ただし、このpracticeを導入すれば学習成果、校務効率、教員負担、児童生徒の能力が改善するとは確認していないため、関係の確度は`hypothesis`とした。

## 成立条件・失敗条件

**効果未確認**:（対象事業で学校向け生成AIの方針策定、研修、出力確認、評価を運用していない）。学習成果、校務時間、教員負担、研修参加率、
出力修正率、個人情報・著作権のインシデントは測っていない。

成立条件は、学校または教育委員会に責任者と見直し期限があること、校務・学習ごとの入力情報と確認手順が決まっていること、教員・児童生徒・
保護者に対象別の研修と相談先があること、目的に合った評価指標と試行範囲があることである。生成AIの契約やアカウントを用意するだけ、
または出力の正確性を確認せず教材・評価に使うだけでは、このpracticeの実装とはみなせない。

**未確認**: 学校・教育委員会の導入率、用途別の研修実施率、出力修正率、学習成果・校務時間・教員負担への影響、個人情報・著作権・誤情報に
関するインシデント率。

## 飽和度の判定

`spreading` とした。ガイドライン、チェック項目、パイロット校、研修教材、実証事業が整備され、学校が運用設計を検討できる段階にある。
一方、自治体・学校横断の採用率、評価指標、運用品質、費用対効果は比較できていないため、`commoditized`とは判定しない。

## 利用上の注意

**効果未確認**: 学校向け教材・研修・SaaSを提供する場合は、まず一つの利用場面に限定し、利用方針、入力情報の境界、出力確認ルーブリック、
教員向け研修、児童生徒・保護者への説明、問題発生時の連絡経路を一枚の運用表にする。試行前後で目的に沿った時間・品質・問い合わせ・
インシデントを記録し、学習成果や校務効率の効果は測定できた範囲だけで判断する。外部資料では現時点でこのpracticeを試す学校事業がないため、
効果の主張は置かない。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
