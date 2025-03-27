from enum import Enum


class ApiStoredLibrariesListObjectTypeItem(str, Enum):
    FRAMEWORK = "framework"
    REFERENCE_CONTROLS = "reference_controls"
    REQUIREMENT_MAPPING_SET = "requirement_mapping_set"
    RISK_MATRIX = "risk_matrix"
    THREATS = "threats"

    def __str__(self) -> str:
        return str(self.value)
