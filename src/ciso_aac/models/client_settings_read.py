import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientSettingsRead")


@_attrs_define
class ClientSettingsRead:
    """
    Attributes:
        id (UUID):
        logo_hash (str):
        favicon_hash (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (Union[Unset, str]):
        logo (Union[None, Unset, str]):
        favicon (Union[None, Unset, str]):
        show_images_unauthenticated (Union[Unset, bool]): Show logo and favicon to unauthenticated users
    """

    id: UUID
    logo_hash: str
    favicon_hash: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Unset | str = UNSET
    logo: None | Unset | str = UNSET
    favicon: None | Unset | str = UNSET
    show_images_unauthenticated: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        logo_hash = self.logo_hash

        favicon_hash = self.favicon_hash

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        logo: None | Unset | str
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        favicon: None | Unset | str
        if isinstance(self.favicon, Unset):
            favicon = UNSET
        else:
            favicon = self.favicon

        show_images_unauthenticated = self.show_images_unauthenticated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "logo_hash": logo_hash,
                "favicon_hash": favicon_hash,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if favicon is not UNSET:
            field_dict["favicon"] = favicon
        if show_images_unauthenticated is not UNSET:
            field_dict["show_images_unauthenticated"] = show_images_unauthenticated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        logo_hash = d.pop("logo_hash")

        favicon_hash = d.pop("favicon_hash")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name", UNSET)

        def _parse_logo(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_favicon(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        favicon = _parse_favicon(d.pop("favicon", UNSET))

        show_images_unauthenticated = d.pop("show_images_unauthenticated", UNSET)

        client_settings_read = cls(
            id=id,
            logo_hash=logo_hash,
            favicon_hash=favicon_hash,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            logo=logo,
            favicon=favicon,
            show_images_unauthenticated=show_images_unauthenticated,
        )

        client_settings_read.additional_properties = d
        return client_settings_read

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
