from enum import Enum


class EffortEnum(str, Enum):
    L = "L"
    M = "M"
    S = "S"
    XL = "XL"

    def __str__(self) -> str:
        return str(self.value)
