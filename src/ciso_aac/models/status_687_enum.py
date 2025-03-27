from enum import Enum


class Status687Enum(str, Enum):
    APPROVED = "approved"
    DEPRECATED = "deprecated"
    DRAFT = "draft"
    EXPIRED = "expired"
    IN_REVIEW = "in_review"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
