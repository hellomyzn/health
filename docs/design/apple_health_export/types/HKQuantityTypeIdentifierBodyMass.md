## HKQuantityTypeIdentifierBodyMass

### 説明
`HKQuantityTypeIdentifierBodyMass` は、Appleのヘルスデータにおいて体重を記録するデータタイプです。このデータは、スマートスケールや他の測定デバイスを使用して測定された体重をキログラム（kg）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明       | データ例 |
| -------- | -------- | ---------- | -------- |
| value    | Double   | 体重（kg） | `58.8`   |

### value のカテゴリ値

このデータタイプでは、`value` は体重をキログラム（kg）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierBodyMass" sourceName="eufy Life" sourceVersion="230" unit="kg" creationDate="2025-01-30 08:52:53 +0900" startDate="2025-01-30 08:52:52 +0900" endDate="2025-01-30 08:52:52 +0900" value="58.8">
</Record>
```
