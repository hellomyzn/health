## HKQuantityTypeIdentifierRestingHeartRate

### 説明
`HKQuantityTypeIdentifierRestingHeartRate` は、安静時の心拍数（回数/min）を測定するデータタイプです。このデータは、心血管の健康状態を評価し、フィットネスレベルの指標として使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                                | データ例 |
| -------- | -------- | ----------------------------------- | -------- |
| value    | Float    | 1分あたりの安静時心拍数（回数/min） | `52`     |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRestingHeartRate" sourceName="my’s Apple Watch" sourceVersion="10.6.1" unit="count/min" creationDate="2025-01-01 06:53:29 +0900" startDate="2025-01-01 01:02:27 +0900" endDate="2025-01-01 06:47:55 +0900" value="52">
</Record>
```
