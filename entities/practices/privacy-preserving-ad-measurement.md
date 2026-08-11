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
relations:
  - {type: responds_to, target: trend/tracking-restrictions, certainty: hypothesis, source: "https://developer.apple.com/app-store/ad-attribution/"}
sources:
  - https://developer.apple.com/app-store/ad-attribution/
  - https://developer.apple.com/videos/play/wwdc2021/10033/
  - https://developer.apple.com/videos/play/wwdc2024/10060/
  - https://privacysandbox.google.com/private-advertising/attribution-reporting/system-overview
  - https://petsymposium.org/popets/2024/popets-2024-0044.pdf
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

**未実施。** 自分の事業でAdAttributionKit、Attribution Reporting、MMM、インクリメンタリティを組み合わせた
測定は試していない。導入率、欠測率、ノイズによる誤差、予算配分の改善幅は未確認である。

## 飽和度の判定

`spreading` とした。Apple・Googleの実装仕様と、プライバシー保護型広告測定の学術研究は確認できる一方、
日本の広告主・媒体における導入率や標準運用は確認できていない。したがって、普及済み・標準化済みではなく、
複数の測定方式が実装・検証されている拡大局面として暫定記録する。

## 自分の事業にどう使うか

**未実施。** まず広告プラットフォームの集計レポートと自社の売上・登録データを同じ期間・同じキャンペーン単位で
突き合わせ、次に地域・期間のホールドアウトなど、個人追跡に依存しない増分検証を設計する必要がある。
