## HKQuantityTypeIdentifierBasalEnergyBurned

### 説明
`HKQuantityTypeIdentifierBasalEnergyBurned` は、Appleのヘルスデータにおいて基礎代謝によるエネルギー消費量（カロリー）を記録するデータタイプです。このデータは、身体が安静時に消費するエネルギー量を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                               | データ例 |
| -------- | -------- | ---------------------------------- | -------- |
| value    | Double   | 基礎代謝による消費カロリー（kcal） | `17.354` |

### value のカテゴリ値

このデータタイプでは、`value` は基礎代謝によるエネルギー消費量（kcal）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierBasalEnergyBurned" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037ea3a0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="kcal" creationDate="2025-01-01 00:23:55 +0900" startDate="2025-01-01 00:03:40 +0900" endDate="2025-01-01 00:20:30 +0900" value="17.354">
</Record>
```
