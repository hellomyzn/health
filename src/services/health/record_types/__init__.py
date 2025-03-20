""""""

from .BodyMass import BodyMassService
from .BodyMassIndex import BodyMassIndexService
from .HeartRate import HeartRateService
from .Height import HeightService

SERVICE_MAPPING = {
    "HKQuantityTypeIdentifierBodyMass": BodyMassService,
    "HKQuantityTypeIdentifierBodyMassIndex": BodyMassIndexService,
    "HKQuantityTypeIdentifierHeartRate": HeartRateService,
    "HKQuantityTypeIdentifierHeight": HeightService,
}
