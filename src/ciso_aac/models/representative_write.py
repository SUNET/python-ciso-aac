import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepresentativeWrite")


@_attrs_define
class RepresentativeWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        email (str):
        entity (UUID):
        create_user (Union[Unset, bool]):  Default: False.
        is_published (Union[Unset, bool]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        role (Union[Unset, str]):
        description (Union[Unset, str]):
        user (Union[None, UUID, Unset]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email: str
    entity: UUID
    create_user: Unset | bool = False
    is_published: Unset | bool = UNSET
    first_name: Unset | str = UNSET
    last_name: Unset | str = UNSET
    phone: Unset | str = UNSET
    role: Unset | str = UNSET
    description: Unset | str = UNSET
    user: None | UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        email = self.email

        entity = str(self.entity)

        create_user = self.create_user

        is_published = self.is_published

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        role = self.role

        description = self.description

        user: None | Unset | str
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "email": email,
                "entity": entity,
            }
        )
        if create_user is not UNSET:
            field_dict["create_user"] = create_user
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
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        email = (None, str(self.email).encode(), "text/plain")

        entity = str(self.entity)

        create_user = (
            self.create_user
            if isinstance(self.create_user, Unset)
            else (None, str(self.create_user).encode(), "text/plain")
        )

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )

        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )

        phone = self.phone if isinstance(self.phone, Unset) else (None, str(self.phone).encode(), "text/plain")

        role = self.role if isinstance(self.role, Unset) else (None, str(self.role).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        user: Unset | tuple[None, bytes, str]

        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = (None, str(self.user).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "email": email,
                "entity": entity,
            }
        )
        if create_user is not UNSET:
            field_dict["create_user"] = create_user
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
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        email = d.pop("email")

        entity = UUID(d.pop("entity"))

        create_user = d.pop("create_user", UNSET)

        is_published = d.pop("is_published", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        role = d.pop("role", UNSET)

        description = d.pop("description", UNSET)

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

        representative_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            email=email,
            entity=entity,
            create_user=create_user,
            is_published=is_published,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            description=description,
            user=user,
        )

        representative_write.additional_properties = d
        return representative_write

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
