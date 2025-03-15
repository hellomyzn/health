## HKQuantityTypeIdentifierRunningPower

### 説明
`HKQuantityTypeIdentifierRunningPower` は、ランニング中の出力パワー（ワット単位）を測定するデータタイプです。このデータはランナーのパフォーマンス評価やランニング効率の分析に利用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                           | データ例 |
| -------- | -------- | ------------------------------ | -------- |
| value    | Float    | ランニング中のパワー（ワット） | `69`     |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRunningPower" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037e4e60>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="W" creationDate="2025-01-14 12:35:00 +0900" startDate="2025-01-14 12:34:55 +0900" endDate="2025-01-14 12:34:55 +0900" value="69">
</Record>
```
