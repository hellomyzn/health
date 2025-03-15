## HKQuantityTypeIdentifierAppleWalkingSteadiness

### 説明
`HKQuantityTypeIdentifierAppleWalkingSteadiness` は、Appleのヘルスデータにおいて歩行の安定性を記録するデータタイプです。このデータは、iPhone によって検出された歩行の安定性をパーセンテージ（%）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明              | データ例  |
| -------- | -------- | ----------------- | --------- |
| value    | Double   | 歩行の安定性（%） | `0.97279` |

### value のカテゴリ値

このデータタイプでは、`value` は歩行の安定性をパーセンテージ（%）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierAppleWalkingSteadiness" sourceName="hellomyzn13" sourceVersion="2890.16.23" device="<<HKDevice: 0x3034fc320>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="%" creationDate="2025-01-13 10:36:28 +0900" startDate="2025-01-06 09:00:00 +0900" endDate="2025-01-13 09:00:00 +0900" value="0.97279">
  <MetadataEntry key="HKAlgorithmVersion" value="2"/>
</Record>
```
