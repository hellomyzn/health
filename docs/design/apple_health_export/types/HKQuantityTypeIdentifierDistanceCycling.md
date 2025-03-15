## HKQuantityTypeIdentifierDistanceCycling

### 説明
`HKQuantityTypeIdentifierDistanceCycling` は、Appleのヘルスデータにおいてサイクリング（自転車移動）の距離を記録するデータタイプです。このデータは、Apple Watch などのデバイスによって計測された移動距離をキロメートル（km）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                   | データ例   |
| -------- | -------- | ---------------------- | ---------- |
| value    | Double   | サイクリング距離（km） | `0.126904` |

### value のカテゴリ値

このデータタイプでは、`value` はサイクリングの距離をキロメートル（km）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierDistanceCycling" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3034fe170>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="km" creationDate="2025-01-03 18:26:56 +0900" startDate="2025-01-03 18:24:30 +0900" endDate="2025-01-03 18:25:00 +0900" value="0.126904">
</Record>
```
