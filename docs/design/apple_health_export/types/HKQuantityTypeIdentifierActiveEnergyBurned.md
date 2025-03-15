## HKQuantityTypeIdentifierActiveEnergyBurned

### 説明
`HKQuantityTypeIdentifierActiveEnergyBurned` は、Appleのヘルスデータにおいてアクティブエネルギー消費量（カロリー）を記録するデータタイプです。このデータは、運動や日常活動によって消費されたカロリー量を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                 | データ例 |
| -------- | -------- | -------------------- | -------- |
| value    | Double   | 消費カロリー（kcal） | `0.156`  |

### value のカテゴリ値

このデータタイプでは、`value` は消費されたカロリー量（kcal）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierActiveEnergyBurned" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x30378a210>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="kcal" creationDate="2025-01-01 00:33:57 +0900" startDate="2025-01-01 00:20:30 +0900" endDate="2025-01-01 00:22:13 +0900" value="0.156">
</Record>
```
