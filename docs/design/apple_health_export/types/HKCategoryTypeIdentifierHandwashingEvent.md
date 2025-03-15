## HKCategoryTypeIdentifierHandwashingEvent

**説明**
`HKCategoryTypeIdentifierHandwashingEvent` は、手洗いイベントを記録する HealthKit のカテゴリタイプです。Apple Watch によって記録され、手洗いを検出した際に記録されます。

### 取得されるカラム

| カラム名 | データ型 | 説明           | データ例                     |
| -------- | -------- | -------------- | ---------------------------- |
| value    | string   | イベントの種類 | HKCategoryValueNotApplicable |

### value のカテゴリ値

| カテゴリ値                   | 説明                                                     |
| ---------------------------- | -------------------------------------------------------- |
| HKCategoryValueNotApplicable | 手洗いイベントの特定のカテゴリ値が適用されないことを示す |

### RecordデータのXML形式

```xml
<Record type="HKCategoryTypeIdentifierHandwashingEvent" sourceName="my’s Apple Watch" sourceVersion="1112.5.1" creationDate="2025-01-01 18:22:46 +0900" startDate="2025-01-01 18:22:40 +0900" endDate="2025-01-01 18:22:46 +0900" value="HKCategoryValueNotApplicable">
</Record>
```
