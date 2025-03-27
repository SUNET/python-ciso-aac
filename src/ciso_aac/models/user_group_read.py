import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroupRead")


@_attrs_define
class UserGroupRead:
    """
    Attributes:
        id (UUID):
        name (str):
        localization_dict (Any):
        folder (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        builtin (Union[Unset, bool]):
    """

    id: UUID
    name: str
    localization_dict: Any
    folder: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    builtin: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        localization_dict = self.localization_dict

        folder = self.folder

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        builtin = self.builtin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "localization_dict": localization_dict,
                "folder": folder,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if builtin is not UNSET:
            field_dict["builtin"] = builtin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        localization_dict = d.pop("localization_dict")

        folder = d.pop("folder")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        builtin = d.pop("builtin", UNSET)

        user_group_read = cls(
            id=id,
            name=name,
            localization_dict=localization_dict,
            folder=folder,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            description=description,
            builtin=builtin,
        )

        user_group_read.additional_properties = d
        return user_group_read

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
