from enum import Enum


class LcStatusEnum(str, Enum):
    DROPPED = "dropped"
    EOL = "eol"
    IN_DESIGN = "in_design"
    IN_DEV = "in_dev"
    IN_PROD = "in_prod"
    UNDEFINED = "undefined"

    def __str__(self) -> str:
        return str(self.value)
