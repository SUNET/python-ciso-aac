from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StrategicScenarioWrite")


@_attrs_define
class StrategicScenarioWrite:
    """
    Attributes:
        id (UUID):
        name (str):
        ebios_rm_study (UUID):
        ro_to_couple (UUID): RO/TO couple from which the attach path is derived
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        ref_id (Union[Unset, str]):
    """

    id: UUID
    name: str
    ebios_rm_study: UUID
    ro_to_couple: UUID
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    ref_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        ebios_rm_study = str(self.ebios_rm_study)

        ro_to_couple = str(self.ro_to_couple)

        is_published = self.is_published

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id = self.ref_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ebios_rm_study": ebios_rm_study,
                "ro_to_couple": ro_to_couple,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        name = (None, str(self.name).encode(), "text/plain")

        ebios_rm_study = str(self.ebios_rm_study)

        ro_to_couple = str(self.ro_to_couple)

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        description: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        ref_id = self.ref_id if isinstance(self.ref_id, Unset) else (None, str(self.ref_id).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "name": name,
                "ebios_rm_study": ebios_rm_study,
                "ro_to_couple": ro_to_couple,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        ebios_rm_study = UUID(d.pop("ebios_rm_study"))

        ro_to_couple = UUID(d.pop("ro_to_couple"))

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        strategic_scenario_write = cls(
            id=id,
            name=name,
            ebios_rm_study=ebios_rm_study,
            ro_to_couple=ro_to_couple,
            is_published=is_published,
            description=description,
            ref_id=ref_id,
        )

        strategic_scenario_write.additional_properties = d
        return strategic_scenario_write

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
