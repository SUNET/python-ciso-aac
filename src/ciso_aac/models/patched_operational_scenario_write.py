import json
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOperationalScenarioWrite")


@_attrs_define
class PatchedOperationalScenarioWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        is_published (Union[Unset, bool]):
        operating_modes_description (Union[Unset, str]): Description of the operating modes of the operational scenario
        likelihood (Union[Unset, int]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
        ebios_rm_study (Union[Unset, UUID]):
        attack_path (Union[Unset, UUID]):
        threats (Union[Unset, list[UUID]]): Threats leveraged by the operational scenario
    """

    id: Unset | UUID = UNSET
    is_published: Unset | bool = UNSET
    operating_modes_description: Unset | str = UNSET
    likelihood: Unset | int = UNSET
    is_selected: Unset | bool = UNSET
    justification: Unset | str = UNSET
    ebios_rm_study: Unset | UUID = UNSET
    attack_path: Unset | UUID = UNSET
    threats: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = self.is_published

        operating_modes_description = self.operating_modes_description

        likelihood = self.likelihood

        is_selected = self.is_selected

        justification = self.justification

        ebios_rm_study: Unset | str = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        attack_path: Unset | str = UNSET
        if not isinstance(self.attack_path, Unset):
            attack_path = str(self.attack_path)

        threats: Unset | list[str] = UNSET
        if not isinstance(self.threats, Unset):
            threats = []
            for threats_item_data in self.threats:
                threats_item = str(threats_item_data)
                threats.append(threats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if operating_modes_description is not UNSET:
            field_dict["operating_modes_description"] = operating_modes_description
        if likelihood is not UNSET:
            field_dict["likelihood"] = likelihood
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if attack_path is not UNSET:
            field_dict["attack_path"] = attack_path
        if threats is not UNSET:
            field_dict["threats"] = threats

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        operating_modes_description = (
            self.operating_modes_description
            if isinstance(self.operating_modes_description, Unset)
            else (None, str(self.operating_modes_description).encode(), "text/plain")
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

        ebios_rm_study: Unset | bytes = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        attack_path: Unset | bytes = UNSET
        if not isinstance(self.attack_path, Unset):
            attack_path = str(self.attack_path)

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

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if operating_modes_description is not UNSET:
            field_dict["operating_modes_description"] = operating_modes_description
        if likelihood is not UNSET:
            field_dict["likelihood"] = likelihood
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if attack_path is not UNSET:
            field_dict["attack_path"] = attack_path
        if threats is not UNSET:
            field_dict["threats"] = threats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_published = d.pop("is_published", UNSET)

        operating_modes_description = d.pop("operating_modes_description", UNSET)

        likelihood = d.pop("likelihood", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        _ebios_rm_study = d.pop("ebios_rm_study", UNSET)
        ebios_rm_study: Unset | UUID
        if isinstance(_ebios_rm_study, Unset):
            ebios_rm_study = UNSET
        else:
            ebios_rm_study = UUID(_ebios_rm_study)

        _attack_path = d.pop("attack_path", UNSET)
        attack_path: Unset | UUID
        if isinstance(_attack_path, Unset):
            attack_path = UNSET
        else:
            attack_path = UUID(_attack_path)

        threats = []
        _threats = d.pop("threats", UNSET)
        for threats_item_data in _threats or []:
            threats_item = UUID(threats_item_data)

            threats.append(threats_item)

        patched_operational_scenario_write = cls(
            id=id,
            is_published=is_published,
            operating_modes_description=operating_modes_description,
            likelihood=likelihood,
            is_selected=is_selected,
            justification=justification,
            ebios_rm_study=ebios_rm_study,
            attack_path=attack_path,
            threats=threats,
        )

        patched_operational_scenario_write.additional_properties = d
        return patched_operational_scenario_write

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
