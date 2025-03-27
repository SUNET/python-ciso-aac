import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationalScenarioRead")


@_attrs_define
class OperationalScenarioRead:
    """
    Attributes:
        id (UUID):
        str_ (str):
        ebios_rm_study (str):
        folder (str):
        attack_path (str):
        stakeholders (list[str]):
        ro_to (str):
        threats (list[str]):
        likelihood (Any):
        gravity (Any):
        risk_level (Any):
        ref_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        operating_modes_description (str): Description of the operating modes of the operational scenario
        is_published (Union[Unset, bool]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
    """

    id: UUID
    str_: str
    ebios_rm_study: str
    folder: str
    attack_path: str
    stakeholders: list[str]
    ro_to: str
    threats: list[str]
    likelihood: Any
    gravity: Any
    risk_level: Any
    ref_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    operating_modes_description: str
    is_published: Unset | bool = UNSET
    is_selected: Unset | bool = UNSET
    justification: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        str_ = self.str_

        ebios_rm_study = self.ebios_rm_study

        folder = self.folder

        attack_path = self.attack_path

        stakeholders = self.stakeholders

        ro_to = self.ro_to

        threats = self.threats

        likelihood = self.likelihood

        gravity = self.gravity

        risk_level = self.risk_level

        ref_id = self.ref_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        operating_modes_description = self.operating_modes_description

        is_published = self.is_published

        is_selected = self.is_selected

        justification = self.justification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "str": str_,
                "ebios_rm_study": ebios_rm_study,
                "folder": folder,
                "attack_path": attack_path,
                "stakeholders": stakeholders,
                "ro_to": ro_to,
                "threats": threats,
                "likelihood": likelihood,
                "gravity": gravity,
                "risk_level": risk_level,
                "ref_id": ref_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "operating_modes_description": operating_modes_description,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        str_ = d.pop("str")

        ebios_rm_study = d.pop("ebios_rm_study")

        folder = d.pop("folder")

        attack_path = d.pop("attack_path")

        stakeholders = cast(list[str], d.pop("stakeholders"))

        ro_to = d.pop("ro_to")

        threats = cast(list[str], d.pop("threats"))

        likelihood = d.pop("likelihood")

        gravity = d.pop("gravity")

        risk_level = d.pop("risk_level")

        ref_id = d.pop("ref_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        operating_modes_description = d.pop("operating_modes_description")

        is_published = d.pop("is_published", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        operational_scenario_read = cls(
            id=id,
            str_=str_,
            ebios_rm_study=ebios_rm_study,
            folder=folder,
            attack_path=attack_path,
            stakeholders=stakeholders,
            ro_to=ro_to,
            threats=threats,
            likelihood=likelihood,
            gravity=gravity,
            risk_level=risk_level,
            ref_id=ref_id,
            created_at=created_at,
            updated_at=updated_at,
            operating_modes_description=operating_modes_description,
            is_published=is_published,
            is_selected=is_selected,
            justification=justification,
        )

        operational_scenario_read.additional_properties = d
        return operational_scenario_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
