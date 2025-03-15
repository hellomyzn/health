## HKQuantityTypeIdentifierSixMinuteWalkTestDistance

### 説明

`HKQuantityTypeIdentifierSixMinuteWalkTestDistance` は、6分間歩行テストの結果として記録される歩行距離をメートル単位で測定するデータタイプです。このデータは、心肺機能の評価や歩行能力の指標として活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                                 | データ例 |
| -------- | -------- | ------------------------------------ | -------- |
| value    | Float    | 6分間歩行テストで測定された距離（m） | `500`    |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierSixMinuteWalkTestDistance" sourceName="hellomyzn13" sourceVersion="2890.16.23" unit="m" creationDate="2025-01-16 08:27:12 +0900" startDate="2025-01-16 08:27:09 +0900" endDate="2025-01-16 08:27:09 +0900" value="500">
  <MetadataEntry key="HKDateOfEarliestDataUsedForEstimate" value="2024-12-17 15:00:00 +0000"/>
  <MetadataEntry key="HKMetadataKeyAppleDeviceCalibrated" value="1"/>
</Record>
```
