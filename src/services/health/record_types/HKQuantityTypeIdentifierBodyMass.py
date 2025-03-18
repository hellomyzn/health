# src/services/health/record_types/HKQuantityTypeIdentifierBodyMass.py

from models.health.record_types import HKQuantityTypeIdentifierBodyMass
from services.health.health_record_base_service import HealthRecordBaseService
from repositories.health.record_types.HKQuantityTypeIdentifierBodyMass import (
    GssHKQuantityTypeIdentifierBodyMassRepository,
    CsvHKQuantityTypeIdentifierBodyMassRepository)
from utils import SingletonMeta


class HKQuantityTypeIdentifierBodyMassService(HealthRecordBaseService, metaclass=SingletonMeta):
    """体重（BodyMass）のレコードを処理するサービス"""

    def __init__(self):
        self.model_cls = HKQuantityTypeIdentifierBodyMass
        self.gss_repo = GssHKQuantityTypeIdentifierBodyMassRepository()
        self.csv_repo = CsvHKQuantityTypeIdentifierBodyMassRepository()
