## HKQuantityTypeIdentifierAppleExerciseTime

### 説明
`HKQuantityTypeIdentifierAppleExerciseTime` は、Appleのヘルスデータにおいて運動時間（分）を記録するデータタイプです。このデータは、Apple Watch などのデバイスによって検出された運動の継続時間を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明           | データ例 |
| -------- | -------- | -------------- | -------- |
| value    | Double   | 運動時間（分） | `1`      |

### value のカテゴリ値

このデータタイプでは、`value` は運動時間（分）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierAppleExerciseTime" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3034fe7b0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="min" creationDate="2025-01-01 01:19:12 +0900" startDate="2025-01-01 01:15:00 +0900" endDate="2025-01-01 01:16:00 +0900" value="1">
</Record>
```
