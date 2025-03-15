## HKQuantityTypeIdentifierFlightsClimbed

### 説明
`HKQuantityTypeIdentifierFlightsClimbed` は、Appleのヘルスデータにおいて登った階数を記録するデータタイプです。このデータは、Apple Watch や iPhone などのデバイスによって計測された階段の上昇回数を「フロア数（count）」で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                | データ例 |
| -------- | -------- | ------------------- | -------- |
| value    | Double   | 登った階数（count） | `2`      |

### value のカテゴリ値

このデータタイプでは、`value` は登った階数を「フロア数（count）」として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierFlightsClimbed" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3034fcbe0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="count" creationDate="2025-01-01 01:26:40 +0900" startDate="2025-01-01 01:15:31 +0900" endDate="2025-01-01 01:22:20 +0900" value="2">
</Record>
```
