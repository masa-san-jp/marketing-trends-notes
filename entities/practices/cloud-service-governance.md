---
id: practice/cloud-service-governance
uri: urn:mtn:practice/cloud-service-governance
type: practice
label_ja: クラウドサービス台帳・権限・移行・障害対応運用
label_en: Cloud service inventory, access, migration, and incident operations
authority:
  wikidata: null
  none_reason: "Wikidataで「クラウドサービス台帳・権限・移行・障害対応運用」「cloud service governance operations」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2019~"
  end: ".."
  display: "企業のクラウド利用が継続的に広がり、導入前後の選定・権限・移行・終了を運用で管理する2020年代"
saturation: spreading
evidence:
  - {field: time, source: "https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000183.html", certainty: independent, retrieved: primary, as_of: "2026-05-29"}
  - {field: saturation, source: "https://www.ipa.go.jp/jinzai/ics/core_human_resource/final_project/2024/cloud-security.html", certainty: attested, retrieved: primary, as_of: "2025-02-28"}
channels: []
relations:
  - {type: responds_to, target: trend/cloud-service-adoption, certainty: hypothesis, source: "https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000183.html"}
sources:
  - https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000183.html
  - https://www.ipa.go.jp/jinzai/ics/core_human_resource/final_project/2024/cloud-security.html
  - https://www.ipa.go.jp/security/guide/sme/ug65p90000019cbk-att/000055520.pdf
status: draft
updated: 2026-08-11
---

# クラウドサービス台帳・権限・移行・障害対応運用

## 何をするか

利用中・導入予定のクラウドサービスを台帳に登録し、業務責任者、保存する情報の分類、利用者・権限、認証方式、契約・更新日、料金、
データの保管地域、連携先、障害時の連絡先、エクスポート方法、終了時の削除確認を一つの運用で管理する。導入時だけでなく、権限変更、
サービス仕様変更、委託先変更、障害・漏えい疑い、契約終了のたびに台帳と判断記録を更新する。

IPAは、クラウドの企画・導入から運用までを対象に、クラウド特有の設定やインシデントに関するガイドラインへ案内するポータルを公開している。
このpracticeでは、サービス選定のチェックだけで終えず、最小権限、多要素認証、ログ確認、バックアップ、復旧手順、ベンダーへの問い合わせ窓口、
データ移行・削除の確認を担当者と期限まで落とし込む。

## どのトレンドへの応答か

[trend/cloud-service-adoption](../trends/cloud-service-adoption.md)（企業のクラウドサービス利用定着）への応答とみる。
クラウド利用率が上がるほど、導入数を増やすことと、誰がどの情報をどのサービスで扱い、障害や契約終了時にどう復旧・移行するかを管理することを
分ける必要があるためである。ただし、このpracticeを採用すれば情報漏えい、障害時間、費用、移行期間が減るとは確認していないため、関係の確度は
`hypothesis` とした。

## 成立条件・失敗条件

**効果未確認**: 対象事業でクラウドサービス台帳を運用し、権限レビュー、復旧訓練、データ移行・削除確認まで行っていない。導入後の費用、
障害時間、情報管理事故、解約時の移行負担への効果は測っていない。

成立条件は、サービスごとの業務責任者とデータ責任者が決まっていること、契約・設定・ログにアクセスできること、退職・異動・委託先変更時の
権限削除を確認できること、バックアップと復旧の担当・目標時間が合意されていることである。台帳を作るだけで権限レビューや復旧手順を試さなければ、
クラウド利用に伴う運用リスクを管理したとはみなさない。

**未確認**: サービス台帳の網羅率、過剰権限の削減率、復旧時間、設定ミス・障害・漏えい疑いの発生率、契約終了時のデータ移行費用、
サービス統合による費用や運用負荷の変化。

## 飽和度の判定

`spreading` とした。企業のクラウド利用が広がる一方、サービス選定から運用までのセキュリティ文書やチェック項目は複数の機関・業界に分散し、
台帳、権限、復旧、終了の指標を企業横断で比較できていないためである。最低限の運用要件が広く共通化された `commoditized` とは判定しない。

## 利用上の注意

**効果未確認**: まず会計、ファイル共有、顧客管理など一つの業務だけを対象に、サービス名、責任者、保存情報、権限、契約更新日、障害連絡先、
データ取り出し方法を台帳化する。その後、退職者の権限削除とバックアップからの復旧を小さく確認し、問題が出た項目を全サービスへ広げる。
現時点では対象事業者でこの運用を試した測定結果がないため、効果の主張は置かない。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
