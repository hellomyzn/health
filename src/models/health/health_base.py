import json
from dataclasses import dataclass, field
from datetime import datetime
from models.model import Model


@dataclass
class HealthBase(Model):
    KEY_ID = "id"
    KEY_SOURCE_NAME = "source_name"
    KEY_CREATION_DATE = "creation_date"
    KEY_START_DATE = "start_date"
    KEY_END_DATE = "end_date"
    KEY_DURATION = "duration"
    KEY_UNIT = "unit"
    KEY_VALUE = "value"

    id: str | None = field(default=None)
    source_name: str | None = field(default=None)
    creation_date: datetime | None = field(default=None)
    start_date: datetime | None = field(default=None)
    end_date: datetime | None = field(default=None)
    duration: float | None = field(default=None)
    unit: str | None = field(default=None)
    value: str | None = field(default=None)

    @classmethod
    def get_columns(cls) -> list:
        return [
            cls.KEY_ID,
            cls.KEY_SOURCE_NAME,
            cls.KEY_CREATION_DATE,
            cls.KEY_START_DATE,
            cls.KEY_END_DATE,
            cls.KEY_DURATION,
            cls.KEY_UNIT,
            cls.KEY_VALUE
        ]

    @classmethod
    def get_key_map(cls) -> dict:
        """to_dict の変換マッピングを返す（リポジトリ側のキーと対応付け）"""
        return {
            "id": cls.KEY_ID,
            "source_name": cls.KEY_SOURCE_NAME,
            "creation_date": cls.KEY_CREATION_DATE,
            "start_date": cls.KEY_START_DATE,
            "end_date": cls.KEY_END_DATE,
            "duration": cls.KEY_DURATION,
            "unit": cls.KEY_UNIT,
            "value": cls.KEY_VALUE
        }

    @classmethod
    def from_dict(cls, dict_: dict) -> "AppleStandHour":
        return cls(
            id=dict_.get(cls.KEY_ID),
            source_name=dict_.get(cls.KEY_SOURCE_NAME),
            creation_date=dict_.get(cls.KEY_CREATION_DATE),
            start_date=dict_.get(cls.KEY_START_DATE),
            end_date=dict_.get(cls.KEY_END_DATE),
            duration=dict_.get(cls.KEY_DURATION),
            unit=dict_.get(cls.KEY_UNIT),
            value=dict_.get(cls.KEY_VALUE)
        )

    def to_dict(self, without_none_field: bool = False) -> dict:
        data = {
            self.KEY_ID: self.id,
            self.KEY_SOURCE_NAME: self.source_name,
            self.KEY_CREATION_DATE: (
                self.creation_date.strftime("%Y-%m-%d %H:%M:%S %z")
                if isinstance(self.creation_date, datetime)
                else self.creation_date
            ),
            self.KEY_START_DATE: (
                self.start_date.strftime("%Y-%m-%d %H:%M:%S %z")
                if isinstance(self.start_date, datetime)
                else self.start_date
            ),
            self.KEY_END_DATE: (
                self.end_date.strftime("%Y-%m-%d %H:%M:%S %z")
                if isinstance(self.end_date, datetime)
                else self.end_date
            ),
            self.KEY_DURATION: self.duration,
            self.KEY_UNIT: self.unit,
            self.KEY_VALUE: self.value
        }
        if without_none_field:
            return {k: v for k, v in data.items() if v is not None}
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)
