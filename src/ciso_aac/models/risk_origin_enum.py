from enum import Enum


class RiskOriginEnum(str, Enum):
    ACTIVIST = "activist"
    AMATEUR = "amateur"
    AVENGER = "avenger"
    COMPETITOR = "competitor"
    ORGANIZED_CRIME = "organized_crime"
    PATHOLOGICAL = "pathological"
    STATE = "state"
    TERRORIST = "terrorist"

    def __str__(self) -> str:
        return str(self.value)
