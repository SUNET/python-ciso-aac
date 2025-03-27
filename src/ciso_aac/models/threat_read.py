import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreatRead")


@_attrs_define
class ThreatRead:
    """
    Attributes:
        id (UUID):
        name (str):
        description (Union[None, str]):
        annotation (Union[None, str]):
        folder (str):
        library (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        locale (Union[Unset, str]):
        default_locale (Union[Unset, bool]):
        is_published (Union[Unset, bool]):
    """

    id: UUID
    name: str
    description: Union[None, str]
    annotation: Union[None, str]
    folder: str
    library: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    urn: Union[None, Unset, str] = UNSET
    ref_id: Union[None, Unset, str] = UNSET
    provider: Union[None, Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    default_locale: Union[Unset, bool] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: Union[None, str]
        description = self.description

        annotation: Union[None, str]
        annotation = self.annotation

        folder = self.folder

        library = self.library

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        urn: Union[None, Unset, str]
        if isinstance(self.urn, Unset):
            urn = UNSET
        else:
            urn = self.urn

        ref_id: Union[None, Unset, str]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        provider: Union[None, Unset, str]
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        locale = self.locale

        default_locale = self.default_locale

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "folder": folder,
                "library": library,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if urn is not UNSET:
            field_dict["urn"] = urn
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        def _parse_annotation(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        annotation = _parse_annotation(d.pop("annotation"))

        folder = d.pop("folder")

        library = d.pop("library")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_urn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        urn = _parse_urn(d.pop("urn", UNSET))

        def _parse_ref_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider = _parse_provider(d.pop("provider", UNSET))

        locale = d.pop("locale", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        is_published = d.pop("is_published", UNSET)

        threat_read = cls(
            id=id,
            name=name,
            description=description,
            annotation=annotation,
            folder=folder,
            library=library,
            created_at=created_at,
            updated_at=updated_at,
            urn=urn,
            ref_id=ref_id,
            provider=provider,
            locale=locale,
            default_locale=default_locale,
            is_published=is_published,
        )

        threat_read.additional_properties = d
        return threat_read

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
