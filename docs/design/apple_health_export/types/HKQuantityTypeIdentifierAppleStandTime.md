## HKQuantityTypeIdentifierAppleStandTime

### 説明
`HKQuantityTypeIdentifierAppleStandTime` は、Appleのヘルスデータにおいて起立時間（分）を記録するデータタイプです。このデータは、Apple Watch などのデバイスによって検出されたスタンド時間を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明               | データ例 |
| -------- | -------- | ------------------ | -------- |
| value    | Double   | スタンド時間（分） | `1`      |

### value のカテゴリ値

このデータタイプでは、`value` はスタンド時間（分）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierAppleStandTime" sourceName="my’s Apple Watch" sourceVersion="2890.16.23.1.1" unit="min" creationDate="2025-01-01 00:52:11 +0900" startDate="2025-01-01 00:45:00 +0900" endDate="2025-01-01 00:50:00 +0900" value="1">
</Record>
```
