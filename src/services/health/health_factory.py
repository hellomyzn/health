
from services.health.record_types import BodyMassService
from services.health.record_types import BodyMassIndexService
from services.health.record_types import HeartRateService
from services.health.record_types import HeightService

SERVICE_MAPPING = {
    "HKQuantityTypeIdentifierBodyMass": BodyMassService,
    "HKQuantityTypeIdentifierBodyMassIndex": BodyMassIndexService,
    "HKQuantityTypeIdentifierHeartRate": HeartRateService,
    "HKQuantityTypeIdentifierHeight": HeightService,
}


class HealthFactory():
    @staticmethod
    def create(record_type: str):
        service_cls = SERVICE_MAPPING.get(record_type)
        if not service_cls:
            raise ValueError(f"Unsupported record_type: {record_type}")
        return service_cls()  # or DIContainer.resolve(service_cls)
