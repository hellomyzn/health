from repositories.health import HealthCsvBase
from repositories.model_adapter import ModelAdapter
from models.health.record_types import HKQuantityTypeIdentifierBodyMass as model


class CsvHKQuantityTypeIdentifierBodyMassRepository(HealthCsvBase):
    """CsvHKQuantityTypeIdentifierBodyMassRepository"""

    FILE_NAME = "BodyMass.csv"

    def __init__(self):
        columns = model.get_columns()
        key_map = model.get_key_map()
        adapter = ModelAdapter(model=model, key_map=key_map)

        super().__init__(path="", header=columns, adapter=adapter)
