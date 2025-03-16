"""repositories.health.types.HKCategoryTypeIdentifierAppleStandHourGSS"""
from repositories import GSSBase
from repositories import ModelAdapter
from repositories.health import Health
from models import HealthRecord


class HKCategoryTypeIdentifierAppleStandHourGSS(Health, GSSBase):
    """HKCategoryTypeIdentifierAppleStandHour のgoogle spread sheetデータ処理"""

    SHEET_NAME = "AppleStandHour"

    CATEGORY_VALUES = {
        "HKCategoryValueAppleStandHourIdle": 0,
        "HKCategoryValueAppleStandHourStood": 1
    }

    def __init__(self, sheet_name="frequency"):
        self.sheet_name = sheet_name
        adapter: ModelAdapter = ModelAdapter(HealthRecord, {
            "id": self.KEY_ID,
            "vocabulary": self.KEY_VOCABULARY,
            "times": self.KEY_TIME,
            "level": self.KEY_LEVEL,
            "eiken_level": self.KEY_EIKEN_LEVEL,
            "school_level": self.KEY_SCHOOL_LEVEL,
            "toeic_level": self.KEY_TOEIC_LEVEL})
        super().__init__(self.sheet_name, self.COLUMNS, adapter)

    @classmethod
    def format_data(cls, record):
        """
        HealthRecord をスプレッドシートに適した形式に変換
        :param record: HealthRecord オブジェクト
        :return: dict (Google Sheets に保存するデータ)
        """
        formatted = {
            "sourceName": record.attributes.get("sourceName"),
            "creationDate": record.attributes.get("creationDate"),
            "startDate": record.attributes.get("startDate"),
            "endDate": record.attributes.get("endDate"),
            "duration": (record.attributes.get("endDate") - record.attributes.get("startDate")).total_seconds(),
            "unit": "count",
            "extra_columns": cls.EXTRA_COLUMNS,
            "value": cls.CATEGORY_VALUES.get(record.attributes.get("value"), -1)  # デフォルト値 -1
        }
        return formatted
