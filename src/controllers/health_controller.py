"""controllers.sample_controller"""
#########################################################
# Builtin packages
#########################################################
from services import HealthService

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
# (None)


class HealthController:
    """データ処理のエントリーポイント"""

    def __init__(self, use_google_sheets=False, spreadsheet_id=None):
        self.service = HealthService(use_google_sheets, spreadsheet_id)

    def process_health_data(self, xml_file):
        """XMLデータを処理"""
        self.service.parse_and_save(xml_file)
        print("✅ XML解析 & 保存完了！")
