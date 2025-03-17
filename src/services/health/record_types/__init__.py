""""""

from .HKQuantityTypeIdentifierBodyMass import HKQuantityTypeIdentifierBodyMassService
from .HKQuantityTypeIdentifierBodyMassIndex import HKQuantityTypeIdentifierBodyMassIndexService
from .HKQuantityTypeIdentifierHeartRate import HKQuantityTypeIdentifierHeartRateService
from .HKQuantityTypeIdentifierHeight import HKQuantityTypeIdentifierHeightService

SERVICE_MAPPING = {
    "HKQuantityTypeIdentifierBodyMass": HKQuantityTypeIdentifierBodyMassService,
    "HKQuantityTypeIdentifierBodyMassIndex": HKQuantityTypeIdentifierBodyMassIndexService,
    "HKQuantityTypeIdentifierHeartRate": HKQuantityTypeIdentifierHeartRateService,
    "HKQuantityTypeIdentifierHeight": HKQuantityTypeIdentifierHeightService,
}
