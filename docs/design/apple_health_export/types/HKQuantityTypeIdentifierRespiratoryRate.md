## HKQuantityTypeIdentifierRespiratoryRate

### 説明
`HKQuantityTypeIdentifierRespiratoryRate` は、1分あたりの呼吸数（回数/min）を測定するデータタイプです。このデータは、呼吸の健康状態や運動時の呼吸パターンを分析するために使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                          | データ例 |
| -------- | -------- | ----------------------------- | -------- |
| value    | Float    | 1分あたりの呼吸数（回数/min） | `15.5`   |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRespiratoryRate" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3034ff3e0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="count/min" creationDate="2025-01-01 00:03:26 +0900" startDate="2025-01-01 00:00:47 +0900" endDate="2025-01-01 00:00:47 +0900" value="15.5">
</Record>
```
