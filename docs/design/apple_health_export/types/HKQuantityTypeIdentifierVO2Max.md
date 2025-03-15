## HKQuantityTypeIdentifierVO2Max

### 説明

`HKQuantityTypeIdentifierVO2Max` は、ユーザーの最大酸素摂取量（VO2 Max）を記録するデータタイプです。VO2 Max は、心肺機能の指標として用いられ、運動能力や持久力の評価に活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                        | データ例 |
| -------- | -------- | --------------------------- | -------- |
| value    | Float    | 最大酸素摂取量（mL/min/kg） | `42`     |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierVO2Max" sourceName="my’s Apple Watch" sourceVersion="2890.16.23.1.1" unit="mL/min·kg" creationDate="2025-01-02 08:39:51 +0900" startDate="2025-01-02 08:39:49 +0900" endDate="2025-01-02 08:39:49 +0900" value="42">
  <MetadataEntry key="HKVO2MaxTestType" value="2"/>
  <MetadataEntry key="HKMetadataKeySyncVersion" value="1"/>
  <MetadataEntry key="HKMetadataKeySyncIdentifier" value="B5870966-52DA-40C9-AED6-D3BE766AB797"/>
</Record>
```
