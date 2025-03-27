from enum import Enum


class ConclusionEnum(str, Enum):
    BLOCKER = "blocker"
    NOT_APPLICABLE = "not_applicable"
    OK = "ok"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
