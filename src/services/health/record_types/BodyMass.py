# src/services/health/record_types/BodyMass.py

from models.health.record_types import BodyMass
from services.health.health_record_base_service import HealthRecordBaseService
from repositories.health.record_types.BodyMass import (
    GssBodyMassRepository,
    CsvBodyMassRepository)
from utils import SingletonMeta


class BodyMassService(HealthRecordBaseService, metaclass=SingletonMeta):
    """体重（BodyMass）のレコードを処理するサービス"""

    def __init__(self):
        self.model_cls = BodyMass
        self.gss_repo = GssBodyMassRepository()
        self.csv_repo = CsvBodyMassRepository()
