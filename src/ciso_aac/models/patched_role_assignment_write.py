import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRoleAssignmentWrite")


@_attrs_define
class PatchedRoleAssignmentWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        is_recursive (Union[Unset, bool]):
        builtin (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        user (Union[None, UUID, Unset]):
        user_group (Union[None, UUID, Unset]):
        role (Union[Unset, UUID]):
        perimeter_folders (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    is_recursive: Unset | bool = UNSET
    builtin: Unset | bool = UNSET
    folder: Unset | UUID = UNSET
    user: None | UUID | Unset = UNSET
    user_group: None | UUID | Unset = UNSET
    role: Unset | UUID = UNSET
    perimeter_folders: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_recursive = self.is_recursive

        builtin = self.builtin

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        user: None | Unset | str
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = self.user

        user_group: None | Unset | str
        if isinstance(self.user_group, Unset):
            user_group = UNSET
        elif isinstance(self.user_group, UUID):
            user_group = str(self.user_group)
        else:
            user_group = self.user_group

        role: Unset | str = UNSET
        if not isinstance(self.role, Unset):
            role = str(self.role)

        perimeter_folders: Unset | list[str] = UNSET
        if not isinstance(self.perimeter_folders, Unset):
            perimeter_folders = []
            for perimeter_folders_item_data in self.perimeter_folders:
                perimeter_folders_item = str(perimeter_folders_item_data)
                perimeter_folders.append(perimeter_folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
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
        if role is not UNSET:
            field_dict["role"] = role
        if perimeter_folders is not UNSET:
            field_dict["perimeter_folders"] = perimeter_folders

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

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

        is_recursive = (
            self.is_recursive
            if isinstance(self.is_recursive, Unset)
            else (None, str(self.is_recursive).encode(), "text/plain")
        )

        builtin = self.builtin if isinstance(self.builtin, Unset) else (None, str(self.builtin).encode(), "text/plain")

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        user: Unset | tuple[None, bytes, str]

        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = (None, str(self.user).encode(), "text/plain")

        user_group: Unset | tuple[None, bytes, str]

        if isinstance(self.user_group, Unset):
            user_group = UNSET
        elif isinstance(self.user_group, UUID):
            user_group = str(self.user_group)
        else:
            user_group = (None, str(self.user_group).encode(), "text/plain")

        role: Unset | bytes = UNSET
        if not isinstance(self.role, Unset):
            role = str(self.role)

        perimeter_folders: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.perimeter_folders, Unset):
            _temp_perimeter_folders = []
            for perimeter_folders_item_data in self.perimeter_folders:
                perimeter_folders_item = str(perimeter_folders_item_data)
                _temp_perimeter_folders.append(perimeter_folders_item)
            perimeter_folders = (None, json.dumps(_temp_perimeter_folders).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
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
        if role is not UNSET:
            field_dict["role"] = role
        if perimeter_folders is not UNSET:
            field_dict["perimeter_folders"] = perimeter_folders

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

        _created_at = d.pop("created_at", UNSET)
        created_at: Unset | datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Unset | datetime.datetime
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        is_published = d.pop("is_published", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        is_recursive = d.pop("is_recursive", UNSET)

        builtin = d.pop("builtin", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_user(data: object) -> None | UUID | Unset:
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
            return cast(None | UUID | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_user_group(data: object) -> None | UUID | Unset:
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
            return cast(None | UUID | Unset, data)

        user_group = _parse_user_group(d.pop("user_group", UNSET))

        _role = d.pop("role", UNSET)
        role: Unset | UUID
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UUID(_role)

        perimeter_folders = []
        _perimeter_folders = d.pop("perimeter_folders", UNSET)
        for perimeter_folders_item_data in _perimeter_folders or []:
            perimeter_folders_item = UUID(perimeter_folders_item_data)

            perimeter_folders.append(perimeter_folders_item)

        patched_role_assignment_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            name=name,
            description=description,
            is_recursive=is_recursive,
            builtin=builtin,
            folder=folder,
            user=user,
            user_group=user_group,
            role=role,
            perimeter_folders=perimeter_folders,
        )

        patched_role_assignment_write.additional_properties = d
        return patched_role_assignment_write

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
