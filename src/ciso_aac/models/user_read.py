import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRead")


@_attrs_define
class UserRead:
    """
    Attributes:
        id (UUID):
        email (str):
        user_groups (list[str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        date_joined (Union[Unset, datetime.datetime]):
        is_sso (Union[Unset, bool]):
        is_third_party (Union[Unset, bool]):
    """

    id: UUID
    email: str
    user_groups: list[str]
    first_name: Unset | str = UNSET
    last_name: Unset | str = UNSET
    is_active: Unset | bool = UNSET
    date_joined: Unset | datetime.datetime = UNSET
    is_sso: Unset | bool = UNSET
    is_third_party: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email = self.email

        user_groups = self.user_groups

        first_name = self.first_name

        last_name = self.last_name

        is_active = self.is_active

        date_joined: Unset | str = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        is_sso = self.is_sso

        is_third_party = self.is_third_party

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "user_groups": user_groups,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if is_sso is not UNSET:
            field_dict["is_sso"] = is_sso
        if is_third_party is not UNSET:
            field_dict["is_third_party"] = is_third_party

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        email = d.pop("email")

        user_groups = cast(list[str], d.pop("user_groups"))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_active = d.pop("is_active", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: Unset | datetime.datetime
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        is_sso = d.pop("is_sso", UNSET)

        is_third_party = d.pop("is_third_party", UNSET)

        user_read = cls(
            id=id,
            email=email,
            user_groups=user_groups,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            date_joined=date_joined,
            is_sso=is_sso,
            is_third_party=is_third_party,
        )

        user_read.additional_properties = d
        return user_read

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
