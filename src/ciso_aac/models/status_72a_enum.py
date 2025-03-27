from enum import Enum


class Status72AEnum(str, Enum):
    DEPRECATED = "deprecated"
    DONE = "done"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
