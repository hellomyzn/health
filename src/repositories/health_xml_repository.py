import os
from lxml import etree as ET
from datetime import datetime, timezone, timedelta
from xml.etree.ElementTree import Element, tostring
from tqdm import tqdm

JST = timezone(timedelta(hours=9))
INPUT_FILE = "src/apple_health_export/hoge.xml"
XML_OUTPUT_DIR = "src/xml"


class HealthXMLRepository:
    """XML ファイルへの保存を担当"""

    def __init__(self):
        os.makedirs(XML_OUTPUT_DIR, exist_ok=True)

    def read(self) -> list[dict,]:
        total_size = os.path.getsize(INPUT_FILE)
        print(f"🔍 処理対象ファイルサイズ: {total_size / (1024*1024):.2f} MB")

        # record_type（サービス）毎にレコード（辞書）をまとめる辞書を用意
        grouped_records = {}

        with open(INPUT_FILE, 'rb') as f:
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


                        # TODO xml repoを作成する
                        # そもそもxmlを小分けにして保存しなくても良いからいらない処理
                        attr = {k: v for k, v in elem.attrib.items() }
                        metadatas = [
                            {k: v for k, v in meta.attrib.items()} for meta in elem.findall("MetadataEntry")
                        ]
                        self.save(attr, metadatas, record_type)

                        elem.clear()
        return grouped_records

    def save(self, attr, metadatas, record_type):
        """HealthRecord をXMLファイルに保存"""
        year = datetime.strptime(attr["startDate"], "%Y-%m-%d %H:%M:%S %z").astimezone(JST).year
        # year = attr["startDate"].astimezone(JST).year
        year_dir = os.path.join(XML_OUTPUT_DIR, str(year))
        os.makedirs(year_dir, exist_ok=True)

        file_path = os.path.join(year_dir, f"{record_type}.xml")

        # XML 要素の作成
        record_elem = Element("Record", attr)
        for metadata in metadatas:
            meta_elem = Element("MetadataEntry", metadata)
            record_elem.append(meta_elem)

        # ファイルへ書き込み
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(tostring(record_elem, encoding="unicode") + "\n")


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
