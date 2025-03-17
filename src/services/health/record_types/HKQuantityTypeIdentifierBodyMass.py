# src/services/health/record_types/HKQuantityTypeIdentifierBodyMass.py

from models.health.record_types.HKQuantityTypeIdentifierBodyMass import HKQuantityTypeIdentifierBodyMass
from repositories.health.record_types.HKQuantityTypeIdentifierBodyMass import GssHKQuantityTypeIdentifierBodyMassRepository
from repositories.health.record_types.HKQuantityTypeIdentifierBodyMass import CsvHKQuantityTypeIdentifierBodyMassRepository
from utils import Singleton


class HKQuantityTypeIdentifierBodyMassService(Singleton):
    """体重（BodyMass）のレコードを処理するサービス"""

    def __init__(self):
        self.model_cls = HKQuantityTypeIdentifierBodyMass
        self.gss_repo = GssHKQuantityTypeIdentifierBodyMassRepository()
        self.csv_repo = CsvHKQuantityTypeIdentifierBodyMassRepository()

    def process(self, attributes: dict):
        # モデルインスタンスの生成（from_dict() は HealthBase の仕組みを継承している前提）
        model_instance = self.model_cls.from_dict(attributes)
        # 保存処理例：
        # Google Sheets への保存
        # self.gss_repo.add([model_instance])
        # CSV への保存（CSVリポジトリは dict 形式を受け取る場合の例）
        self.csv_repo.add(model_instance.to_dict(without_none_field=True))
