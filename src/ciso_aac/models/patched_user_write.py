import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserWrite")


@_attrs_define
class PatchedUserWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        date_joined (Union[Unset, datetime.datetime]):
        user_groups (Union[Unset, list[UUID]]): The user groups this user belongs to. A user will get all permissions
            granted to each of their user groups.
        is_third_party (Union[Unset, bool]):
    """

    id: Unset | UUID = UNSET
    email: Unset | str = UNSET
    first_name: Unset | str = UNSET
    last_name: Unset | str = UNSET
    is_active: Unset | bool = UNSET
    date_joined: Unset | datetime.datetime = UNSET
    user_groups: Unset | list[UUID] = UNSET
    is_third_party: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        is_active = self.is_active

        date_joined: Unset | str = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        user_groups: Unset | list[str] = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = []
            for user_groups_item_data in self.user_groups:
                user_groups_item = str(user_groups_item_data)
                user_groups.append(user_groups_item)

        is_third_party = self.is_third_party

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups
        if is_third_party is not UNSET:
            field_dict["is_third_party"] = is_third_party

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")

        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )

        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )

        date_joined: Unset | bytes = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat().encode()

        user_groups: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.user_groups, Unset):
            _temp_user_groups = []
            for user_groups_item_data in self.user_groups:
                user_groups_item = str(user_groups_item_data)
                _temp_user_groups.append(user_groups_item)
            user_groups = (None, json.dumps(_temp_user_groups).encode(), "application/json")

        is_third_party = (
            self.is_third_party
            if isinstance(self.is_third_party, Unset)
            else (None, str(self.is_third_party).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups
        if is_third_party is not UNSET:
            field_dict["is_third_party"] = is_third_party

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

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_active = d.pop("is_active", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: Unset | datetime.datetime
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        user_groups = []
        _user_groups = d.pop("user_groups", UNSET)
        for user_groups_item_data in _user_groups or []:
            user_groups_item = UUID(user_groups_item_data)

            user_groups.append(user_groups_item)

        is_third_party = d.pop("is_third_party", UNSET)

        patched_user_write = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            date_joined=date_joined,
            user_groups=user_groups,
            is_third_party=is_third_party,
        )

        patched_user_write.additional_properties = d
        return patched_user_write

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
