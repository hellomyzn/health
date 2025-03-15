## HKQuantityTypeIdentifierHeartRate

### 説明
`HKQuantityTypeIdentifierHeartRate` は、Appleのヘルスデータにおいて心拍数（bpm: beats per minute）を記録するデータタイプです。このデータは、Apple Watch などのデバイスによって測定された心拍数を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明          | データ例 |
| -------- | -------- | ------------- | -------- |
| value    | Integer  | 心拍数（bpm） | `60`     |

### value のカテゴリ値

このデータタイプでは、`value` は心拍数（bpm）を数値として記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierHeartRate" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3034fd2c0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="count/min" creationDate="2025-01-01 00:16:19 +0900" startDate="2025-01-01 00:03:10 +0900" endDate="2025-01-01 00:03:10 +0900" value="60">
  <MetadataEntry key="HKMetadataKeyHeartRateMotionContext" value="0"/>
</Record>
```
