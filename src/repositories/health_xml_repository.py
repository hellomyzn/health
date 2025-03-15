import os
from datetime import timezone, timedelta
from xml.etree.ElementTree import Element, tostring
from models import HealthRecord

JST = timezone(timedelta(hours=9))
XML_OUTPUT_DIR = "src/xml"


class HealthXMLRepository:
    """XML ファイルへの保存を担当"""

    def __init__(self):
        os.makedirs(XML_OUTPUT_DIR, exist_ok=True)

    def save(self, record: HealthRecord):
        """HealthRecord をXMLファイルに保存"""
        year = record.start_date.astimezone(JST).year
        year_dir = os.path.join(XML_OUTPUT_DIR, str(year))
        os.makedirs(year_dir, exist_ok=True)

        file_path = os.path.join(year_dir, f"{record.record_type}.xml")

        # XML 要素の作成
        record_elem = Element("Record", record.attributes)
        for metadata in record.metadata:
            meta_elem = Element("MetadataEntry", metadata)
            record_elem.append(meta_elem)

        # ファイルへ書き込み
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(tostring(record_elem, encoding="unicode") + "\n")
