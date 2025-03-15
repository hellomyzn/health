## HKQuantityTypeIdentifierStepCount

### 説明

`HKQuantityTypeIdentifierStepCount` は、ユーザーが歩いた歩数を記録するデータタイプです。このデータは、日常活動の追跡や健康管理に活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明          | データ例 |
| -------- | -------- | ------------- | -------- |
| value    | Integer  | 歩数（count） | `59`     |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierStepCount" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3034ff3e0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="count" creationDate="2025-01-01 00:58:45 +0900" startDate="2025-01-01 00:47:42 +0900" endDate="2025-01-01 00:56:45 +0900" value="59">
</Record>
```
