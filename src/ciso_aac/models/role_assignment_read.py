import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleAssignmentRead")


@_attrs_define
class RoleAssignmentRead:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        role (UUID):
        perimeter_folders (list[UUID]):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        is_recursive (Union[Unset, bool]):
        builtin (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        user (Union[None, UUID, Unset]):
        user_group (Union[None, UUID, Unset]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    role: UUID
    perimeter_folders: list[UUID]
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    is_recursive: Union[Unset, bool] = UNSET
    builtin: Union[Unset, bool] = UNSET
    folder: Union[Unset, UUID] = UNSET
    user: Union[None, UUID, Unset] = UNSET
    user_group: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        role = str(self.role)

        perimeter_folders = []
        for perimeter_folders_item_data in self.perimeter_folders:
            perimeter_folders_item = str(perimeter_folders_item_data)
            perimeter_folders.append(perimeter_folders_item)

        is_published = self.is_published

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_recursive = self.is_recursive

        builtin = self.builtin

        folder: Union[Unset, str] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        user: Union[None, Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = self.user

        user_group: Union[None, Unset, str]
        if isinstance(self.user_group, Unset):
            user_group = UNSET
        elif isinstance(self.user_group, UUID):
            user_group = str(self.user_group)
        else:
            user_group = self.user_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "role": role,
                "perimeter_folders": perimeter_folders,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if is_recursive is not UNSET:
            field_dict["is_recursive"] = is_recursive
        if builtin is not UNSET:
            field_dict["builtin"] = builtin
        if folder is not UNSET:
            field_dict["folder"] = folder
        if user is not UNSET:
            field_dict["user"] = user
        if user_group is not UNSET:
            field_dict["user_group"] = user_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        role = UUID(d.pop("role"))

        perimeter_folders = []
        _perimeter_folders = d.pop("perimeter_folders")
        for perimeter_folders_item_data in _perimeter_folders:
            perimeter_folders_item = UUID(perimeter_folders_item_data)

            perimeter_folders.append(perimeter_folders_item)

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        is_recursive = d.pop("is_recursive", UNSET)

        builtin = d.pop("builtin", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, UUID]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_user(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_type_0 = UUID(data)

                return user_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_user_group(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_group_type_0 = UUID(data)

                return user_group_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        user_group = _parse_user_group(d.pop("user_group", UNSET))

        role_assignment_read = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            role=role,
            perimeter_folders=perimeter_folders,
            is_published=is_published,
            description=description,
            is_recursive=is_recursive,
            builtin=builtin,
            folder=folder,
            user=user,
            user_group=user_group,
        )

        role_assignment_read.additional_properties = d
        return role_assignment_read

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
