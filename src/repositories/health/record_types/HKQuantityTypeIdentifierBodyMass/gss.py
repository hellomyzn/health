from repositories import GSSBase
from repositories.model_adapter import ModelAdapter
from models.health.record_types import HKQuantityTypeIdentifierBodyMass as model
from utils import Singleton


class GssHKQuantityTypeIdentifierBodyMassRepository(GSSBase, Singleton):
    """GssHKQuantityTypeIdentifierBodyMassRepository"""

    SHEET_NAME = "BodyMass"

    def __init__(self):
        columns = model.get_columns()
        key_map = model.get_key_map()

        adapter = ModelAdapter(model=model, key_map=key_map)
        super().__init__(self.SHEET_NAME, columns, adapter)
