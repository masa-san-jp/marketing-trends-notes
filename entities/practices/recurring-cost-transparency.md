---
id: practice/recurring-cost-transparency
uri: urn:mtn:practice/recurring-cost-transparency
type: practice
label_ja: 継続支出の透明化
label_en: Recurring cost transparency
saturation: spreading
authority:
  wikidata: null
  none_reason: "「継続支出の透明化」「subscription cost transparency」で検索したが、この運用の型に対応する同一性項目は確認できなかった（2026-08-11検索実施）"
time:
  start: "2022"
  end: ".."
  display: 改正特定商取引法の通信販売に関する規定が施行された2022年6月から
evidence:
  - {field: time, source: "https://www.caa.go.jp/policies/policy/consumer_transaction/specified_commercial_transactions/assets/consumer_transaction_cms202_220601_05.pdf", certainty: attested, retrieved: primary, as_of: "2022-06-01"}
relations:
  - {type: responds_to, target: trend/anxiety-multiplication, certainty: hypothesis, source: "https://www.boj.or.jp/research/o_survey/ishiki2507.htm"}
sources:
  - https://www.caa.go.jp/policies/policy/consumer_transaction/specified_commercial_transactions/assets/consumer_transaction_cms202_220601_05.pdf
  - https://www.caa.go.jp/policies/policy/consumer_research/international_affairs/icpen_2023/
  - https://www.boj.or.jp/research/o_survey/ishiki2507.htm
status: draft
updated: 2026-08-11
---

# 継続支出の透明化

## 何をするか

サブスクリプションや定期購入など、契約後も支払いが続く商品・サービスについて、申込みを確定する前に
支出の全体像を確認できるようにする。具体的には、次を最終確認画面で一度に見せる。

- 無料期間から有料に切り替わる時期と、その後に支払う金額
- 支払時期と支払方法
- 契約期間、自動更新の有無、利用できる回数
- 解約方法、申出期限、違約金などの不利益

消費者庁の事業者向け資料は、2022年6月1日以降、オンラインのサブスクリプション申込みにおいて、
これらの契約事項を最終確認画面で簡単に確認できるよう表示する必要があると説明している。

## どのトレンドへの応答か

[trend/anxiety-multiplication](../trends/anxiety-multiplication.md)（不安の多重化）への応答とみる。
日銀の2025年6月調査では、「暮らし向きにゆとりがなくなってきた」と答えた人が61.0％、物価が「かなり上がった」と答えた人が75.3％だった。
支出の不確実性を減らす表示は、複数の金銭的不安を抱える人が契約判断をしやすくする可能性がある。

ただし、表示を透明にしたことで不安が減った、契約後の後悔が減った、購買率が上がったという効果は、ここで確認した資料からは言えない。
この関係は**私の仮説**（`certainty: hypothesis`）として置く。

## 効いた条件・効かない条件

消費者庁の資料から、少なくとも契約条件を隠さず、申込みの最終段階で確認可能にすることは実装条件として言える。
一方、「初回◯円」だけを大きく見せ、2回目以降の金額・自動更新・解約方法を別画面に追いやる設計では、このpracticeの目的を満たさない。

**未実施**（自分の事業で試していない）。透明化による契約率・解約率・問い合わせ率への影響は測っていない。

## 飽和度の判定

`spreading` とした。法令対応として最終確認画面への表示が求められ、サブスク・定期購入のオンライン申込みに広く関係するためである。
ただし、実際の画面でどの程度分かりやすく表示されているか、事業者間での実装差は未確認。

## 自分の事業にどう使うか

**未実施。** 継続課金を行う場合は、申込み画面に「今日払う額」「次回以降の額」「次回支払日」「解約方法」を同じ視界で置き、
表示確認後の問い合わせ率・解約率・返金依頼を測る。これは効果の仮説を検証するための測定設計であり、現時点の実績ではない。
