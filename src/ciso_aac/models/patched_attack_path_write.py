import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAttackPathWrite")


@_attrs_define
class PatchedAttackPathWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        ref_id (Union[Unset, str]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
        strategic_scenario (Union[Unset, UUID]): Strategic scenario from which the attack path is derived
        stakeholders (Union[Unset, list[UUID]]): Stakeholders leveraged by the attack path
    """

    id: Unset | UUID = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    ref_id: Unset | str = UNSET
    is_selected: Unset | bool = UNSET
    justification: Unset | str = UNSET
    strategic_scenario: Unset | UUID = UNSET
    stakeholders: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = self.is_published

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id = self.ref_id

        is_selected = self.is_selected

        justification = self.justification

        strategic_scenario: Unset | str = UNSET
        if not isinstance(self.strategic_scenario, Unset):
            strategic_scenario = str(self.strategic_scenario)

        stakeholders: Unset | list[str] = UNSET
        if not isinstance(self.stakeholders, Unset):
            stakeholders = []
            for stakeholders_item_data in self.stakeholders:
                stakeholders_item = str(stakeholders_item_data)
                stakeholders.append(stakeholders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if strategic_scenario is not UNSET:
            field_dict["strategic_scenario"] = strategic_scenario
        if stakeholders is not UNSET:
            field_dict["stakeholders"] = stakeholders

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

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        ref_id = self.ref_id if isinstance(self.ref_id, Unset) else (None, str(self.ref_id).encode(), "text/plain")

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

        strategic_scenario: Unset | bytes = UNSET
        if not isinstance(self.strategic_scenario, Unset):
            strategic_scenario = str(self.strategic_scenario)

        stakeholders: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.stakeholders, Unset):
            _temp_stakeholders = []
            for stakeholders_item_data in self.stakeholders:
                stakeholders_item = str(stakeholders_item_data)
                _temp_stakeholders.append(stakeholders_item)
            stakeholders = (None, json.dumps(_temp_stakeholders).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if strategic_scenario is not UNSET:
            field_dict["strategic_scenario"] = strategic_scenario
        if stakeholders is not UNSET:
            field_dict["stakeholders"] = stakeholders

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

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        _strategic_scenario = d.pop("strategic_scenario", UNSET)
        strategic_scenario: Unset | UUID
        if isinstance(_strategic_scenario, Unset):
            strategic_scenario = UNSET
        else:
            strategic_scenario = UUID(_strategic_scenario)

        stakeholders = []
        _stakeholders = d.pop("stakeholders", UNSET)
        for stakeholders_item_data in _stakeholders or []:
            stakeholders_item = UUID(stakeholders_item_data)

            stakeholders.append(stakeholders_item)

        patched_attack_path_write = cls(
            id=id,
            is_published=is_published,
            name=name,
            description=description,
            ref_id=ref_id,
            is_selected=is_selected,
            justification=justification,
            strategic_scenario=strategic_scenario,
            stakeholders=stakeholders,
        )

        patched_attack_path_write.additional_properties = d
        return patched_attack_path_write

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
