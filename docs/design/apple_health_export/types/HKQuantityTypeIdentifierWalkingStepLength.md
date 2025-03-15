## HKQuantityTypeIdentifierWalkingStepLength

### 説明

`HKQuantityTypeIdentifierWalkingStepLength` は、歩行時の1歩の長さ（ステップ長）を測定するデータタイプです。この値は、歩行能力の評価や運動習慣の分析に使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                     | データ例 |
| -------- | -------- | ------------------------ | -------- |
| value    | Float    | 歩行時のステップ長（cm） | `48`     |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierWalkingStepLength" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3034fee40>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="cm" creationDate="2025-01-01 20:27:40 +0900" startDate="2025-01-01 10:28:18 +0900" endDate="2025-01-01 10:28:20 +0900" value="48">
</Record>
```
