## HKQuantityTypeIdentifierRunningSpeed

### 説明
`HKQuantityTypeIdentifierRunningSpeed` は、ランニング中の移動速度（km/hr単位）を測定するデータタイプです。このデータはランニングパフォーマンスの分析やトレーニング計画に利用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                        | データ例  |
| -------- | -------- | --------------------------- | --------- |
| value    | Float    | ランニング中の速度（km/hr） | `4.92155` |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRunningSpeed" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3035d1db0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="km/hr" creationDate="2025-01-14 12:34:57 +0900" startDate="2025-01-14 12:34:55 +0900" endDate="2025-01-14 12:34:55 +0900" value="4.92155">
</Record>
```
