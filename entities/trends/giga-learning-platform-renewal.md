---
id: trend/giga-learning-platform-renewal
uri: urn:mtn:trend/giga-learning-platform-renewal
type: trend
kind: tech-enabled
stage: growing
market: education
geo: japan
label_ja: GIGAスクール端末・学習基盤の更新運用
label_en: Renewal and operationalization of Japan's GIGA school learning platform
authority:
  wikidata: null
  none_reason: "Wikidataで「GIGAスクール端末・学習基盤の更新運用」「renewal and operationalization of Japan's GIGA school learning platform」を確認したが、日本の端末・ネットワーク・クラウド学習環境の更新運用という変化そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "GIGAスクール構想第2期で、1人1台端末・ネットワーク・クラウド学習環境を導入後の更新・持続運用へ移る局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: GIGAスクール構想第2期
  note: "文部科学省の制度名称を踏まえ、導入後の端末・ネットワーク・クラウド学習環境の更新と持続運用という観測対象をこのKBで要約したラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mext.go.jp/content/20240417-mxt_jogai02-000033777_5.pdf", certainty: attested, retrieved: primary, as_of: "2024-04-17", tense: completed}
  - {field: stage, source: "https://www.mext.go.jp/content/20251020-mxt_syoto02-000045471_14.pdf", certainty: attested, retrieved: primary, as_of: "2025-10-20", tense: completed}
  - {field: time, source: "https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_01736.html", certainty: attested, retrieved: primary, as_of: "2026-08-11", tense: completed}
  - {field: current-status, source: "https://www.mext.go.jp/content/20240417-mxt_jogai02-000033777_5.pdf", certainty: attested, retrieved: primary, as_of: "2024-04-17", tense: intended}
