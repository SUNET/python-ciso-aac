import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSOSettingsRead")


@_attrs_define
class SSOSettingsRead:
    """
    Attributes:
        id (UUID):
        name (str):
        provider (str):
        settings (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        provider_name (str):
        is_published (Union[Unset, bool]):
        is_enabled (Union[Unset, bool]):
        provider_id (Union[Unset, str]):
        client_id (Union[Unset, str]): App ID, or consumer key
        secret (Union[Unset, str]): API secret, client secret, or consumer secret
        key (Union[Unset, str]): Key
        folder (Union[Unset, UUID]):
    """

    id: UUID
    name: str
    provider: str
    settings: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    provider_name: str
    is_published: Unset | bool = UNSET
    is_enabled: Unset | bool = UNSET
    provider_id: Unset | str = UNSET
    client_id: Unset | str = UNSET
    secret: Unset | str = UNSET
    key: Unset | str = UNSET
    folder: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        provider = self.provider

        settings = self.settings

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        provider_name = self.provider_name

        is_published = self.is_published

        is_enabled = self.is_enabled

        provider_id = self.provider_id

        client_id = self.client_id

        secret = self.secret

        key = self.key

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "provider": provider,
                "settings": settings,
                "created_at": created_at,
                "updated_at": updated_at,
                "provider_name": provider_name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if key is not UNSET:
            field_dict["key"] = key
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        provider = d.pop("provider")

        settings = d.pop("settings")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        provider_name = d.pop("provider_name")

        is_published = d.pop("is_published", UNSET)

        is_enabled = d.pop("is_enabled", UNSET)

        provider_id = d.pop("provider_id", UNSET)

        client_id = d.pop("client_id", UNSET)

        secret = d.pop("secret", UNSET)

        key = d.pop("key", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        sso_settings_read = cls(
            id=id,
            name=name,
            provider=provider,
            settings=settings,
            created_at=created_at,
            updated_at=updated_at,
            provider_name=provider_name,
            is_published=is_published,
            is_enabled=is_enabled,
            provider_id=provider_id,
            client_id=client_id,
            secret=secret,
            key=key,
            folder=folder,
        )

        sso_settings_read.additional_properties = d
        return sso_settings_read

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
