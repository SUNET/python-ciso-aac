from enum import Enum


class CsfFunctionEnum(str, Enum):
    DETECT = "detect"
    GOVERN = "govern"
    IDENTIFY = "identify"
    PROTECT = "protect"
    RECOVER = "recover"
    RESPOND = "respond"

    def __str__(self) -> str:
        return str(self.value)
