---
id: practice/privacy-preserving-ad-measurement
uri: urn:mtn:practice/privacy-preserving-ad-measurement
type: practice
label_ja: プライバシー保護型広告効果測定
label_en: Privacy-preserving ad measurement
saturation: spreading
authority:
  wikidata: null
  none_reason: "Wikidataで「プライバシー保護型広告効果測定」「privacy-preserving ad measurement」を確認したが、複数プラットフォームの仕様・研究・運用を束ねる実務の型そのものは確認できない"
time:
  start: "2021~"
  end: ".."
  display: ATT・第三者Cookie制約の後、ユーザー単位の識別子共有を避け、集計・閾値・ノイズ付きの信号で広告効果を測る2020年代
evidence:
  - {field: time, source: "https://developer.apple.com/videos/play/wwdc2021/10033/", certainty: attested, retrieved: primary, as_of: "2021-06"}
  - {field: time, source: "https://developer.apple.com/videos/play/wwdc2024/10060/", certainty: attested, retrieved: primary, as_of: "2024-06"}
  - {field: time, source: "https://petsymposium.org/popets/2024/popets-2024-0044.pdf", certainty: independent, retrieved: primary, as_of: "2024"}
  - {field: saturation, source: "https://markezine.jp/article/detail/46696", certainty: vendor, retrieved: primary, as_of: "2024-05"}
  - {field: saturation, source: "https://www.jicdaq.or.jp/release/press-release20241202/", certainty: attested, retrieved: primary, as_of: "2024-07"}
  - {field: saturation, source: "https://www.ppc.go.jp/files/pdf/241205_hearing_material-3.pdf", certainty: attested, retrieved: primary, as_of: "2024-12-05"}
  - {field: saturation, source: "https://privacysandbox.google.com/resources/case-studies/smn", certainty: vendor, retrieved: primary, as_of: "2025-01-29"}
  - {field: saturation, source: "https://prtimes.jp/main/html/rd/p/000000482.000007821.html", certainty: vendor, retrieved: primary, as_of: "2022-05-31"}
relations:
  - {type: responds_to, target: trend/tracking-restrictions, certainty: hypothesis, source: "https://developer.apple.com/app-store/ad-attribution/"}
sources:
  - https://developer.apple.com/app-store/ad-attribution/
  - https://developer.apple.com/videos/play/wwdc2021/10033/
  - https://developer.apple.com/videos/play/wwdc2024/10060/
  - https://privacysandbox.google.com/private-advertising/attribution-reporting/system-overview
  - https://petsymposium.org/popets/2024/popets-2024-0044.pdf
  - https://xica.net/en/action/marketing-mix-modeling/
  - https://markezine.jp/article/detail/46696
  - https://www.jicdaq.or.jp/release/press-release20241202/
  - https://www.ppc.go.jp/files/pdf/241205_hearing_material-3.pdf
  - https://privacysandbox.google.com/resources/case-studies/smn
  - https://prtimes.jp/main/html/rd/p/000000482.000007821.html
status: draft
updated: 2026-08-11
---

# プライバシー保護型広告効果測定

## 何をするか

広告のクリック・表示とインストール・購入などのコンバージョンを、ユーザーや端末を広告主・媒体間で
横断的に識別して結合するのではなく、プラットフォームが集計・遅延・閾値・ノイズなどの制約を付けた
ポストバックやレポートとして返し、キャンペーンの貢献度を測る。個人単位の行動履歴を再構成せず、
「どの広告・キャンペーンがどの程度の成果に結びついたか」を集計単位で判断する運用である。

AppleのAdAttributionKitは、他社アプリ間の個人・端末追跡を使わずにアプリのインストールや再エンゲージメントを
キャンペーンへ帰属させる。ポストバックの一部の値はプライバシー閾値を満たす場合だけ返され、少ないコンバージョンでは
返る情報が減る。GoogleのAttribution Reportingも、イベントレベルのレポートと集計可能レポートを分け、
ブラウザ側の関連付けとAggregation Serviceによる要約を組み合わせる。

## どのトレンドへの応答か

[trend/tracking-restrictions](../trends/tracking-restrictions.md)（広告トラッキング制約の常態化）への応答とみる。
ユーザー単位のIDFA・第三者Cookie・クロスサイト識別子が使いにくくなった後も、広告費の配分と効果検証は必要なので、
個人の追跡を維持するのではなく、集計された信号を受け取る測定方式へ置き換えるという仮説である。
ただし、これらのAPIの存在は採用率や広告主の成果を示さないため、関係の確度は `hypothesis` とした。

## 成立条件と限界

必要なコンバージョン、計測期間、キャンペーン粒度、集計単位を先に定義し、広告側・コンバージョン側・
サーバー側の実装を対応させる。小規模なキャンペーンではプライバシー閾値により値が欠落しやすく、
遅延やノイズを含むレポートを、ユーザー単位のアトリビューションと同じ精度として扱ってはいけない。
チャネル横断の予算判断には、集計レポートに加えてMMMやインクリメンタリティ実験を組み合わせる余地がある。

