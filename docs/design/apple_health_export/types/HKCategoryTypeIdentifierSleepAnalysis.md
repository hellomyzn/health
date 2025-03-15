
## HKCategoryTypeIdentifierSleepAnalysis

### 説明
`HKCategoryTypeIdentifierSleepAnalysis` は、Appleのヘルスデータにおける睡眠の記録を表します。記録されたデータは、睡眠の開始時間と終了時間、および睡眠の状態（浅い睡眠、深い睡眠、覚醒など）を示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                       | データ例                                        |
| -------- | -------- | -------------------------- | ----------------------------------------------- |
| value    | String   | 睡眠の状態を示すカテゴリ値 | `HKCategoryValueSleepAnalysisAsleepUnspecified` |

### value のカテゴリ値

| カテゴリ値                                    | 説明               |
| --------------------------------------------- | ------------------ |
| HKCategoryValueSleepAnalysisInBed             | ベッドにいる状態   |
| HKCategoryValueSleepAnalysisAsleepUnspecified | 指定なしの睡眠状態 |
| HKCategoryValueSleepAnalysisAwake             | 覚醒状態           |
| HKCategoryValueSleepAnalysisAsleepCore        | コア睡眠           |
| HKCategoryValueSleepAnalysisAsleepDeep        | 深い睡眠           |
| HKCategoryValueSleepAnalysisAsleepREM         | レム睡眠           |

### RecordデータのXML形式
```xml
<Record type="HKCategoryTypeIdentifierSleepAnalysis" sourceName="AutoSleep" sourceVersion="6.14.0" creationDate="2025-01-18 19:45:22 +0900" startDate="2025-01-18 06:59:00 +0900" endDate="2025-01-18 08:13:00 +0900" value="HKCategoryValueSleepAnalysisAsleepUnspecified">
</Record>
```
