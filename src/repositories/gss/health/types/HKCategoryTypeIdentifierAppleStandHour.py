class HKCategoryTypeIdentifierAppleStandHour:
    """HKCategoryTypeIdentifierAppleStandHour のデータ処理"""

    SHEET_NAME = "AppleStandHour"

    # このデータ固有のカラム
    EXTRA_COLUMNS = ["value"]

    CATEGORY_VALUES = {
        "HKCategoryValueAppleStandHourIdle": 0,
        "HKCategoryValueAppleStandHourStood": 1
    }

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