predictions:
  - {claim: "文部科学省の次回公表で、GIGA第2期の令和6年度〜令和10年度の整備事業計画に基づく端末整備・更新が都道府県・市町村で計画どおり進捗している", by: "2029-03", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    文部科学省の補助・仕様・計画、自治体の調達と更新計画、学校のICT支援、端末管理・校内ネットワーク・クラウド学習サービスの運用を通じて伝わる。学校現場では教員研修、故障・問い合わせ対応、児童生徒のアカウント更新、授業でのデジタル教材利用が接点になるが、どの接点が更新判断や利用継続を左右するかは未確認のため、`channels` は張らない。
channels: []
relations: []
sources:
  - https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_01736.html
  - https://www.mext.go.jp/content/20240417-mxt_jogai02-000033777_5.pdf
  - https://www.mext.go.jp/content/20251020-mxt_syoto02-000045471_14.pdf
  - https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_00080.html
  - https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/mext_02734.html
status: verified
updated: 2026-09-21
---

# GIGAスクール端末・学習基盤の更新運用

## 見出している未来（何に向かって動いているか）

文部科学省は、都道府県・市町村が令和6年度から令和10年度（GIGA第2期）にかけて、予備機を含む
1人1台端末の計画的な更新を完了することを見込んでいる。同省の調達等ガイドライン（2024年4月17日）
は、「国策であるGIGAスクール構想の第2期を見据え、予備機を含む1人1台端末の計画的な更新を行う」
という令和5年11月閣議決定の方針を踏まえ、都道府県・市町村に令和6年度から令和10年度までの
各年度における端末整備・更新予定台数を記載した整備事業計画の策定を求めている。共同調達に
あたっては、「1人1台端末をはじめとするICT環境によって実現を目指す学びの姿」を各調達設置者が
計画に記載したうえで、それを踏まえた端末の在り方を検討することが期待されるとしている。

これは文部科学省が示した多年度の整備計画・期待であり（`attested`）、教員や児童生徒自身が
「今後どう端末を使いたいか」に答えた意向調査ではない。令和10年度（2028年度）までの整備完了に
向けて、都道府県・市町村ごとの進捗はこの記録では確認できていない。

## 足元の根拠（完了した事実）

GIGAスクール構想の第1期で整備された1人1台端末、高速ネットワーク、クラウドを使う学習環境が、初期導入の段階から計画的な更新と持続運用の段階へ移っている。文部科学省は第2期に向けて、端末の整備・更新計画、ネットワーク計画、学校DX計画、1人1台端末の利活用計画、更新・再利用・廃棄の取組を一体で整理するよう求めている。

端末は故障・保証切れ・性能低下・児童生徒の入れ替わりに対応しながら、学習を止めない予備機、修理・返却・再利用・リサイクルまで含めて管理する対象になった。文部科学省は1人1台端末の年度更新タスクリストも公開し、導入後にOSやアプリ、アカウント、校務・学習サービス、支援体制を継続的に見直す運用を示している。

利用が増えるほど、ネットワークの帯域、同時接続、校内無線、クラウド接続の実測も重要になる。デジタル教科書やMEXCBTなどの利用を前提に、文部科学省は学校ネットワークのアセスメントと改善を促している。これは端末台数やサービス契約数の増加だけでなく、端末・ネットワーク・クラウドを学習基盤として切れ目なく維持する変化である。

ここでいうtrendは、端末整備によって授業の質や学力が向上したことを意味しない。更新計画、ネットワーク測定、故障時の継続手段、アカウント・クラウド運用が、自治体・学校の通常業務として扱われ始めた変化を観測している。

## kind と stage の判定

**kind: tech-enabled とした。** 端末、校内ネットワーク、クラウド学習環境という技術基盤が、デジタル教材・学習サービス・校務の利用を可能にし、その更新や接続品質が利用継続の条件になっているためである。特定ベンダーの製品採用を示す `vendor-pushed` や、利用者の価値観の変化を示す `demand-shift` とは区別する。

**stage: growing とした。** GIGA第2期の端末更新、更新計画、年度更新タスクリスト、ネットワークアセスメント、予備機を含む継続運用が政策・予算・自治体計画の対象になっている。一方、自治体別の更新完了率、実測帯域、故障停止時間、クラウド利用の質、費用、教育成果は同じ定義で比較できないため、peakやcommoditizedとは判定しない。

## 時間

始点は、GIGA第2期の端末・ネットワーク・利活用計画と更新要件が具体化した `2024~` とした。これは端末配備の開始時点ではなく、導入後の更新・持続運用が独立した計画課題として整理された観測時点である。終点は `..`（継続中）。

## チャネルと伝播

文部科学省の補助・仕様・計画、自治体の調達と更新計画、学校のICT支援、端末管理・校内ネットワーク・クラウド学習サービスの運用を通じて伝わる。学校現場では教員研修、故障・問い合わせ対応、児童生徒のアカウント更新、授業でのデジタル教材利用が接点になるが、どの接点が更新判断や利用継続を左右するかは未確認のため、`channels` は張らない。

## 反証（これが偽なら何が観測されるか）

- GIGA学習基盤が更新・持続運用の段階に移っていないなら、端末更新計画、予備機、年度更新タスクリスト、ネットワークアセスメントへの公的支援・計画が継続して具体化しないはず
- 更新運用が学習の継続条件を改善するなら、端末故障による停止時間、ネットワーク障害・同時接続時の遅延、アカウント利用不能、授業中断を同じ定義で追跡できるはず
- 学習基盤の更新が教育的価値につながるなら、端末台数やログイン数だけでなく、教員・児童生徒の利用場面、学習活動、教員負担、学習成果を独立評価で確認できるはず

## 未着手

- 2026年9月21日、既存sourcesにあった文部科学省の調達等ガイドライン（20240417-mxt_jogai02-000033777_5.pdf）を実読し、令和10年度までの整備事業計画を見出している未来として追記した
- 自治体・学校別の端末更新計画、更新完了、予備機、修理・返却・再利用・リサイクルの実装状況を整理する
- 学校ネットワークの実測帯域、同時接続時の遅延・停止、校内無線、クラウド接続、デジタル教科書・MEXCBTの利用状況を同じ定義で確認する
- 端末・MDM・アカウント・クラウドサービスの更新、データ移行、情報セキュリティ、ICT支援員・教員の運用負荷を追跡する
- このtrendに応答するpractice（端末・ネットワーク・学習基盤のライフサイクル運用）の自治体・学校での採用率、継続性、費用、学習中断への影響を整理する
