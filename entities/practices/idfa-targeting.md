---
id: practice/idfa-targeting
uri: urn:mtn:practice/idfa-targeting
type: practice
label_ja: IDFA前提の行動ターゲティング配信
label_en: IDFA-based behavioral ad targeting
saturation: negative
authority:
  wikidata: null
  none_reason: 執筆環境からWikidata APIに到達できず未確認
time:
  start: "2012~"
  end: "2021"
  display: IDFA導入（2012年とされる・未確認）からATT許可必須化（2021）まで
evidence: []
relations:
  - {type: killed_by, target: event/apple-att, certainty: attested, source: "https://developer.apple.com/app-store/user-privacy-and-data-use/"}
sources:
  - https://developer.apple.com/app-store/user-privacy-and-data-use/
status: draft
updated: 2026-08-10
---

# IDFA前提の行動ターゲティング配信

## 何をするか

iOS の広告識別子（IDFA）を鍵に、アプリ横断でユーザーの行動データを結合し、ターゲティング配信と
インストール計測を行う。2010年代のモバイル広告運用の標準形だった。

## どのトレンドへの応答か

前提としていた環境（識別子が黙って取れる）ごと消えた施策なので、いまの体系では「応答」ではなく
**死因の記録**としてこのファイルを置いている。

## 成立条件・失敗条件

**効かなくなった条件が本体**: [event/apple-att](../events/apple-att.md) により、iOS 14.5 以降は
IDFA アクセスと他社データとの紐づけ自体にユーザーの明示的許可が必須になった
（[Apple 開発者文書](https://developer.apple.com/app-store/user-privacy-and-data-use/)、2026-08-10 実読）。
許可が無ければこの施策は技術的に成立しない。`killed_by` を `certainty: attested` で張れるのは、
死因が当事者（Apple）の仕様文書で直接確認できるため。

**未確認**: 許可率の実測（低いとされるが、独立した数字に到達できていない）。Android 側
（GAID）の制約の進行。「完全に死んだ」のか「許可を得た残存部分がある」のかの定量。

## 飽和度の判定

`saturation: negative` とした——いま新規にこの施策に投資するのは、成立しない前提に賭けることに
なる。negative の中でも「逆効果」ではなく「実行不能」の型。

## 利用上の注意

直接は使わない（使えない）。このファイルの用途は、**打ち手が環境の一点に依存しているときの
死に方の記録**として参照すること——いま検討する施策が「どのプラットフォームの、どの仕様に
依存しているか」を列挙する習慣の根拠になる。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
