from enum import Enum


class CategoryAe3Enum(str, Enum):
    PHYSICAL = "physical"
    POLICY = "policy"
    PROCEDURE = "procedure"
    PROCESS = "process"
    TECHNICAL = "technical"

    def __str__(self) -> str:
        return str(self.value)
