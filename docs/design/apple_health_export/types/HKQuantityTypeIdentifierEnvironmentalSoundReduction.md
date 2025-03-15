## HKQuantityTypeIdentifierEnvironmentalSoundReduction

### 説明
`HKQuantityTypeIdentifierEnvironmentalSoundReduction` は、Appleのヘルスデータにおいて周囲の環境音の低減量を記録するデータタイプです。このデータは、Apple Watch などのデバイスによって測定された環境音の減少レベルをデシベル（dBASPL）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                     | データ例 |
| -------- | -------- | ------------------------ | -------- |
| value    | Double   | 環境音の低減量（dBASPL） | `16.97`  |

### value のカテゴリ値

このデータタイプでは、`value` は環境音の低減量をデシベル（dBASPL）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierEnvironmentalSoundReduction" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037e4fa0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="dBASPL" creationDate="2025-02-08 08:38:26 +0900" startDate="2025-02-08 08:32:02 +0900" endDate="2025-02-08 09:00:07 +0900" value="16.97">
</Record>
```
