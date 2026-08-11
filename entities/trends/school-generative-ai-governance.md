---
id: trend/school-generative-ai-governance
uri: urn:mtn:trend/school-generative-ai-governance
type: trend
kind: regulation-driven
stage: growing
market: education
geo: japan
label_ja: 学校教育における生成AI利用の制度化
label_en: Institutionalization of generative AI use in school education
authority:
  wikidata: null
  none_reason: "Wikidataで「学校教育における生成AI利用の制度化」「institutionalization of generative AI use in school education」を確認したが、この政策・運用の変化そのものの項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: "2023年の暫定ガイドラインから2024年12月のVer.2.0改訂以降"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 学校現場における生成AIの利活用
  note: "学校関係者が自称する市場カテゴリではなく、文部科学省のガイドラインと実証事業の積み上がりをこのKBでまとめた名称"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mext.go.jp/a_menu/other/mext_02412.html?s=03", certainty: attested, retrieved: primary, as_of: "2024-12-26"}
  - {field: time, source: "https://www.mext.go.jp/content/20241226-mxt_shuukyo02-000030823_001.pdf", certainty: attested, retrieved: primary, as_of: "2024-12-26"}
  - {field: stage, source: "https://www.mext.go.jp/zyoukatsu/ai/", certainty: attested, retrieved: primary, as_of: "2026-08-11"}
channels: []
relations: []
sources:
  - https://www.mext.go.jp/zyoukatsu/ai/
  - https://www.mext.go.jp/zyoukatsu/ai/about.html
  - https://www.mext.go.jp/a_menu/other/mext_02412.html?s=03
  - https://www.mext.go.jp/content/20241226-mxt_shuukyo02-000030823_001.pdf
status: verified
updated: 2026-08-11
---

# 学校教育における生成AI利用の制度化

## 何が変わったか

文部科学省は2023年7月に初等中等教育段階の生成AI利用に関する暫定的なガイドラインを公表し、2024年12月26日にVer.2.0へ改訂した。
Ver.2.0は、生成AIを一律に禁止・義務付けるものではなく、人間中心の利活用と情報活用能力の育成強化を基本に、教職員の校務利用、
児童生徒の学習活動、教育委員会の役割ごとに留意点を整理している。

教職員の校務では、仕組みや特徴を理解し、生成内容の適切性を判断できる範囲で活用する前提が示される。一方、児童生徒の学習では、
発達段階と情報活用能力に留意し、リスクや懸念への対策を講じた上で利用を検討する整理になっている。文部科学省はガイドラインに加え、
生成AIパイロット校、研修教材、実証事業を掲載しており、学校での利用を「ツールを導入するか」だけでなく、学習目的、情報モラル、
著作権、個人情報、出力確認、評価方法を含む運用条件として扱い始めている。

これは学校向け生成AIサービスの普及率や学力向上を示すトレンドではない。公的なガイドラインと実証・研修の積み上がりが、教育現場で
生成AIを検討する際の判断条件を制度・運用の側から具体化している変化である。

## kind と stage の判定

**kind: regulation-driven とした。** 法律による一律の義務ではないが、文部科学省のガイドライン改訂、教育委員会向けの通知、パイロット校と
研修の枠組みが、学校教育における生成AI利用の条件を先に定義しているためである。生成AIサービスの機能追加だけを起点とする
`tech-enabled`とは区別する。

**stage: growing とした。** 2023年の暫定版から2024年のVer.2.0へ更新され、2025年以降も研修、パイロット校、教育分野特化の実証事業が
継続している。一方、自治体・学校別の採用率、授業・校務での利用頻度、学習成果、教員負担の比較データは揃っていないため、peakや
commoditizedとは判定しない。

## 時間

始点は暫定ガイドラインが公表された `2023~` とした。これは生成AI技術の登場時点ではなく、学校教育での利用条件が公的資料として整理され
始めた観測時点である。終点は `..`（継続中）。

## チャネルと伝播

特定の広告・SNSチャネルから広がった変化ではなく、文部科学省のガイドライン、教育委員会向け通知、パイロット校、教員研修、授業・校務の
実証を通じて伝わる。したがって `channels` は張らない。**未確認**: 学校向けサービスの選定、教員コミュニティ、教材・研修事業者、保護者への
説明など、どの接点が実際の導入判断に影響したか。

## 反証（これが偽なら何が観測されるか）

- 学校教育における生成AI利用の制度化が進んでいないなら、2024年のガイドライン改訂後にパイロット校、研修、実証事業が継続して増えないはず
- 利用条件が学校の実務を変えているなら、教育委員会・学校の利用方針、教員研修、学習活動での利用場面が同じ定義で追跡できるはず
- 学習や校務への効果まで生じているなら、独立した評価で学習成果、教員負担、情報活用能力、インシデントの変化が確認されるはず

## 未着手

- 2024年度以降の生成AIパイロット校と教育分野特化の実証事業を、自治体・校種・用途別に整理する
- 学校・教育委員会の生成AI利用方針、教員研修、児童生徒の学習利用、保護者説明の実装率を同じ定義で確認する
- 学習成果、教員負担、情報モラル、個人情報・著作権に関するインシデントを、導入前後で比較できる独立評価を探す
- このtrendに応答するpractice（学校向け生成AIの利用方針・研修・出力確認・評価設計をつなぐ運用）の採用率と実績を整理する
