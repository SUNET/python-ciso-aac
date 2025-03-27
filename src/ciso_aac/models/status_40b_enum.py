from enum import Enum


class Status40BEnum(str, Enum):
    ASSIGNED = "assigned"
    CONFIRMED = "confirmed"
    DEPRECATED = "deprecated"
    DISMISSED = "dismissed"
    IDENTIFIED = "identified"
    IN_PROGRESS = "in_progress"
    MITIGATED = "mitigated"
    RESOLVED = "resolved"
    VALUE_0 = "--"

    def __str__(self) -> str:
        return str(self.value)
