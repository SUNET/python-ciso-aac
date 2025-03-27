from enum import Enum


class Category5C3Enum(str, Enum):
    AUDIT = "audit"
    PENTEST = "pentest"
    SELF_IDENTIFIED = "self_identified"
    VALUE_0 = "--"

    def __str__(self) -> str:
        return str(self.value)
