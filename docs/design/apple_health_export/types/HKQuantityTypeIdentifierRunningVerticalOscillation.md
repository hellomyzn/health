## HKQuantityTypeIdentifierRunningVerticalOscillation

### 説明

`HKQuantityTypeIdentifierRunningVerticalOscillation` は、ランニング中の上下動（垂直振動）をセンチメートル単位で測定するデータタイプです。このデータはランニングフォームの効率性や安定性の分析に役立ちます。

### 取得されるカラム

| カラム名 | データ型 | 説明                       | データ例 |
| -------- | -------- | -------------------------- | -------- |
| value    | Float    | ランニング中の上下動（cm） | `8.3`    |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierRunningVerticalOscillation" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037d28a0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="cm" creationDate="2025-01-14 12:35:20 +0900" startDate="2025-01-14 12:35:07 +0900" endDate="2025-01-14 12:35:07 +0900" value="8.3">
```
