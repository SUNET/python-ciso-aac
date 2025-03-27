from enum import Enum


class Status32BEnum(str, Enum):
    EXPLOITABLE = "exploitable"
    FIXED = "fixed"
    MITIGATED = "mitigated"
    POTENTIAL = "potential"
    VALUE_0 = "--"

    def __str__(self) -> str:
        return str(self.value)
