## HKQuantityTypeIdentifierHeartRateVariabilitySDNN

### 説明
`HKQuantityTypeIdentifierHeartRateVariabilitySDNN` は、心拍変動（HRV）の標準偏差（SDNN）を記録するデータタイプです。このデータは、自律神経のバランスや心臓の健康状態を評価するために使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                             | データ例  |
| -------- | -------- | -------------------------------- | --------- |
| value    | Float    | 心拍変動の標準偏差（ミリ秒単位） | `20.1694` |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierHeartRateVariabilitySDNN" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3035adf90>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="ms" creationDate="2025-01-01 01:26:42 +0900" startDate="2025-01-01 01:25:41 +0900" endDate="2025-01-01 01:26:41 +0900" value="20.1694">
  <MetadataEntry key="HKAlgorithmVersion" value="2"/>
</Record>
```
