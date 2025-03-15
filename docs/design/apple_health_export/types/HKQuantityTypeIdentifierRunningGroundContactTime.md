## HKQuantityTypeIdentifierRunningGroundContactTime

### 説明
`HKQuantityTypeIdentifierRunningGroundContactTime` は、ランニング中の地面接触時間（ミリ秒単位）を測定するデータタイプです。このデータはランニングフォームの分析や効率的なランニングの指標として使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                   | データ例 |
| -------- | -------- | ---------------------- | -------- |
| value    | Float    | 地面接触時間（ミリ秒） | `284`    |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRunningGroundContactTime" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037cec10>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="ms" creationDate="2025-01-14 12:35:20 +0900" startDate="2025-01-14 12:35:13 +0900" endDate="2025-01-14 12:35:13 +0900" value="284">
</Record>
```
