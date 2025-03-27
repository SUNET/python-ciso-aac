import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.name_enum import NameEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalSettings")


@_attrs_define
class GlobalSettings:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        name (Union[Unset, NameEnum]): * `general` - General
            * `sso` - SSO
        value (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Union[Unset, bool] = UNSET
    name: Union[Unset, NameEnum] = UNSET
    value: Union[Unset, Any] = UNSET
    folder: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        value = self.value

        folder: Union[Unset, str] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        name: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.name, Unset):
            name = (None, str(self.name.value).encode(), "text/plain")

        value = self.value if isinstance(self.value, Unset) else (None, str(self.value).encode(), "text/plain")

        folder: Union[Unset, bytes] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_published = d.pop("is_published", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, NameEnum]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = NameEnum(_name)

        value = d.pop("value", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, UUID]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        global_settings = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            name=name,
            value=value,
            folder=folder,
        )

        global_settings.additional_properties = d
        return global_settings

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
