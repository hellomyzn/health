"""controllers.sample_controller"""
#########################################################
# Builtin packages
#########################################################
from services.health import HealthService

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

    def __init__(self):
        self.service = HealthService()

    def process_health_data(self, xml_file):
        """XMLデータを処理"""
        self.service.parse_and_save(xml_file)
        print("✅ XML解析 & 保存完了！")
