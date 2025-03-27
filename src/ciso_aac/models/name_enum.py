from enum import Enum


class NameEnum(str, Enum):
    GENERAL = "general"
    SSO = "sso"

    def __str__(self) -> str:
        return str(self.value)
