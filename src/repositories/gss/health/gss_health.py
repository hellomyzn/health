from repositories.gss.gss import GSSBase

class GSSHealth(GSSBase):
    """HealthデータのGoogleスプレッドシート管理"""

    # 共通カラム
    COMMON_COLUMNS = [
        "sourceName", "creationDate", "startDate", "endDate", "duration", "unit"
    ]

    def __init__(self, spreadsheet_id):
        super().__init__(spreadsheet_id)

    def save_health_data(self, sheet_name, record_type, data):
        """
        Healthデータを適切なシートに保存
        :param sheet_name: 保存するシート名
        :param record_type: データの種類 (e.g., HKCategoryTypeIdentifierAppleStandHour)
        :param data: HealthRecordオブジェクトの辞書データ
        """
        columns = self.COMMON_COLUMNS + data.get("extra_columns", [])
        row = [data[col] for col in columns]
        self.add_row(sheet_name, row)
