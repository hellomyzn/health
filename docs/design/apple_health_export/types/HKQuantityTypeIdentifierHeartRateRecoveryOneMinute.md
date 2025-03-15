## HKQuantityTypeIdentifierHeartRateRecoveryOneMinute

### 説明
`HKQuantityTypeIdentifierHeartRateRecoveryOneMinute` は、運動後1分間の心拍回復率を記録するデータタイプです。このデータは、運動後の心拍の回復度合いを測定し、心肺機能の指標として活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                     | データ例  |
| -------- | -------- | ------------------------ | --------- |
| value    | Float    | 1分後の心拍回復率（bpm） | `38.6132` |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierHeartRateRecoveryOneMinute" sourceName="my’s Apple Watch" sourceVersion="2890.16.23.1.1" unit="count/min" creationDate="2025-01-14 13:01:02 +0900" startDate="2025-01-14 12:59:51 +0900" endDate="2025-01-14 12:59:51 +0900" value="38.6132">
  <MetadataEntry key="HKMetadataKeyHeartRateRecoveryActivityType" value="52"/>
  <MetadataEntry key="HKMetadataKeySessionEstimate" value="19.6447 count/min"/>
  <MetadataEntry key="HKMetadataKeyHeartRateRecoveryActivityDuration" value="865.696 s"/>
  <MetadataEntry key="HKMetadataKeyHeartRateRecoveryTestType" value="2"/>
  <MetadataEntry key="HKMetadataKeyHeartRateRecoveryMaxObservedRecoveryHeartRate" value="114 count/min"/>
  <MetadataEntry key="HKAlgorithmVersion" value="1"/>
  <MetadataEntry key="HKMetadataKeyUserMotionContext" value="1"/>
</Record>
```
