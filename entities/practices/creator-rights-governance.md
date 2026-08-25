---
id: practice/creator-rights-governance
uri: urn:mtn:practice/creator-rights-governance
type: practice
label_ja: クリエイター契約・権利情報・収益分配・異議対応運用
label_en: Creator contract, rights information, revenue-sharing, and dispute operations
authority:
  wikidata: null
  none_reason: "Wikidataで「クリエイター契約・権利情報・収益分配・異議対応運用」「creator contract rights revenue sharing dispute operations」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2021~"
  end: ".."
  display: "デジタルプラットフォームでの作品利用に対応し、契約・権利情報・許諾・明細・収益分配・異議対応を一つの運用にする"
saturation: spreading
evidence:
  - {field: time, source: "https://www.bunka.go.jp/tokei_hakusho_shuppan/tokeichosa/chosakuken/index.html", certainty: attested, retrieved: primary, as_of: "2026-08-11"}
  - {field: saturation, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/seisaku/r06_04/", certainty: attested, retrieved: primary, as_of: "2025-01-20"}
channels: []
relations:
  - {type: responds_to, target: trend/creator-rights-compensation-transparency, certainty: hypothesis, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/seisaku/r06_04/"}
sources:
  - https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/seisaku/r06_04/
  - https://www.bunka.go.jp/tokei_hakusho_shuppan/tokeichosa/chosakuken/index.html
  - https://www.bunka.go.jp/prmagazine/rensai/news/news_019.html
  - https://www.bunka.go.jp/seisaku/chosakuken/
status: draft
updated: 2026-08-11
---

# クリエイター契約・権利情報・収益分配・異議対応運用

## 何をするか

作品・クリエイター・権利者・管理事業者・利用プラットフォームを一つの権利台帳で対応付け、どの作品を、誰が、どの地域・期間・方法で利用でき、
どの契約・料率・利用明細・収益分配に基づいて対価が支払われるかを追えるようにする。

- 権利情報: 作品ID、著作者・実演家・権利者、権利の種類、地域、期間、二次利用、許諾・禁止条件、更新日を登録する
- 契約・利用許諾: プラットフォーム・管理事業者との契約、広告・サブスクリプション・再生・視聴の対象、再編集・翻訳・二次利用の範囲を版管理する
- 明細・分配: 再生・視聴・利用数、収入の対象、料率・算定期間、控除、支払日、契約変更を明細と根拠資料に対応付ける
- 異議・監査: クリエイターが明細や利用を確認し、訂正・説明・監査・削除・利用停止を申し立てられる窓口と期限、判断、補償・再発防止を記録する

権利者が確認できない作品を利用する場合は、権利者探索、意思確認、裁定、補償金、利用期間、権利者からの申出を別のケースとして管理する。文化庁が
説明する未管理著作物裁定制度は、一定の手続と補償金を前提に、最長3年間の適法利用を可能にする制度であり、通常の契約・許諾管理の代替ではない。

## どのトレンドへの応答か

[trend/creator-rights-compensation-transparency](../trends/creator-rights-compensation-transparency.md)（クリエイターの権利・対価情報の透明化）への応答とみる。
文化庁の政策小委員会では、契約条件、料率、再生数、プラットフォーム収入、明細、二次収益、交渉力の不透明さが論点になっているため、作品・権利・
利用・対価を対応付け、クリエイターが確認・異議申立てできる状態にする運用が必要になる。

ただし、このpracticeを導入すれば収益、交渉力、クリエイターの満足度、権利侵害、権利処理コストが改善するとは確認していない。trendへの応答関係も、
透明性の課題に対する運用上の必要性から置いた**私の仮説**（`certainty: hypothesis`）である。

## 成立条件・失敗条件

**効果未確認**:（対象事業で作品制作、権利管理、プラットフォーム契約、収益分配、著作権異議対応を運用していない）。権利情報の登録率、契約・料率の
開示範囲、明細の照合時間、異議の解決率、支払までの時間、権利処理コスト、クリエイター収益への効果は測っていない。

成立条件は、作品・権利者・契約・利用・明細を同じIDで追えること、権利情報を更新できる責任者がいること、利用範囲・地域・期間・二次利用を契約前に
確定できること、明細の算定根拠を説明できること、異議・監査・訂正・補償の手続があること、権利者不明時の探索・裁定・補償を通常の許諾と混同しない
ことである。契約書を保存するだけ、または支払額だけを通知するだけでは、このpracticeの実装とはみなさない。

**未確認**: 分野・プラットフォーム別の採用率、権利情報データベースとの接続、料率・控除・明細の開示率、異議・監査の解決時間、二次利用・終了後の権利、
裁定・補償制度の利用件数と権利者への支払実績。

## 飽和度の判定

`spreading` とした。文化庁の個人クリエイター権利情報集約、対価還元、分野横断権利情報検索、著作権相談・裁定に関する調査研究や制度案内があり、
契約・権利・利用・分配をつなぐ運用を設計する材料は整備されている。一方、プラットフォーム・分野横断の採用率、データの相互運用、異議・監査・
補償の実績は比較できていないため、`commoditized`とは判定しない。

## 利用上の注意

**効果未確認**: クリエイターや作品を扱う事業で試す場合は、まず一作品について、権利者、許諾範囲、契約、利用実績、明細、支払、異議・更新を台帳化する。
利用許諾の前後で、権利確認、明細照合、支払、問い合わせ、訂正・異議対応にかかった時間を記録し、権利情報を整備した効果と作品・利用量の増加を混同しない。
外部資料では現時点でこのpracticeを試すクリエイター事業がないため、効果の主張は置かない。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
