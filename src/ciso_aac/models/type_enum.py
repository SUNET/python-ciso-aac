from enum import Enum


class TypeEnum(str, Enum):
    PR = "PR"
    SP = "SP"

    def __str__(self) -> str:
        return str(self.value)
