## HKQuantityTypeIdentifierRunningStrideLength

### 説明

`HKQuantityTypeIdentifierRunningStrideLength` は、ランニング中のストライド（歩幅）をメートル単位で測定するデータタイプです。このデータはランニングフォームの分析やパフォーマンスの向上に役立ちます。

### 取得されるカラム

| カラム名 | データ型 | 説明                            | データ例 |
| -------- | -------- | ------------------------------- | -------- |
| value    | Float    | ランニング中のストライド長（m） | `0.9`    |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRunningStrideLength" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037d2fd0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="m" creationDate="2025-01-14 12:35:20 +0900" startDate="2025-01-14 12:35:13 +0900" endDate="2025-01-14 12:35:13 +0900" value="0.9">
</Record>
```
