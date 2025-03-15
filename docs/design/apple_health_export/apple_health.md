## Health Data Type

| データタイプ                                             | 説明                                     |
| -------------------------------------------------------- | ---------------------------------------- |
| `HKCategoryTypeIdentifierAppleStandHour`                 | 1時間ごとに立ち上がったかどうかを記録    |
| `HKCategoryTypeIdentifierAudioExposureEvent`             | 有害な音量レベルへの曝露イベントを記録   |
| `HKCategoryTypeIdentifierHandwashingEvent`               | 手洗いイベントを検出・記録               |
| `HKCategoryTypeIdentifierMindfulSession`                 | マインドフルネスセッションの記録         |
| `HKCategoryTypeIdentifierSleepAnalysis`                  | 睡眠状態（浅い、深い、レムなど）の記録   |
| `HKDataTypeSleepDurationGoal`                            | 設定された睡眠時間の目標                 |
| `HKQuantityTypeIdentifierActiveEnergyBurned`             | 消費したアクティブエネルギー（カロリー） |
| `HKQuantityTypeIdentifierAppleExerciseTime`              | 運動時間の記録（分単位）                 |
| `HKQuantityTypeIdentifierAppleStandTime`                 | 立っていた時間の合計（分単位）           |
| `HKQuantityTypeIdentifierAppleWalkingSteadiness`         | 歩行の安定性を評価するスコア             |
| `HKQuantityTypeIdentifierBasalEnergyBurned`              | 安静時のエネルギー消費量（カロリー）     |
| `HKQuantityTypeIdentifierBodyFatPercentage`              | 体脂肪率（%）                            |
| `HKQuantityTypeIdentifierBodyMass`                       | 体重（kg）                               |
| `HKQuantityTypeIdentifierBodyMassIndex`                  | BMI（体格指数）                          |
| `HKQuantityTypeIdentifierDistanceCycling`                | サイクリングの距離（km）                 |
| `HKQuantityTypeIdentifierDistanceWalkingRunning`         | 歩行およびランニングの距離（km）         |
| `HKQuantityTypeIdentifierEnvironmentalAudioExposure`     | 周囲の音量レベルへの曝露（dB）           |
| `HKQuantityTypeIdentifierEnvironmentalSoundReduction`    | 環境音の減少度合い                       |
| `HKQuantityTypeIdentifierFlightsClimbed`                 | 登った階数                               |
| `HKQuantityTypeIdentifierHeadphoneAudioExposure`         | ヘッドフォンの音量曝露（dB）             |
| `HKQuantityTypeIdentifierHeartRate`                      | 心拍数（BPM）                            |
| `HKQuantityTypeIdentifierHeartRateRecoveryOneMinute`     | 運動後1分間の心拍数回復量                |
| `HKQuantityTypeIdentifierHeartRateVariabilitySDNN`       | 心拍変動（SDNN）                         |
| `HKQuantityTypeIdentifierHeight`                         | 身長（cm）                               |
| `HKQuantityTypeIdentifierLeanBodyMass`                   | 除脂肪体重（kg）                         |
| `HKQuantityTypeIdentifierPhysicalEffort`                 | 身体活動の強度                           |
| `HKQuantityTypeIdentifierRespiratoryRate`                | 呼吸数（回/分）                          |
| `HKQuantityTypeIdentifierRestingHeartRate`               | 安静時心拍数（BPM）                      |
| `HKQuantityTypeIdentifierRunningGroundContactTime`       | ランニング時の地面接触時間（ms）         |
| `HKQuantityTypeIdentifierRunningPower`                   | ランニング時の出力（W）                  |
| `HKQuantityTypeIdentifierRunningSpeed`                   | ランニング速度（m/s）                    |
| `HKQuantityTypeIdentifierRunningStrideLength`            | ランニングストライド長（m）              |
| `HKQuantityTypeIdentifierRunningVerticalOscillation`     | ランニング時の上下動（cm）               |
| `HKQuantityTypeIdentifierSixMinuteWalkTestDistance`      | 6分間歩行テストの距離（m）               |
| `HKQuantityTypeIdentifierStairAscentSpeed`               | 階段上昇速度（m/s）                      |
| `HKQuantityTypeIdentifierStairDescentSpeed`              | 階段下降速度（m/s）                      |
| `HKQuantityTypeIdentifierStepCount`                      | 歩数（歩）                               |
| `HKQuantityTypeIdentifierTimeInDaylight`                 | 日光を浴びた時間（分）                   |
| `HKQuantityTypeIdentifierVO2Max`                         | 最大酸素摂取量（ml/kg/min）              |
| `HKQuantityTypeIdentifierWalkingAsymmetryPercentage`     | 歩行の左右非対称性（%）                  |
| `HKQuantityTypeIdentifierWalkingDoubleSupportPercentage` | 両足が地面に接している時間の割合（%）    |
| `HKQuantityTypeIdentifierWalkingHeartRateAverage`        | 歩行時の平均心拍数（BPM）                |
| `HKQuantityTypeIdentifierWalkingSpeed`                   | 歩行速度（m/s）                          |
| `HKQuantityTypeIdentifierWalkingStepLength`              | 歩幅（cm）                               |


## 共通のカラム
| カラム名     | データ型 | 説明                                                                   | データ例                  |
| ------------ | -------- | ---------------------------------------------------------------------- | ------------------------- |
| sourceName   | str      | データを記録したデバイスまたはアプリの名前                             | "my’s Apple Watch"        |
| creationDate | datetime | データが記録された日時 (yyyy-mm-dd hh:mm:ss +h:00)                     | 2025-01-01 07:34:29 +0900 |
| startDate    | datetime | 記録が開始された日時（該当する時間の開始） (yyyy-mm-dd hh:mm:ss +h:00) | 2025-01-01 07:00:00 +0900 |
| endDate      | datetime | 記録が終了した日時（該当する時間の終了） (yyyy-mm-dd hh:mm:ss +h:00)   | 2025-01-01 08:00:00 +0900 |
| duration     | float    | `startDate` と `endDate` の差分（秒単位の継続時間）                    | 3600.0                    |
| unit         | str      | `value`の単位                                                          | "count/min"               |
