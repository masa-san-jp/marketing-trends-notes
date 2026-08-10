---
id: event/apple-att
uri: urn:mtn:event/apple-att
type: event
label_ja: Apple ATT（App Tracking Transparency）の許可必須化
label_en: Apple App Tracking Transparency enforcement
authority:
  wikidata: null
  none_reason: 執筆環境からWikidata APIに到達できず未確認（App Tracking Transparency で項目がある可能性が高い）
time:
  start: "2021"
  end: null
  display: iOS 14.5 / iPadOS 14.5 / tvOS 14.5 以降
evidence:
  - {field: time, source: "https://developer.apple.com/app-store/user-privacy-and-data-use/", certainty: attested, retrieved: primary, as_of: "2026-08-10"}
relations:
  - {type: part_of, target: trend/tracking-restrictions}
  - {type: documented_in, target: source/apple-user-privacy-page}
sources:
  - https://developer.apple.com/app-store/user-privacy-and-data-use/
  - https://developer.apple.com/documentation/apptrackingtransparency
status: verified
updated: 2026-08-10
---

# Apple ATT（App Tracking Transparency）の許可必須化

## 何が起きたか

iOS 14.5・iPadOS 14.5・tvOS 14.5 以降、アプリがユーザーを「トラッキング」する（自アプリで集めた
ユーザー・端末データを、他社のアプリ・ウェブサイト・オフラインのデータと紐づけて広告のターゲティング
や効果測定に使う）、または端末の広告識別子（IDFA）にアクセスするには、AppTrackingTransparency
フレームワークを通じた**ユーザーの明示的な許可が必須**になった。

Apple の開発者向け文書
[User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
（2026-08-10 実読）が定義する「トラッキング」には、他社データに基づくターゲティング広告の表示、
データブローカーへの位置情報・メールリストの共有、リターゲティング目的での ID リストの第三者
広告ネットワークへの共有、他社データと結合する third-party SDK の設置（自分で使わなくても）が
含まれる。端末上でのみ結合し外に出さない場合などは対象外と明記されている。

技術仕様は [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)。

**未確認**: iOS 14.5 の正確なリリース日（2021年4月26日とされる）は、執筆環境から Apple の
リリースノート等に到達できず一次確認していない。`time.start` は年までを確定分として置いた。

**未確認**: 許可プロンプトのオプトイン率の実測値（各計測ベンダーが公表しているが vendor 数字で、
かつ執筆環境から到達できず）。

## なぜ時間軸の釘になるか

モバイル広告の精密ターゲティングと効果測定は IDFA を前提に組まれていた。その前提が「ユーザーの
許可がある場合のみ」に変わった日付として、複数の trend / practice（トラッキング制約の常態化、
IDFA 前提の配信手法の失効）をこのイベントに固定できる。
