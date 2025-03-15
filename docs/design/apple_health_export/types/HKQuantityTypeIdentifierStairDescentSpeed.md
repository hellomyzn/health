## HKQuantityTypeIdentifierStairDescentSpeed

### 説明

`HKQuantityTypeIdentifierStairDescentSpeed` は、階段を下る際の速度を測定するデータタイプです。このデータは、移動能力の評価やフィットネス分析に活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                | データ例   |
| -------- | -------- | ------------------- | ---------- |
| value    | Float    | 階段下降速度（m/s） | `0.303332` |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierStairDescentSpeed" sourceName="my’s Apple Watch" sourceVersion="2890.16.23.1.1" unit="m/s" creationDate="2025-01-01 00:48:33 +0900" startDate="2025-01-01 00:47:40 +0900" endDate="2025-01-01 00:47:47 +0900" value="0.303332">
</Record>
```
