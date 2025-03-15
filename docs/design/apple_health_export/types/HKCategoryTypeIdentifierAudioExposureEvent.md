## HKCategoryTypeIdentifierAudioExposureEvent

**説明**
`HKCategoryTypeIdentifierAudioExposureEvent` は、環境音の一時的な高音量露出イベントを記録する HealthKit のカテゴリタイプです。Apple Watch によって記録され、一定の閾値を超えた環境音レベルを検出した際に記録されます。

### 取得されるカラム
| カラム名 | データ型 | 説明           | データ例                                                     |
| -------- | -------- | -------------- | ------------------------------------------------------------ |
| value    | string   | イベントの種類 | HKCategoryValueEnvironmentalAudioExposureEventMomentaryLimit |

### value のカテゴリ値
| カテゴリ値                                                   | 説明                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| HKCategoryValueEnvironmentalAudioExposureEventMomentaryLimit | 環境音の一時的な高音量露出イベントを示す |

### RecordデータのXML形式
```xml
<Record type="HKCategoryTypeIdentifierAudioExposureEvent" sourceName="my’s Apple Watch" sourceVersion="1" device="<<HKDevice: 0x3035d0fa0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>" creationDate="2025-01-03 12:46:46 +0900" startDate="2025-01-03 12:44:01 +0900" endDate="2025-01-03 12:46:46 +0900" value="HKCategoryValueEnvironmentalAudioExposureEventMomentaryLimit">
  <MetadataEntry key="HKMetadataKeyAudioExposureLevel" value="98.5993 dBASPL"/>
</Record>
```

### 備考
- 高音量（85dB以上）が長時間続くと聴覚に影響を与える可能性がある。
- Apple Watchは、短時間でも **有害な音量レベル（例: 100dB以上）** に達した場合、このイベントを記録する。
