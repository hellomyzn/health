import os
try:
    # lxml がインストールされていれば高速にパースできる
    from lxml import etree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from tqdm import tqdm
from models.health_record import HealthRecord
from repositories import HealthXMLRepository
from repositories.health.HKCategoryTypeIdentifierAppleStandHour import GssHKCategoryTypeIdentifierAppleStandHourRepository


JST = timezone(timedelta(hours=9))

class FileWithProgress:
    """
    ファイルオブジェクトをラップし、read時にtqdmの進捗バーを更新するクラス
    """
    def __init__(self, file_obj, pbar):
        self.file_obj = file_obj
        self.pbar = pbar

    def read(self, size):
        data = self.file_obj.read(size)
        self.pbar.update(len(data))
        return data

    def readline(self, *args, **kwargs):
        line = self.file_obj.readline(*args, **kwargs)
        self.pbar.update(len(line))
        return line

    def __iter__(self):
        return iter(self.file_obj)

    def __getattr__(self, attr):
        return getattr(self.file_obj, attr)

class HealthService:
    """Apple Health のデータを処理するサービス（高速化対応版）"""

    def __init__(self, use_google_sheets=False, spreadsheet_id=None):
        self.xml_repo = HealthXMLRepository()
        # Google Sheets 連携が必要な場合は別途対応
        self.gss_repo = GssHKCategoryTypeIdentifierAppleStandHourRepository()

    def hoge(self):
        print(self.gss_repo)
        return 

    def parse_and_save(self, xml_file):
        """
        XMLファイルを1回のパースで処理し、ファイルサイズに基づくプログレスバーで進捗を表示
        """
        total_size = os.path.getsize(xml_file)
        print(f"🔍 処理対象ファイルサイズ: {total_size / (1024*1024):.2f} MB")

        with open(xml_file, 'rb') as f:
            with tqdm(total=total_size, desc="Processing Records", unit="B", unit_scale=True) as pbar:
                file_with_progress = FileWithProgress(f, pbar)
                # lxml/ElementTree の iterparse に直接ラップしたファイルを渡す
                context = ET.iterparse(file_with_progress, events=("start",))
                for event, elem in context:
                    if elem.tag == "Record":
                        record_type = elem.get("type")
                        date_str = elem.get("startDate")
                        # 日時文字列をパースし、日本時間に変換
                        start_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z").astimezone(JST)
                        attributes = {k: v for k, v in elem.attrib.items()}
                        metadata_entries = [
                            {k: v for k, v in meta.attrib.items()}
                            for meta in elem.findall("MetadataEntry")
                        ]
                        record = HealthRecord(record_type, start_date, attributes, metadata_entries)
                        self.xml_repo.save(record)
                    # メモリ解放のため、各要素をクリア
                    elem.clear()
