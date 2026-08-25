---
id: practice/giga-device-network-lifecycle
uri: urn:mtn:practice/giga-device-network-lifecycle
type: practice
label_ja: GIGA端末・ネットワーク・学習基盤のライフサイクル運用
label_en: GIGA device, network, and learning-platform lifecycle operations
authority:
  wikidata: null
  none_reason: "Wikidataで「GIGA端末・ネットワーク・学習基盤のライフサイクル運用」「GIGA device network and learning-platform lifecycle operations」を確認したが、この自治体・学校向け運用の型そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "GIGA第2期で、端末・ネットワーク・クラウド学習環境を更新し、故障・接続・アカウントの停止を抑えながら継続運用する実務"
saturation: spreading
evidence:
  - {field: time, source: "https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_01736.html", certainty: attested, retrieved: primary, as_of: "2026-08-11"}
  - {field: saturation, source: "https://www.mext.go.jp/content/20240417-mxt_jogai02-000033777_5.pdf", certainty: attested, retrieved: primary, as_of: "2024-04-17"}
channels: []
relations:
  - {type: responds_to, target: trend/giga-learning-platform-renewal, certainty: hypothesis, source: "https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_01736.html"}
sources:
  - https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_01736.html
  - https://www.mext.go.jp/content/20240417-mxt_jogai02-000033777_5.pdf
  - https://www.mext.go.jp/content/20251020-mxt_syoto02-000045471_14.pdf
  - https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_02142.html
  - https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_02734.html
status: draft
updated: 2026-08-11
---

# GIGA端末・ネットワーク・学習基盤のライフサイクル運用

## 何をするか

自治体または学校単位で、端末の台帳、導入年、OS・性能、保証・契約、故障・修理履歴、予備機、児童生徒・教職員の割当、返却・再利用・リサイクルを管理する。更新時には、調達だけでなくデータ移行、初期設定、MDM、アカウント、認証、学習サービスへの接続、旧端末の扱い、授業を止めない切替手順を確認する。

ネットワークは、校内無線、回線、同時接続数、時間帯別の帯域・遅延・停止、クラウドサービスへの接続、デジタル教科書やMEXCBTなどの利用状況を実測する。障害時の切り分け、連絡先、代替手段、復旧目標を学校・教育委員会・ICT支援事業者で共有し、月次または学期ごとに更新する。

端末・ネットワーク・クラウド学習基盤の運用を、担当者の経験だけに依存させず、年度更新タスク、アカウントの入学・転出・卒業対応、権限・ログ・個人情報の確認、教員への利用支援、故障時の予備機配布まで一つのライフサイクルとして記録する。

## どのトレンドへの応答か

[trend/giga-learning-platform-renewal](../trends/giga-learning-platform-renewal.md)（GIGAスクール端末・学習基盤の更新運用）への応答とみる。第2期の更新計画や年度更新タスクリストが、端末を配備して終わりにせず、ネットワーク、クラウド、アカウント、支援、再利用・廃棄まで継続管理する必要を示しているためである。ただし、このpracticeを採用すれば授業中断、故障時間、教員負担、学習成果、費用が改善するとは確認していないため、関係の確度は`hypothesis`とした。

## 成立条件・失敗条件

**効果未確認**:（対象事業で自治体・学校向けのGIGA端末・ネットワーク・学習基盤ライフサイクル運用を提供・検証していない）。端末故障による停止時間、ネットワーク障害、アカウント利用不能、更新費用、教員・ICT支援員の負荷、学習成果は測っていない。

成立条件は、端末・ネットワーク・クラウドごとの責任者と更新期限が決まっていること、故障・性能・帯域・遅延を同じ定義で記録できること、予備機・代替回線・紙やオフラインの継続手段があること、入学・転出・卒業・異動時のアカウントとデータ移行を確認できることである。台帳や更新計画を作るだけで、実測、復旧訓練、授業継続、再利用・廃棄の確認をしなければ、このpracticeの実装とはみなさない。

**未確認**: 自治体・学校の台帳網羅率、更新完了率、予備機充足率、故障・修理期間、ネットワーク帯域・遅延・停止時間、アカウント停止、更新費用、教員・ICT支援員の負荷、学習活動や成果への影響。

## 飽和度の判定

`spreading` とした。文部科学省が第2期の端末更新・ネットワーク・学校DX・利活用計画、年度更新タスクリスト、ネットワークアセスメントを示し、自治体・学校が導入後の運用を検討できる段階にある。一方、自治体・学校横断の採用率、運用品質、費用、学習中断の減少を比較できるデータは揃っていないため、`commoditized`とは判定しない。

## 利用上の注意

**効果未確認**: 学校向けのサービスや支援を行う場合は、まず一つの自治体または学校を対象に、端末台帳、故障・予備機、ネットワーク実測、アカウント・クラウド接続、更新・データ移行、障害時の授業継続を一枚の運用表にする。学期中の端末交換やネットワーク障害を小さく想定し、復旧時間、問い合わせ、教員負担、利用できなかった授業時間を記録してから対象を広げる。外部資料では現時点で学校向けの検証事業がないため、効果の主張は置かない。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
