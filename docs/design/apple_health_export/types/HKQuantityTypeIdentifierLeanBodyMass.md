## HKQuantityTypeIdentifierLeanBodyMass

### 説明
`HKQuantityTypeIdentifierLeanBodyMass` は、除脂肪体重（筋肉、骨、水分などの脂肪以外の体重）を記録するデータタイプです。このデータは、健康管理やフィットネスの指標として使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                         | データ例 |
| -------- | -------- | ---------------------------- | -------- |
| value    | Float    | 除脂肪体重（キログラム単位） | `49.3`   |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierLeanBodyMass" sourceName="eufy Life" sourceVersion="230" unit="kg" creationDate="2025-01-30 08:52:53 +0900" startDate="2025-01-30 08:52:52 +0900" endDate="2025-01-30 08:52:52 +0900" value="49.3">
</Record>
```
