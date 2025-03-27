from enum import Enum


class ResultEnum(str, Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_APPLICABLE = "not_applicable"
    NOT_ASSESSED = "not_assessed"
    PARTIALLY_COMPLIANT = "partially_compliant"

    def __str__(self) -> str:
        return str(self.value)
