from enum import Enum


class StakeholderWriteCategoryEnum(str, Enum):
    CLIENT = "client"
    PARTNER = "partner"
    SUPPLIER = "supplier"

    def __str__(self) -> str:
        return str(self.value)
