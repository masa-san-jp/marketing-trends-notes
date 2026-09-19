---
id: trend/cloud-service-adoption
uri: urn:mtn:trend/cloud-service-adoption
type: trend
kind: demand-shift
stage: growing
market: saas-b2b
geo: japan
label_ja: 企業のクラウドサービス利用定着
label_en: Continued adoption of cloud services by Japanese enterprises
authority:
  wikidata: null
  none_reason: "Wikidataで「企業のクラウドサービス利用」「enterprise cloud service adoption」を確認したが、日本企業のクラウド利用率の変化そのものの項目は確認できない"
time:
  start: "2019~"
  end: ".."
  display: "総務省の通信利用動向調査で、企業のクラウドサービス利用が2019年以降上昇している局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: クラウドサービスの利用
  note: "「企業のクラウドサービス利用定着」は、総務省調査の利用率推移を要約する記述的なラベル。企業がこの複合語を自称するかは確認していない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000183.html", certainty: independent, retrieved: primary, as_of: "2026-05-29", tense: completed}
  - {field: stage, source: "https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000183.html", certainty: independent, retrieved: primary, as_of: "2026-05-29", tense: completed}
  - {field: time, source: "https://www.e-stat.go.jp/stat-search/files?collect_area=000&page=1&toukei=00200356&tstat=000001243701", certainty: independent, retrieved: primary, as_of: "2026-05-29", tense: completed}
  - {field: current-status, source: "https://www.yano.co.jp/press-release/show/press_id/4055", certainty: vendor, retrieved: primary, as_of: "2026-03-16", tense: intended}
predictions:
  - {claim: "次回の通信利用動向調査で、企業のクラウドサービス利用率が2025年の8割超を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "矢野経済研究所の次回同種調査で、クラウド基盤（IaaS/PaaS）サービス市場規模が2029年予測値（5兆2,200億円）に向けた拡大経路を維持し、2026年時点で2025年実績（2兆7,100億円）を下回らない", by: "2027-06", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定の広告やSNSから広がる変化ではなく、業務システムの更新、テレワーク・拠点間共有、データ保管、外部サービスとの連携を通じて企業内に
    広がる。導入経路としてクラウド事業者、既存の業務ソフト、SIer、社内IT部門などが関わりうるが、どの経路が利用率の上昇を説明するかは
    この調査だけでは特定できないため、`channels` は張らない。
channels: []
relations: []
sources:
  - https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000183.html
  - https://www.soumu.go.jp/johotsusintokei/statistics/statistics05.html
  - https://www.e-stat.go.jp/stat-search/files?collect_area=000&page=1&toukei=00200356&tstat=000001243701
  - https://www.yano.co.jp/press-release/show/press_id/4055
status: verified
updated: 2026-09-19
---

# 企業のクラウドサービス利用定着

## 見出している未来（何に向かって動いているか）

クラウド基盤サービスの市場は、AIの本番稼働フェーズへの移行を主因として、今後も拡大が続くと
予測されている。矢野経済研究所「クラウド基盤（IaaS/PaaS）サービス市場に関する調査」
（2026年3月16日発表）は、同市場（事業者売上高ベース）が2029年に5兆2,200億円に達すると予測
し、2023年から2029年のCAGRを18.0％としている。同社は、2025年時点ではAI活用がPoC（概念
実証）段階にとどまる企業が多いが「今後は実用化・本番稼働フェーズへの移行が進む見込み」と
説明し、大手クラウド事業者のAI関連サービス拡充がさらに市場規模を押し上げると見込んでいる。

これは矢野経済研究所という市場調査会社自身の予測であり（`vendor`）、企業自身が「今後クラウド
利用を拡大したいか」と回答した意向調査ではない。オンプレミス回帰を選ぶ企業の増加も抑制要因
として同時に指摘されている。

## 足元の根拠（完了した事実）

日本企業でクラウドサービスを利用する割合が、単発の導入ではなく、複数年にわたって上昇している。総務省の「通信利用動向調査」では、
企業のクラウドサービス利用率は2019年の約65％から2025年の8割超まで上がった。2025年調査でも前年から上昇しており、クラウドを使うことが
一部の先進企業だけの選択ではなく、企業の業務基盤に組み込まれる方向が続いている。

ここでいうクラウドサービスは、インターネット経由で提供される業務システムや保存・共有、基盤などを含む広い統計上の区分であり、
すべてが同じSaaS製品を意味するわけではない。企業のクラウド利用率の上昇と、個別のSaaS製品の契約継続、業務プロセスへの定着、導入効果は
別の事実として扱う。

## kind と stage の判定

**kind: demand-shift とした。** クラウド技術が利用を可能にしていること自体ではなく、企業側が業務システムや保存・共有基盤を
ネットワーク経由のサービスとして利用する割合の変化を観測している。特定ベンダーが作った市場用語の採用率ではなく、総務省の企業調査で
利用者側の実装状況を測っているため、このエントリでは需要側の変化として扱う。

**stage: growing とした。** 企業のクラウドサービス利用率は2019年以降上昇し、2025年には8割を超えた。一方、企業規模・業種別の利用差、
全社利用と一部部門利用の差、移行後の費用・セキュリティ・データ移行負担は残っており、すべての業務が標準化されたpeakとは判定しない。

## 時間

始点は、総務省の時系列で企業のクラウドサービス利用率を比較できる2019年とした。これはクラウドの発明やサービス提供の始まりではなく、
企業利用が継続的な定点観測の対象になった範囲の始点である。終点は `..`（継続中）。

## チャネルと伝播

特定の広告やSNSから広がる変化ではなく、業務システムの更新、テレワーク・拠点間共有、データ保管、外部サービスとの連携を通じて企業内に
広がる。導入経路としてクラウド事業者、既存の業務ソフト、SIer、社内IT部門などが関わりうるが、どの経路が利用率の上昇を説明するかは
この調査だけでは特定できないため、`channels` は張らない。

## 反証（これが偽なら何が観測されるか）

- 企業のクラウド利用定着が一時的な導入ではないなら、次回以降の独立調査でも利用率が大きく下がらず、全社利用または複数部門利用の割合が維持・上昇するはず
- 利用率の上昇が業務基盤への組み込みを意味するなら、クラウド上の業務システム、データ連携、バックアップやセキュリティ管理の実装状況も同じ定義で追えるはず
- 利用率の上昇が実質的な定着を伴わないなら、解約・オンプレミス回帰、移行停止、費用超過、障害・情報管理事故の増加が企業規模や業種別に観測されるはず

## 未着手

- 2026年9月19日、矢野経済研究所のプレスリリースを実読して見出している未来を追記した。企業自身の「今後の利用拡大意向」を測る調査は今回探せていない
- 令和7年調査の企業規模・業種別に、クラウド利用率と全社利用・一部利用の差を確認する
- クラウドサービスの用途別利用率を時系列で整理し、保存・共有、業務アプリ、基盤利用のどこが伸びたかを確認する
- 導入前後の移行費用、運用負荷、障害、セキュリティ管理、解約・オンプレミス回帰を同じ定義で追える独立資料を探す
- このtrendに応答するpractice（利用サービス台帳、契約・権限・データ移行・障害対応をつなぐクラウド運用）の採用率と実績を整理する
