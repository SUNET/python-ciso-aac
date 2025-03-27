from enum import Enum


class StatusAb4Enum(str, Enum):
    DONE = "done"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    TO_DO = "to_do"

    def __str__(self) -> str:
        return str(self.value)
