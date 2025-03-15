## HKQuantityTypeIdentifierHeadphoneAudioExposure

### 説明
`HKQuantityTypeIdentifierHeadphoneAudioExposure` は、Appleのヘルスデータにおいてヘッドフォンを使用した際の音量レベルを記録するデータタイプです。このデータは、AirPods や EarPods などのデバイスによって測定された音量レベルをデシベル（dBASPL）で示します。

### 取得されるカラム

| カラム名 | データ型 | 説明                             | データ例  |
| -------- | -------- | -------------------------------- | --------- |
| value    | Double   | ヘッドフォン音量レベル（dBASPL） | `65.1861` |

### value のカテゴリ値

このデータタイプでは、`value` はヘッドフォンの音量レベルをデシベル（dBASPL）として数値で記録されます。そのため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierHeadphoneAudioExposure" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3034d64e0>, name:AirPods Pro, manufacturer:Apple Inc., model:0x200e, localIdentifier:38:EC:0D:BF:32:C6-tacl, creation date:2020-06-01 06:06:25 +0000>" unit="dBASPL" creationDate="2025-01-05 12:01:21 +0900" startDate="2025-01-05 11:51:18 +0900" endDate="2025-01-05 11:51:36 +0900" value="65.1861">
```
