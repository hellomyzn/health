## HKQuantityTypeIdentifierPhysicalEffort

### 説明
`HKQuantityTypeIdentifierPhysicalEffort` は、身体活動の強度を測定し、単位時間あたりのエネルギー消費量（kcal/hr·kg）として記録するデータタイプです。このデータは、運動強度の指標として活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                         | データ例 |
| -------- | -------- | ---------------------------- | -------- |
| value    | Float    | 身体活動の強度（kcal/hr·kg） | `1.1`    |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierPhysicalEffort" sourceName="my’s Apple Watch" sourceVersion="2890.16.23.1.1" unit="kcal/hr·kg" creationDate="2025-01-01 00:48:36 +0900" startDate="2025-01-01 00:01:20 +0900" endDate="2025-01-01 00:47:51 +0900" value="1.1">
  <MetadataEntry key="HKActivityType" value="3000"/>
  <MetadataEntry key="HKAlgorithmVersion" value="1"/>
  <MetadataEntry key="HKPhysicalEffortEstimationType" value="2"/>
</Record>
```
