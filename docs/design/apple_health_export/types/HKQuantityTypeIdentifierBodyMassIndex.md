## HKQuantityTypeIdentifierBodyMassIndex

### 説明
`HKQuantityTypeIdentifierBodyMassIndex` は、AppleのヘルスデータにおいてBMI（ボディマス指数）を記録するデータタイプです。このデータは、体重と身長を基に計算されたBMI値を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                  | データ例 |
| -------- | -------- | --------------------- | -------- |
| value    | Double   | BMI（ボディマス指数） | `20.8`   |

### value のカテゴリ値

このデータタイプでは、`value` はBMIの数値として記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierBodyMassIndex" sourceName="eufy Life" sourceVersion="230" unit="count" creationDate="2025-01-30 08:52:53 +0900" startDate="2025-01-30 08:52:52 +0900" endDate="2025-01-30 08:52:52 +0900" value="20.8">
</Record>
```
