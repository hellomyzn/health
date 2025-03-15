from datetime import datetime


class HealthRecord:
    """Apple Healthのデータを保持するモデル"""

    def __init__(self, record_type: str, start_date: datetime, attributes: dict, metadata: list):
        self.record_type = record_type
        self.start_date = start_date
        self.attributes = attributes  # Recordの属性
        self.metadata = metadata  # MetadataEntryのリスト

    def to_dict(self):
        """Googleスプレッドシート用の辞書フォーマット"""
        return {
            "Type": self.record_type,
            "StartDate": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            **self.attributes,
            "Metadata": ", ".join([f"{k}={v}" for metadata in self.metadata for k, v in metadata.items()])
        }
