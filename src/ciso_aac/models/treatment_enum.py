from enum import Enum


class TreatmentEnum(str, Enum):
    ACCEPT = "accept"
    AVOID = "avoid"
    MITIGATE = "mitigate"
    OPEN = "open"
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
