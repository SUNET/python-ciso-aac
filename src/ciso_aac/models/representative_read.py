import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepresentativeRead")


@_attrs_define
class RepresentativeRead:
    """
    Attributes:
        id (UUID):
        entity (str):
        user (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        email (str):
        is_published (Union[Unset, bool]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        role (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    id: UUID
    entity: str
    user: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email: str
    is_published: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        entity = self.entity

        user = self.user

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        email = self.email

        is_published = self.is_published

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        role = self.role

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "entity": entity,
                "user": user,
                "created_at": created_at,
                "updated_at": updated_at,
                "email": email,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        entity = d.pop("entity")

        user = d.pop("user")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        email = d.pop("email")

        is_published = d.pop("is_published", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        role = d.pop("role", UNSET)

        description = d.pop("description", UNSET)

        representative_read = cls(
            id=id,
            entity=entity,
            user=user,
            created_at=created_at,
            updated_at=updated_at,
            email=email,
            is_published=is_published,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            description=description,
        )

        representative_read.additional_properties = d
        return representative_read

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