2024年の差分プライバシー研究は、広告コンバージョン測定を形式化し、アトリビューション規則・寄与上限・
プライバシー保証・クエリ結果の関係を分析している。これは個人追跡をやめれば自動的に同じ精度が得られるという
意味ではなく、測定精度とプライバシー保護の設計上のトレードオフを明示する研究である
（[Differentially Private Ad Conversion Measurement](https://petsymposium.org/popets/2024/popets-2024-0044.pdf)、
2026-08-11 実読）。

## 日本での実務側の観測

MMMについては、サイカが主催しインテージが実施した2024年5月の調査で、国内年商100億円以上企業に勤める
係長以上409人のうち、MMMを「知っており、現在導入している」は7.2%、「導入している・知っている・興味がある」の
合計は30.4%だった。導入経験者の導入時期では2020年6.1%に対して2021年16.3%で、導入の増加時期も確認できる
（[調査結果の紹介](https://markezine.jp/article/detail/46696)、2026-08-11 実読）。これは対象企業と設問が限定された
ベンダー主催調査であり、日本企業全体の導入率やプライバシー保護型計測APIの採用率とはみなさない。

広告品質の周辺実務では、JICDAQの2024年調査が、広告主・広告会社・媒体社など309社を対象に、無効トラフィック・
アドフラウド・ブランドセーフティへの認知と対策状況を確認している。対策は無効トラフィックとアドフラウドで約5〜6割、
ブランドセーフティで約6〜7割と報告され、広告主ではアドベリフィケーションツール利用の増加も示された。ただし、
これは広告品質管理の調査であって、MMMやインクリメンタリティの導入率を測ったものではない
（[JICDAQデジタル広告課題意識調査2024](https://www.jicdaq.or.jp/release/press-release20241202/)、2026-08-11 実読）。

日本固有の実装例として、2024年12月に個人情報保護委員会へ提出されたJIAA資料は、トラッキング制限への代替として、
同意に基づく共通ID、ユーザーデータを使わないコンテンツ／コンテキストターゲティング、Privacy Sandboxなどのブラウザ技術を挙げ、
広告主のFirst Party Data活用ニーズが広告配信だけでなく販促・経営戦略・サービス最適化へ広がっていると整理している
（[JIAAヒアリング資料](https://www.ppc.go.jp/files/pdf/241205_hearing_material-3.pdf)、2026-08-11 実読）。
これは業界団体の説明資料であり、導入率の統計ではない。

また、ソニーグループ傘下で日本を拠点とするDSPのSMNは、複数のSSPと日本の3社（スポーツ、モバイル、通信）で、
Protected Audience API、Topics API、Attribution Reporting APIのテストを行った。Googleのケーススタディでは、
一部用途で従来システムに近い配信結果や高いCTRが得られた一方、レイテンシーと技術的参入障壁が残り、継続テストが必要とされている
（[SMNのテスト事例](https://privacysandbox.google.com/resources/case-studies/smn)、2026-08-11 実読）。
これは日本の実装可能性を示す個別事例であり、市場全体の採用率ではない。

モバイル側の過去の実装例として、i-mobileは2022年5月時点で、自社ネットワークのiOSアプリ総リクエスト数の約90%を
SKAdNetwork計測対応にしたと発表している。ただし、これは一社の在庫におけるリクエスト比率であり、日本のiOSアプリ全体や
広告主全体の導入率には一般化しない（[i-mobile発表](https://prtimes.jp/main/html/rd/p/000000482.000007821.html)、2026-08-11 実読）。

**未実施。** 自分の事業でAdAttributionKit、Attribution Reporting、MMM、インクリメンタリティを組み合わせた
測定は試していない。導入率、欠測率、ノイズによる誤差、予算配分の改善幅は未確認である。

## 飽和度の判定

`spreading` とした。Apple・Googleの実装仕様と、プライバシー保護型広告測定の学術研究は確認できる一方、
日本のMMM導入調査と広告品質対策の調査は確認できたが、いずれも特定主体・対象に限られ、プライバシー保護型計測APIの
導入率や標準運用を直接測ってはいない。JIAAの整理、SMNの実装テスト、i-mobileの在庫対応は、導入可能な実装と周辺運用が
存在することを示すが、普及済み・標準化済みとは言えない。複数の測定方式が実装・検証されている拡大局面として暫定記録する。

## 自分の事業にどう使うか

**未実施。** まず広告プラットフォームの集計レポートと自社の売上・登録データを同じ期間・同じキャンペーン単位で
突き合わせ、次に地域・期間のホールドアウトなど、個人追跡に依存しない増分検証を設計する必要がある。
