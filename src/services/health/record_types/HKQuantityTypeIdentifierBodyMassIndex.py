# src/services/health/record_types/HKQuantityTypeIdentifierBodyMass.py

from models.health.record_types import HKQuantityTypeIdentifierBodyMassIndex
from services.health.health_record_base_service import HealthRecordBaseService
from repositories.health.record_types.HKQuantityTypeIdentifierBodyMassIndex import (
    GssHKQuantityTypeIdentifierBodyMassIndexRepository,
    CsvHKQuantityTypeIdentifierBodyMassIndexRepository)
from utils import SingletonMeta


class HKQuantityTypeIdentifierBodyMassIndexService(HealthRecordBaseService, metaclass=SingletonMeta):

    def __init__(self):
        self.model_cls = HKQuantityTypeIdentifierBodyMassIndex
        self.gss_repo = GssHKQuantityTypeIdentifierBodyMassIndexRepository()
        self.csv_repo = CsvHKQuantityTypeIdentifierBodyMassIndexRepository()
