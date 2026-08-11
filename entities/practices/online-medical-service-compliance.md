---
id: practice/online-medical-service-compliance
uri: urn:mtn:practice/online-medical-service-compliance
type: practice
label_ja: オンライン診療の適合・継続運用
label_en: Compliance and continuity operations for online medical services
authority:
  wikidata: null
  none_reason: "「オンライン診療の適合・継続運用」「online medical service compliance operations」で検索したが、この運用の型そのもののWikidata項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "オンライン診療の制度・指針に沿って、適用判断、本人確認、記録、対面切替を運用する段階"
saturation: spreading
evidence:
  - {field: time, source: "https://www.mhlw.go.jp/stf/index_0024_00004.html", certainty: attested, retrieved: primary, as_of: "2026-04-02"}
channels: []
relations:
  - {type: responds_to, target: trend/online-medical-consultation-adoption, certainty: hypothesis, source: "https://www.mhlw.go.jp/stf/index_0024_00004.html"}
sources:
  - https://www.mhlw.go.jp/stf/index_0024_00004.html
  - https://www.mhlw.go.jp/stf/shingi2/0000190167_00062.html
status: draft
updated: 2026-08-11
---

# オンライン診療の適合・継続運用

## 何をするか

オンライン診療に適した患者・症状・診療場面を事前に判定し、本人確認、通信、診療記録、処方・配送、個人情報管理、対面への切替条件を一つの手順にまとめる。制度や指針の改訂日と担当者を台帳化し、広告・予約時の説明と診療現場の運用を一致させる。

## どのトレンドへの応答か

[trend/online-medical-consultation-adoption](../trends/online-medical-consultation-adoption.md)（オンライン診療の制度対応と利用拡大）への応答とみる。利用率がまだ限定的な段階で制度適合と安全な対面切替を先に整えるためである。実際の利用率や医療安全を改善する効果は未確認のため、関係の確度は`hypothesis`とした。

## 効いた条件・効かない条件

**未実施。** オンライン完結率、対面切替率、再診率、患者負担、通信障害、ヒヤリハットを同じ定義で追っていない。対象外の症例を無理にオンライン化すると、利便性より安全管理上の負担が大きくなる。

## 飽和度の判定

`emerging` とした。制度対応の必要性は明確になっているが、診療科・地域・医療機関ごとの標準運用と効果測定は未確認である。

## 自分の事業にどう使うか

**未実施。** 医療機関または関連サービスの一つの診療フローで、適用判定、本人確認、記録、対面切替、問い合わせ、インシデントを月次で点検する。医療行為や法令適合の判断は有資格者と担当官庁の最新情報に従う。
