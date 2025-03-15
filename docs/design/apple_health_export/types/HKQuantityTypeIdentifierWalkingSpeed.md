## HKQuantityTypeIdentifierWalkingSpeed

### 説明

`HKQuantityTypeIdentifierWalkingSpeed` は、歩行中の速度を測定するデータタイプです。この値は、日常の歩行速度の変化を評価するために使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                 | データ例 |
| -------- | -------- | -------------------- | -------- |
| value    | Float    | 歩行中の速度（km/h） | `3.024`  |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierWalkingSpeed" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x30378a2b0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="km/hr" creationDate="2025-01-01 20:27:40 +0900" startDate="2025-01-01 10:28:18 +0900" endDate="2025-01-01 10:28:20 +0900" value="3.024">
</Record>
```
