## HKQuantityTypeIdentifierEnvironmentalAudioExposure

### 説明
`HKQuantityTypeIdentifierEnvironmentalAudioExposure` は、Appleのヘルスデータにおいて周囲の環境音の音量レベルを記録するデータタイプです。このデータは、Apple Watch などのデバイスによって測定された環境音の騒音レベルをデシベル（dBASPL）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                         | データ例  |
| -------- | -------- | ---------------------------- | --------- |
| value    | Double   | 環境音の音量レベル（dBASPL） | `71.7797` |

### value のカテゴリ値

このデータタイプでは、`value` は環境音の騒音レベルをデシベル（dBASPL）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierEnvironmentalAudioExposure" sourceName="my’s Apple Watch" sourceVersion="10.6.1" device="<<HKDevice: 0x3037e4e60>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" unit="dBASPL" creationDate="2025-01-01 00:28:18 +0900" startDate="2025-01-01 00:23:43 +0900" endDate="2025-01-01 00:53:43 +0900" value="71.7797">
</Record>
```
