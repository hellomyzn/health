## HKCategoryTypeIdentifierMindfulSession

**説明**
`HKCategoryTypeIdentifierMindfulSession` は、マインドフルネスセッションの記録を行う HealthKit のカテゴリタイプです。Apple Watch やその他のアプリによって記録され、瞑想や呼吸セッションなどの実施をトラッキングします。

### 取得されるカラム

| カラム名 | データ型 | 説明           | データ例                     |
| -------- | -------- | -------------- | ---------------------------- |
| value    | string   | イベントの種類 | HKCategoryValueNotApplicable |

### value のカテゴリ値

| カテゴリ値                   | 説明                                                                 |
| ---------------------------- | -------------------------------------------------------------------- |
| HKCategoryValueNotApplicable | マインドフルネスセッションの特定のカテゴリ値が適用されないことを示す |

### RecordデータのXML形式

```xml
<Record type="HKCategoryTypeIdentifierMindfulSession" sourceName="my’s Apple Watch" sourceVersion="10.6.1" creationDate="2025-01-31 08:43:23 +0900" startDate="2025-01-31 08:38:20 +0900" endDate="2025-01-31 08:43:20 +0900" value="HKCategoryValueNotApplicable">
</Record>
```
