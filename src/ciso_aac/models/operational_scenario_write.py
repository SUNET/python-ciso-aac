import json
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationalScenarioWrite")


@_attrs_define
class OperationalScenarioWrite:
    """
    Attributes:
        id (UUID):
        operating_modes_description (str): Description of the operating modes of the operational scenario
        ebios_rm_study (UUID):
        attack_path (UUID):
        is_published (Union[Unset, bool]):
        likelihood (Union[Unset, int]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
        threats (Union[Unset, list[UUID]]): Threats leveraged by the operational scenario
    """

    id: UUID
    operating_modes_description: str
    ebios_rm_study: UUID
    attack_path: UUID
    is_published: Unset | bool = UNSET
    likelihood: Unset | int = UNSET
    is_selected: Unset | bool = UNSET
    justification: Unset | str = UNSET
    threats: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        operating_modes_description = self.operating_modes_description

        ebios_rm_study = str(self.ebios_rm_study)

        attack_path = str(self.attack_path)

        is_published = self.is_published

        likelihood = self.likelihood

        is_selected = self.is_selected

        justification = self.justification

        threats: Unset | list[str] = UNSET
        if not isinstance(self.threats, Unset):
            threats = []
            for threats_item_data in self.threats:
                threats_item = str(threats_item_data)
                threats.append(threats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "operating_modes_description": operating_modes_description,
                "ebios_rm_study": ebios_rm_study,
                "attack_path": attack_path,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if likelihood is not UNSET:
            field_dict["likelihood"] = likelihood
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if threats is not UNSET:
            field_dict["threats"] = threats

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        operating_modes_description = (None, str(self.operating_modes_description).encode(), "text/plain")

        ebios_rm_study = str(self.ebios_rm_study)

        attack_path = str(self.attack_path)

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        likelihood = (
            self.likelihood
            if isinstance(self.likelihood, Unset)
            else (None, str(self.likelihood).encode(), "text/plain")
        )

        is_selected = (
            self.is_selected
            if isinstance(self.is_selected, Unset)
            else (None, str(self.is_selected).encode(), "text/plain")
        )

        justification = (
            self.justification
            if isinstance(self.justification, Unset)
            else (None, str(self.justification).encode(), "text/plain")
        )

        threats: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.threats, Unset):
            _temp_threats = []
            for threats_item_data in self.threats:
                threats_item = str(threats_item_data)
                _temp_threats.append(threats_item)
            threats = (None, json.dumps(_temp_threats).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "operating_modes_description": operating_modes_description,
                "ebios_rm_study": ebios_rm_study,
                "attack_path": attack_path,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if likelihood is not UNSET:
            field_dict["likelihood"] = likelihood
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if threats is not UNSET:
            field_dict["threats"] = threats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        operating_modes_description = d.pop("operating_modes_description")

        ebios_rm_study = UUID(d.pop("ebios_rm_study"))

        attack_path = UUID(d.pop("attack_path"))

        is_published = d.pop("is_published", UNSET)

        likelihood = d.pop("likelihood", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        threats = []
        _threats = d.pop("threats", UNSET)
        for threats_item_data in _threats or []:
            threats_item = UUID(threats_item_data)

            threats.append(threats_item)

        operational_scenario_write = cls(
            id=id,
            operating_modes_description=operating_modes_description,
            ebios_rm_study=ebios_rm_study,
            attack_path=attack_path,
            is_published=is_published,
            likelihood=likelihood,
            is_selected=is_selected,
            justification=justification,
            threats=threats,
        )

        operational_scenario_write.additional_properties = d
        return operational_scenario_write

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
