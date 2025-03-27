import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientSettingsWrite")


@_attrs_define
class ClientSettingsWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (Union[Unset, str]):
        logo (Union[None, Unset, str]):
        favicon (Union[None, Unset, str]):
        show_images_unauthenticated (Union[Unset, bool]): Show logo and favicon to unauthenticated users
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Unset | str = UNSET
    logo: None | Unset | str = UNSET
    favicon: None | Unset | str = UNSET
    show_images_unauthenticated: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

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

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        logo: Unset | tuple[None, bytes, str]

        if isinstance(self.logo, Unset):
            logo = UNSET
        elif isinstance(self.logo, str):
            logo = (None, str(self.logo).encode(), "text/plain")
        else:
            logo = (None, str(self.logo).encode(), "text/plain")

        favicon: Unset | tuple[None, bytes, str]

        if isinstance(self.favicon, Unset):
            favicon = UNSET
        elif isinstance(self.favicon, str):
            favicon = (None, str(self.favicon).encode(), "text/plain")
        else:
            favicon = (None, str(self.favicon).encode(), "text/plain")

        show_images_unauthenticated = (
            self.show_images_unauthenticated
            if isinstance(self.show_images_unauthenticated, Unset)
            else (None, str(self.show_images_unauthenticated).encode(), "text/plain")
        )

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

        client_settings_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            logo=logo,
            favicon=favicon,
            show_images_unauthenticated=show_images_unauthenticated,
        )

        client_settings_write.additional_properties = d
        return client_settings_write

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
