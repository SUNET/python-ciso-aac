import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedThreatWrite")


@_attrs_define
class PatchedThreatWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        annotation (Union[None, Unset, str]):
        locale (Union[Unset, str]):
        default_locale (Union[Unset, bool]):
        is_published (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        library (Union[None, UUID, Unset]):
    """

    id: Union[Unset, UUID] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    urn: Union[None, Unset, str] = UNSET
    ref_id: Union[None, Unset, str] = UNSET
    provider: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    annotation: Union[None, Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    default_locale: Union[Unset, bool] = UNSET
    is_published: Union[Unset, bool] = UNSET
    folder: Union[Unset, UUID] = UNSET
    library: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        annotation: Union[None, Unset, str]
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        locale = self.locale

        default_locale = self.default_locale

        is_published = self.is_published

        folder: Union[Unset, str] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        library: Union[None, Unset, str]
        if isinstance(self.library, Unset):
            library = UNSET
        elif isinstance(self.library, UUID):
            library = str(self.library)
        else:
            library = self.library

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if urn is not UNSET:
            field_dict["urn"] = urn
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if library is not UNSET:
            field_dict["library"] = library

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Union[Unset, bytes] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        urn: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.urn, Unset):
            urn = UNSET
        elif isinstance(self.urn, str):
            urn = (None, str(self.urn).encode(), "text/plain")
        else:
            urn = (None, str(self.urn).encode(), "text/plain")

        ref_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, str):
            ref_id = (None, str(self.ref_id).encode(), "text/plain")
        else:
            ref_id = (None, str(self.ref_id).encode(), "text/plain")

        provider: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, str):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (None, str(self.provider).encode(), "text/plain")

        name: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, str):
            name = (None, str(self.name).encode(), "text/plain")
        else:
            name = (None, str(self.name).encode(), "text/plain")

        description: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        annotation: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.annotation, Unset):
            annotation = UNSET
        elif isinstance(self.annotation, str):
            annotation = (None, str(self.annotation).encode(), "text/plain")
        else:
            annotation = (None, str(self.annotation).encode(), "text/plain")

        locale = self.locale if isinstance(self.locale, Unset) else (None, str(self.locale).encode(), "text/plain")

        default_locale = (
            self.default_locale
            if isinstance(self.default_locale, Unset)
            else (None, str(self.default_locale).encode(), "text/plain")
        )

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        folder: Union[Unset, bytes] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        library: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.library, Unset):
            library = UNSET
        elif isinstance(self.library, UUID):
            library = str(self.library)
        else:
            library = (None, str(self.library).encode(), "text/plain")

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
        if urn is not UNSET:
            field_dict["urn"] = urn
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if library is not UNSET:
            field_dict["library"] = library

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_annotation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        locale = d.pop("locale", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        is_published = d.pop("is_published", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, UUID]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_library(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                library_type_0 = UUID(data)

                return library_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        library = _parse_library(d.pop("library", UNSET))

        patched_threat_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            urn=urn,
            ref_id=ref_id,
            provider=provider,
            name=name,
            description=description,
            annotation=annotation,
            locale=locale,
            default_locale=default_locale,
            is_published=is_published,
            folder=folder,
            library=library,
        )

        patched_threat_write.additional_properties = d
        return patched_threat_write

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
