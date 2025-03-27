import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityRead")


@_attrs_define
class EntityRead:
    """
    Attributes:
        id (UUID):
        folder (str):
        owned_folders (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        mission (Union[Unset, str]):
        reference_link (Union[None, Unset, str]):
        builtin (Union[Unset, bool]):
    """

    id: UUID
    folder: str
    owned_folders: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Unset | bool = UNSET
    description: None | Unset | str = UNSET
    mission: Unset | str = UNSET
    reference_link: None | Unset | str = UNSET
    builtin: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        folder = self.folder

        owned_folders = self.owned_folders

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        is_published = self.is_published

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mission = self.mission

        reference_link: None | Unset | str
        if isinstance(self.reference_link, Unset):
            reference_link = UNSET
        else:
            reference_link = self.reference_link

        builtin = self.builtin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "folder": folder,
                "owned_folders": owned_folders,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if mission is not UNSET:
            field_dict["mission"] = mission
        if reference_link is not UNSET:
            field_dict["reference_link"] = reference_link
        if builtin is not UNSET:
            field_dict["builtin"] = builtin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        folder = d.pop("folder")

        owned_folders = cast(list[str], d.pop("owned_folders"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        mission = d.pop("mission", UNSET)

        def _parse_reference_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        reference_link = _parse_reference_link(d.pop("reference_link", UNSET))

        builtin = d.pop("builtin", UNSET)

        entity_read = cls(
            id=id,
            folder=folder,
            owned_folders=owned_folders,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            mission=mission,
            reference_link=reference_link,
            builtin=builtin,
        )

        entity_read.additional_properties = d
        return entity_read

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
