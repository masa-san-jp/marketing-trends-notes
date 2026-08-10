---
id: trend/tracking-restrictions
uri: urn:mtn:trend/tracking-restrictions
type: trend
kind: regulation-driven
stage: peak
market: cross-category
geo: global
label_ja: 広告トラッキング制約の常態化
label_en: Normalization of ad-tracking restrictions
authority:
  wikidata: null
  none_reason: 現象そのものの項目は想定しにくい。執筆環境からWikidata APIに到達できず検索は未実施
time:
  start: "2018~"
  end: ".."
  display: GDPR適用（2018）前後から段階的に。ATT（2021）で モバイルに波及
naming:
  self_identified: true
  named_by: null
  named_when: null
  original_label: クッキーレス／ポストクッキー
  note: "業界内で自然発生的に定着した呼称で、当事者（広告主・媒体・代理店）自身が使う。初出の特定は未確認。「クッキーレス」はブラウザ側、ATT はアプリ側と、指す範囲が呼称ごとに微妙に違う点に注意"
freshness:
  valid_as_of: "2026-08-10"
  recheck_by: "2027-02-10"
evidence:
  - {field: kind, source: "https://developer.apple.com/app-store/user-privacy-and-data-use/", certainty: attested, retrieved: primary, as_of: "2026-08-10"}
predictions:
  - {claim: "2027年末までに、日本の主要広告主の間で計測の主軸がユーザー単位のトラッキングからMMM・インクリメンタリティ計測側へ寄る（業界団体・独立調査でその旨が確認できる）", by: "2027-12", resolved: null, outcome: null}
relations: []
sources:
  - https://developer.apple.com/app-store/user-privacy-and-data-use/
  - https://developer.apple.com/documentation/apptrackingtransparency
status: draft
updated: 2026-08-10
---

# 広告トラッキング制約の常態化

## 何が変わったか

ユーザー・端末を横断して行動を追跡し、精密なターゲティングと効果測定を行う——2010年代のデジタル
広告の前提だったこの手法が、規制とプラットフォームの制度変更で段階的に制約され、**制約がある状態が
例外ではなく常態**になった。

確定分として一次確認できているのは Apple の ATT（[event/apple-att](../events/apple-att.md)）:
iOS 14.5 以降、他社データとの紐づけ（トラッキング）と IDFA アクセスにユーザーの明示的許可が必須
（[Apple 開発者文書](https://developer.apple.com/app-store/user-privacy-and-data-use/)、2026-08-10 実読）。

**未確認**: GDPR（2018年適用）・改正個人情報保護法・Safari ITP・Chrome のサードパーティクッキー
廃止方針とその転換（2024年に廃止を撤回したとされる）は、執筆環境から一次情報に到達できず未確認。
この trend の全体像はこれらを併せて描く必要があり、現状は ATT の一点でしか裏が取れていない。

## kind と stage の判定

**kind: regulation-driven とした。** 判定表の第1問「規制・制度の施行日・条文を指せるか」に対し、
ATT はプラットフォームの規約であって行政規制ではない——ここに迷いがある。だが事業者から見れば
「外部から強制された制度変更で、応答の選択肢がない」という構造は行政規制と同じ側にあり、
GDPR・個人情報保護法という本来の行政規制も同じ束に入るため、regulation-driven を採る。
tech-enabled（技術が可能にした変化）ではない——技術的には従来の手法のほうが「可能」で、
制度がそれを止めた。

**stage: peak とした。** 制約は撤回されず追加される方向で推移し、業界の標準的な前提として
一般化している。ただし peak の判定表が求める「数字の高原状態」を示す独立した定量（例: 許可率・
クッキー同期率の推移）は執筆環境から取れておらず、**この stage 判定は定性による**。
**未確認**: 定量の裏づけ。再検証時（2027-02まで）に許可率・対応済み広告主比率の独立調査を探す。

## 時間

始点は `2018~`（およそ）。GDPR 適用（2018年5月とされる・未確認）を起点の目安とし、ATT（2021）で
モバイルアプリ側に波及、以降も制約が積み増される。終点は `..`（継続中）。

## チャネルと伝播

この trend は特定チャネル発ではない（規制・制度の側から来ている）ので、`channels` は張っていない。
影響はチャネル横断に及ぶ——だから `market: cross-category`。

## 反証（これが偽なら何が観測されるか）

- これが「常態化」でなく一時的な振れなら、**主要プラットフォームのどれかが制約を実質的に
  巻き戻し**、ユーザー単位トラッキングの可用性が2018年以前の水準に戻る動きが観測されるはず。
  Chrome のクッキー廃止撤回（未確認）がこの反証の部分的な成立である可能性があり、再検証時に
  「撤回された制約」と「残った制約」を仕分ける必要がある
- 制約が実務に効いていないなら、**広告主側の計測手法の構成が変わっていない**はず（MMM・
  コンバージョンAPI・クリーンルームへの移行が起きない）。移行が観測されれば効いている

## 未着手

- GDPR・改正個情法・ITP・Chrome の方針転換の一次確認（この trend の本体。ATT 以外が全部未確認）
- ATT 許可率の独立した実測を探す（ベンダー数字しか無い可能性が高い——その場合は vendor と明記して置く）
- 応答する practice の整理: MMM 回帰・リテールメディア（[practice/retail-media](../practices/retail-media.md)）・
  ファーストパーティデータ活用を responds_to で繋ぐ
