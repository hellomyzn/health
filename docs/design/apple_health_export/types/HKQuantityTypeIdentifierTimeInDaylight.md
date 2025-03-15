## HKQuantityTypeIdentifierTimeInDaylight

### 説明

`HKQuantityTypeIdentifierTimeInDaylight` は、ユーザーが日光を浴びた時間を記録するデータタイプです。このデータは、健康管理や生活習慣の分析に活用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                   | データ例 |
| -------- | -------- | ---------------------- | -------- |
| value    | Integer  | 日光を浴びた時間（分） | `5`      |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierTimeInDaylight" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037ed860>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="min" creationDate="2025-01-01 10:40:40 +0900" startDate="2025-01-01 10:26:00 +0900" endDate="2025-01-01 10:31:00 +0900" value="5">
  <MetadataEntry key="HKMetadataKeyMaximumLightIntensity" value="16376 lx"/>
</Record>
```
