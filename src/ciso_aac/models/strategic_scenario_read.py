import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StrategicScenarioRead")


@_attrs_define
class StrategicScenarioRead:
    """
    Attributes:
        id (UUID):
        ebios_rm_study (str):
        folder (str):
        ro_to_couple (str):
        gravity (Any):
        attack_paths (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        ref_id (Union[Unset, str]):
    """

    id: UUID
    ebios_rm_study: str
    folder: str
    ro_to_couple: str
    gravity: Any
    attack_paths: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    ref_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        ebios_rm_study = self.ebios_rm_study

        folder = self.folder

        ro_to_couple = self.ro_to_couple

        gravity = self.gravity

        attack_paths = self.attack_paths

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

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
                "ebios_rm_study": ebios_rm_study,
                "folder": folder,
                "ro_to_couple": ro_to_couple,
                "gravity": gravity,
                "attack_paths": attack_paths,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
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

        ebios_rm_study = d.pop("ebios_rm_study")

        folder = d.pop("folder")

        ro_to_couple = d.pop("ro_to_couple")

        gravity = d.pop("gravity")

        attack_paths = cast(list[str], d.pop("attack_paths"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        strategic_scenario_read = cls(
            id=id,
            ebios_rm_study=ebios_rm_study,
            folder=folder,
            ro_to_couple=ro_to_couple,
            gravity=gravity,
            attack_paths=attack_paths,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            ref_id=ref_id,
        )

        strategic_scenario_read.additional_properties = d
        return strategic_scenario_read

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
