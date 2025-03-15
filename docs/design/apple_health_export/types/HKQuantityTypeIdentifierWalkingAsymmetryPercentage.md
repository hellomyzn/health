## HKQuantityTypeIdentifierWalkingAsymmetryPercentage

### 説明

`HKQuantityTypeIdentifierWalkingAsymmetryPercentage` は、歩行の左右対称性を測定するデータタイプです。この値は、片側の足の着地時間の割合を示し、歩行のバランスを評価するのに使用されます。

### 取得されるカラム

| カラム名 | データ型 | 説明                    | データ例 |
| -------- | -------- | ----------------------- | -------- |
| value    | Float    | 歩行非対称性の割合（%） | `0.07`   |

### value のカテゴリ値

このデータタイプでは、`value` は数値として記録されるため、特定のカテゴリ値は存在しません。

### RecordデータのXML形式

```xml
<Record type="HKQuantityTypeIdentifierWalkingAsymmetryPercentage" sourceName="hellomyzn13" sourceVersion="17.6.1" device="<<HKDevice: 0x3037e97c0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone16,1, software:17.6.1, creation date:2024-08-31 17:17:55 +0000>" unit="%" creationDate="2025-01-01 20:27:40 +0900" startDate="2025-01-01 18:11:16 +0900" endDate="2025-01-01 18:11:38 +0900" value="0">
  <MetadataEntry key="HKMetadataKeyDevicePlacementSide" value="1"/>
</Record>
```
