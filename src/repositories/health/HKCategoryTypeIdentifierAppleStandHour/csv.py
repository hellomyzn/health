from repositories import CsvBase
from repositories.model_adapter import ModelAdapter
from models.health import HKCategoryTypeIdentifierAppleStandHour
# from common.config.constant import HK_CSV_PATH  # 例：定数として保存先パスを管理

class CsvHKCategoryTypeIdentifierAppleStandHourRepository(CsvBase):
    # CSV に書き込むカラム名の定義
    KEY_RECORD_TYPE = "record_type"
    KEY_SOURCE_NAME = "sourceName"
    KEY_CREATION_DATE = "creationDate"
    KEY_START_DATE = "startDate"
    KEY_END_DATE = "endDate"
    KEY_DURATION = "duration"
    KEY_UNIT = "unit"
    KEY_VALUE = "value"
    HEADER = [
        KEY_RECORD_TYPE, KEY_SOURCE_NAME, KEY_CREATION_DATE,
        KEY_START_DATE, KEY_END_DATE, KEY_DURATION, KEY_UNIT, KEY_VALUE
    ]

    # ModelAdapter の定義（モデルからCSV出力用リストに変換）
    adapter = ModelAdapter(HKCategoryTypeIdentifierAppleStandHour, {
        "record_type": "record_type",
        "sourceName": "sourceName",
        "creationDate": "creationDate",
        "startDate": "startDate",
        "endDate": "endDate",
        "duration": "duration",
        "unit": "unit",
        "value": "value"
    })

    def __init__(self):
        # 定数 HK_CSV_PATH などからファイルパスを構築（例）
        # file_path = f"{HK_CSV_PATH}/HKCategoryTypeIdentifierAppleStandHour.csv"
        file_path = "sample"
        super().__init__(file_path, self.HEADER, self.adapter)
