import os
import csv
try:
    # lxml がインストールされていれば高速にパースできる
    from lxml import etree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from tqdm import tqdm

from services.health.record_types import SERVICE_MAPPING

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

    def __init__(self):
        pass

    def parse_and_save(self, xml_file):
        """
        XMLファイルを1回のパースで処理し、ファイルサイズに基づくプログレスバーで進捗を表示しながら
        CSVにレコードを保存する
        """
        total_size = os.path.getsize(xml_file)
        print(f"🔍 処理対象ファイルサイズ: {total_size / (1024*1024):.2f} MB")

        # record_type（サービス）毎にレコード（辞書）をまとめる辞書を用意
        grouped_records = {}

        with open(xml_file, 'rb') as f:
            with tqdm(total=total_size, desc="Processing Records", unit="B", unit_scale=True) as pbar:
                file_with_progress = FileWithProgress(f, pbar)
                # iterparse でXMLを逐次処理
                context = ET.iterparse(file_with_progress, events=("start",))
                for _, elem in context:
                    if elem.tag == "Record":
                        record_type = elem.get("type")
                        id_ = None
                        source_name = elem.get("sourceName")
                        creation_date_str = elem.get("creationDate")
                        start_date_str = elem.get("startDate")
                        end_date_str = elem.get("endDate")
                        unit = elem.get("unit")
                        duration = None
                        value = elem.get("value")

                        # 日時文字列をパースし、日本時間に変換
                        creation_date = datetime.strptime(creation_date_str, "%Y-%m-%d %H:%M:%S %z").astimezone(JST)
                        start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S %z").astimezone(JST)
                        end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S %z").astimezone(JST)
                        duration = (end_date - start_date).total_seconds()

                        data = {
                            "id": id_,
                            "source_name": source_name,
                            "creation_date": creation_date,
                            "start_date": start_date,
                            "end_date": end_date,
                            "unit": unit,
                            "duration": duration,
                            "value": value
                        }

                        grouped_records.setdefault(record_type, []).append(data)
                        elem.clear()

        for record_type, records in grouped_records.items():
            service_cls = SERVICE_MAPPING.get(record_type)
            if service_cls is None:
                print(f"⚠️ 対応するサービスが見つかりません: {record_type}")
                continue
            service_instance = service_cls()
            # ここで process() を、複数件処理できるように（例：リストを受け取るように）実装
            service_instance.process(records)
