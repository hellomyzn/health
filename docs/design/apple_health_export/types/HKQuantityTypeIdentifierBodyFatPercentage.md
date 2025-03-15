## HKQuantityTypeIdentifierBodyFatPercentage

### 説明
`HKQuantityTypeIdentifierBodyFatPercentage` は、Appleのヘルスデータにおいて体脂肪率を記録するデータタイプです。このデータは、スマートスケールや他の測定デバイスを使用して測定された体脂肪率をパーセンテージ（%）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明          | データ例 |
| -------- | -------- | ------------- | -------- |
| value    | Double   | 体脂肪率（%） | `0.162`  |

### value のカテゴリ値

このデータタイプでは、`value` は体脂肪率をパーセンテージ（%）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierBodyFatPercentage" sourceName="eufy Life" sourceVersion="230" unit="%" creationDate="2025-01-30 08:52:53 +0900" startDate="2025-01-30 08:52:52 +0900" endDate="2025-01-30 08:52:52 +0900" value="0.162">
</Record>
```
