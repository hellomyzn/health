## HKQuantityTypeIdentifierDistanceWalkingRunning

### 説明
`HKQuantityTypeIdentifierDistanceWalkingRunning` は、Appleのヘルスデータにおいてウォーキングやランニングの移動距離を記録するデータタイプです。このデータは、Apple Watch や iPhone などのデバイスによって計測された歩行またはランニングの距離をキロメートル（km）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                       | データ例  |
| -------- | -------- | -------------------------- | --------- |
| value    | Double   | 歩行・ランニング距離（km） | `0.04142` |

### value のカテゴリ値

このデータタイプでは、`value` は歩行またはランニングの移動距離をキロメートル（km）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierDistanceWalkingRunning" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3037e96d0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="km" creationDate="2025-01-01 00:58:45 +0900" startDate="2025-01-01 00:47:42 +0900" endDate="2025-01-01 00:56:45 +0900" value="0.04142">
</Record>
```
