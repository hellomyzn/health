from dataclasses import dataclass, field
from models.health import HealthBase


@dataclass
class Hoge(HealthBase):
    # 子クラス固有のフィールド
    hoge: str | None = field(default=None)

    @classmethod
    def get_columns(cls) -> list:
        # 親クラスのカラムに"hoge"を追加する
        return super().get_columns() + ["hoge"]

    @classmethod
    def get_key_map(cls) -> dict:
        # 親クラスのキー変換マッピングに"hoge"の対応を追加する
        base_map = super().get_key_map()
        base_map.update({"hoge": "hoge"})
        return base_map

    @classmethod
    def from_dict(cls, d: dict) -> "AppleStandHour":
        # 親クラスから初期化した後、固有フィールドを上書き
        instance = super().from_dict(d)
        instance.hoge = d.get("hoge")
        return instance

    def to_dict(self, without_none_field: bool = False) -> dict:
        # 親クラスの辞書に固有のフィールドを追加する
        data = super().to_dict(without_none_field)
        data["hoge"] = self.hoge
        if without_none_field:
            return {k: v for k, v in data.items() if v is not None}
        return data
