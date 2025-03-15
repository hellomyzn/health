## HKCategoryTypeIdentifierAppleStandHour

**説明**
1時間ごとに立ち上がったかどうかを記録するデータタイプ。Apple Watchがユーザーのスタンド状態を検出し、時間ごとに記録する。

### 取得されるカラム
| value | int | スタンド状態を表すカテゴリ値（下記参照） | 1 |

### value のカテゴリ値
| カテゴリ値                         | 数値 | 説明                                                         |
| ---------------------------------- | ---- | ------------------------------------------------------------ |
| HKCategoryValueAppleStandHourIdle  | 0    | その時間内に立ち上がらなかった（座ったままだった）ことを示す |
| HKCategoryValueAppleStandHourStood | 1    | その時間内に立ち上がったことを示す                           |

### RecordデータのXML形式
```xml
<Record type="HKCategoryTypeIdentifierAppleStandHour"
    sourceName="my’s Apple Watch"
    sourceVersion="10.6.1"
    device="<<HKDevice: 0x3035d0460>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,10, software:10.6.1, creation date:2024-08-24 17:12:03 +0000>"
    creationDate="2025-01-01 07:34:29 +0900"
    startDate="2025-01-01 07:00:00 +0900"
    endDate="2025-01-01 08:00:00 +0900"
    value="HKCategoryValueAppleStandHourStood">
</Record>
```
