## HKQuantityTypeIdentifierWalkingDoubleSupportPercentage

### 説明

`HKQuantityTypeIdentifierWalkingDoubleSupportPercentage` は、歩行中の両足が地面に接地している時間の割合を測定するデータタイプです。この値は、歩行の安定性を評価するのに使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                            | データ例 |
| -------- | -------- | ------------------------------- | -------- |
| value    | Float    | 歩行中の両足支持時間の割合（%） | `0.305`  |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierWalkingDoubleSupportPercentage" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3034fe490>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="%" creationDate="2025-01-01 20:27:40 +0900" startDate="2025-01-01 10:28:18 +0900" endDate="2025-01-01 10:28:20 +0900" value="0.305">
</Record>
```
