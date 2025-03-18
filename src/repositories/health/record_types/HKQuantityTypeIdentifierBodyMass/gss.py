from repositories import GSSBase
from repositories.model_adapter import ModelAdapter
from models.health.record_types import HKQuantityTypeIdentifierBodyMass as model
from utils import SingletonMeta


class GssHKQuantityTypeIdentifierBodyMassRepository(GSSBase, metaclass=SingletonMeta):
    """GssHKQuantityTypeIdentifierBodyMassRepository

    このクラスは SingletonMeta をメタクラスとして指定しているため、
    初回のインスタンス生成時のみ __init__ が実行され、以降は同じインスタンスが再利用されます。
    """

    SHEET_NAME = "BodyMass"

    def __init__(self):
        # この __init__ は初回のみ実行される
        columns = model.get_columns()
        key_map = model.get_key_map()
        adapter = ModelAdapter(model=model, key_map=key_map)
        super().__init__(self.SHEET_NAME, columns, adapter)
