from services.health import HealthFactory
from repositories import HealthXMLRepository

class HealthService:
    """Apple Health のデータを処理するサービス（高速化対応版）"""

    def __init__(self):
        self.xml_repo = HealthXMLRepository()
        pass

    def parse_and_save(self):
        """
        XMLファイルを1回のパースで処理し、ファイルサイズに基づくプログレスバーで進捗を表示しながら
        CSVにレコードを保存する
        """
        health_data = self.xml_repo.read()

        for record_type, records in health_data.items():

            try:
                service_instance = HealthFactory.create(record_type)
            except ValueError as exc:
                print(f"⚠️ 対応するサービスが見つかりません: {record_type}")
                continue
            # ここで process() を、複数件処理できるように（例：リストを受け取るように）実装
            service_instance.process(records)
