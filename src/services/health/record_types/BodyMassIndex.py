# src/services/health/record_types/BodyMass.py

from models.health.record_types import BodyMassIndex
from services.health.health_record_base_service import HealthRecordBaseService
from repositories.health.record_types.BodyMassIndex import (
    GssBodyMassIndexRepository,
    CsvBodyMassIndexRepository)
from utils import SingletonMeta


class BodyMassIndexService(HealthRecordBaseService, metaclass=SingletonMeta):

    def __init__(self):
        self.model_cls = BodyMassIndex
        self.gss_repo = GssBodyMassIndexRepository()
        self.csv_repo = CsvBodyMassIndexRepository()
