## HKQuantityTypeIdentifierWalkingHeartRateAverage

### 説明

`HKQuantityTypeIdentifierWalkingHeartRateAverage` は、歩行中の平均心拍数を測定するデータタイプです。この値は、日常活動中の心臓の健康状態を評価するのに使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                      | データ例 |
| -------- | -------- | ------------------------- | -------- |
| value    | Float    | 歩行中の平均心拍数（bpm） | `85`     |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierWalkingHeartRateAverage" sourceName="my’s Apple Watch" sourceVersion="10.6.1" unit="count/min" creationDate="2025-01-02 08:39:52 +0900" startDate="2025-01-02 01:06:07 +0900" endDate="2025-01-02 08:39:48 +0900" value="85">
</Record>
```
