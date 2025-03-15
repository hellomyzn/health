## HKQuantityTypeIdentifierStairAscentSpeed

### 説明

`HKQuantityTypeIdentifierStairAscentSpeed` は、階段を上る際の速度を測定するデータタイプです。このデータは、移動能力の評価やフィットネス分析に活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                | データ例  |
| -------- | -------- | ------------------- | --------- |
| value    | Float    | 階段上昇速度（m/s） | `0.29998` |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierStairAscentSpeed" sourceName="my’s Apple Watch" sourceVersion="2890.16.23.1.1" unit="m/s" creationDate="2025-01-01 01:16:24 +0900" startDate="2025-01-01 01:15:09 +0900" endDate="2025-01-01 01:15:18 +0900" value="0.29998">
</Record>
```
