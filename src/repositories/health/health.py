"""repositories.health.health"""
#########################################################
# Builtin packages
#########################################################
# (None)

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from repositories import ModelAdapter

class Health():
    """gss health repository"""
    KEY_ID = "id"
    KEY_SOURCE_NAME = "source_name"
    KEY_CREATION_DATE = "creation_date"
    KEY_START_DATE = "start_date"
    KEY_END_DATE = "end_date"
    KEY_DURATION = "duration"
    KEY_UNIT = "unit"
    KEY_VALUE = "value"
    COLUMNS = [KEY_ID, KEY_SOURCE_NAME, KEY_CREATION_DATE,
            KEY_START_DATE, KEY_END_DATE, KEY_DURATION,
            KEY_UNIT, KEY_VALUE]

    def __init__(self, sheet_name="frequency"):
        adapter: ModelAdapter = ModelAdapter(HealthRecord, {
            "id": self.KEY_ID,
            "vocabulary": self.KEY_VOCABULARY,
            "times": self.KEY_TIME,
            "level": self.KEY_LEVEL,
            "eiken_level": self.KEY_EIKEN_LEVEL,
            "school_level": self.KEY_SCHOOL_LEVEL,
            "toeic_level": self.KEY_TOEIC_LEVEL})