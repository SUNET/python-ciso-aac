from enum import Enum


class Status2E9Enum(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    TO_DO = "to_do"
    VALUE_5 = "--"

    def __str__(self) -> str:
        return str(self.value)
