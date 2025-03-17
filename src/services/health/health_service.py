import os
import csv
try:
    # lxml がインストールされていれば高速にパースできる
    from lxml import etree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from tqdm import tqdm

JST = timezone(timedelta(hours=9))


def save_record_to_csv(record):
    """
    record は dict 形式で、下記のキーを持つものとする：
      - "record_type": レコードのタイプ文字列
      - "start_date": datetime 型（レコードの開始日時）
      - "data": 辞書（CSVに保存するデータ）
    """
    year = record["start_date"].year
    record_type = record["record_type"]
    # 保存先ディレクトリ（例：output/2025）
    directory = os.path.join("/opt/work/src/csv", str(year))
    os.makedirs(directory, exist_ok=True)
    # ファイルパス例：output/2025/HKQuantityTypeIdentifierHeight.csv
    csv_file = os.path.join(directory, f"{record_type}.csv")

    data = record["data"]
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode="a", encoding="utf-8", newline="") as f:
        # ヘッダーはdataのキーを利用（必要に応じて順序を調整）
        writer = csv.DictWriter(f, fieldnames=list(data.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)


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
        # 今回はXMLからCSVに保存する例としてxml_repoのみ利用
        # self.xml_repo = HealthXMLRepository()
        # ここではGoogle Sheetsリポジトリは使用しない例とする
        pass

    def parse_and_save(self, xml_file):
        """
        XMLファイルを1回のパースで処理し、ファイルサイズに基づくプログレスバーで進捗を表示しながら
        CSVにレコードを保存する
        """
        total_size = os.path.getsize(xml_file)
        print(f"🔍 処理対象ファイルサイズ: {total_size / (1024*1024):.2f} MB")

        with open(xml_file, 'rb') as f:
            with tqdm(total=total_size, desc="Processing Records", unit="B", unit_scale=True) as pbar:
                file_with_progress = FileWithProgress(f, pbar)
                # iterparse でXMLを逐次処理
                context = ET.iterparse(file_with_progress, events=("start",))
                for event, elem in context:
                    if elem.tag == "Record":
                        record_type = elem.get("type")
                        date_str = elem.get("startDate")
                        # 日時文字列をパースし、日本時間に変換
                        start_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z").astimezone(JST)
                        # ここでは、XML要素の属性をそのままCSV保存用データとする
                        data = {k: v for k, v in elem.attrib.items()}
                        # 必要に応じてMetadataEntryの情報を連結するなどの加工も可能
                        record = {
                            "record_type": record_type,
                            "start_date": start_date,
                            "data": data
                        }
                        save_record_to_csv(record)
                    # メモリ節約のため、処理済み要素をクリア
                    elem.clear()
