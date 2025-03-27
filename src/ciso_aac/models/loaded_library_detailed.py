import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadedLibraryDetailed")


@_attrs_define
class LoadedLibraryDetailed:
    """
    Attributes:
        id (UUID):
        name (str):
        description (Union[None, str]):
        annotation (Union[None, str]):
        locales (list[Any]):
        dependencies (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        urn (Union[None, str]):
        version (int):
        is_published (Union[Unset, bool]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        locale (Union[Unset, str]):  Default: 'en'.
        default_locale (Union[Unset, bool]):
        copyright_ (Union[None, Unset, str]):
        packager (Union[None, Unset, str]): Packager of the library
        publication_date (Union[None, Unset, datetime.date]):
        builtin (Union[Unset, bool]):
        objects_meta (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
    """

    id: UUID
    name: str
    description: None | str
    annotation: None | str
    locales: list[Any]
    dependencies: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    urn: None | str
    version: int
    is_published: Unset | bool = UNSET
    ref_id: None | Unset | str = UNSET
    provider: None | Unset | str = UNSET
    locale: Unset | str = "en"
    default_locale: Unset | bool = UNSET
    copyright_: None | Unset | str = UNSET
    packager: None | Unset | str = UNSET
    publication_date: None | Unset | datetime.date = UNSET
    builtin: Unset | bool = UNSET
    objects_meta: Unset | Any = UNSET
    folder: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        annotation: None | str
        annotation = self.annotation

        locales = self.locales

        dependencies = self.dependencies

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        urn: None | str
        urn = self.urn

        version = self.version

        is_published = self.is_published

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        provider: None | Unset | str
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        locale = self.locale

        default_locale = self.default_locale

        copyright_: None | Unset | str
        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        else:
            copyright_ = self.copyright_

        packager: None | Unset | str
        if isinstance(self.packager, Unset):
            packager = UNSET
        else:
            packager = self.packager

        publication_date: None | Unset | str
        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        elif isinstance(self.publication_date, datetime.date):
            publication_date = self.publication_date.isoformat()
        else:
            publication_date = self.publication_date

        builtin = self.builtin

        objects_meta = self.objects_meta

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "locales": locales,
                "dependencies": dependencies,
                "created_at": created_at,
                "updated_at": updated_at,
                "urn": urn,
                "version": version,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if packager is not UNSET:
            field_dict["packager"] = packager
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if builtin is not UNSET:
            field_dict["builtin"] = builtin
        if objects_meta is not UNSET:
            field_dict["objects_meta"] = objects_meta
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        name = (None, str(self.name).encode(), "text/plain")

        description: tuple[None, bytes, str]

        if isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        annotation: tuple[None, bytes, str]

        if isinstance(self.annotation, str):
            annotation = (None, str(self.annotation).encode(), "text/plain")
        else:
            annotation = (None, str(self.annotation).encode(), "text/plain")

        _temp_locales = self.locales
        locales = (None, json.dumps(_temp_locales).encode(), "application/json")

        _temp_dependencies = self.dependencies
        dependencies = (None, json.dumps(_temp_dependencies).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        urn: tuple[None, bytes, str]

        if isinstance(self.urn, str):
            urn = (None, str(self.urn).encode(), "text/plain")
        else:
            urn = (None, str(self.urn).encode(), "text/plain")

        version = (None, str(self.version).encode(), "text/plain")

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        ref_id: Unset | tuple[None, bytes, str]

        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, str):
            ref_id = (None, str(self.ref_id).encode(), "text/plain")
        else:
            ref_id = (None, str(self.ref_id).encode(), "text/plain")

        provider: Unset | tuple[None, bytes, str]

        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, str):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (None, str(self.provider).encode(), "text/plain")

        locale = self.locale if isinstance(self.locale, Unset) else (None, str(self.locale).encode(), "text/plain")

        default_locale = (
            self.default_locale
            if isinstance(self.default_locale, Unset)
            else (None, str(self.default_locale).encode(), "text/plain")
        )

        copyright_: Unset | tuple[None, bytes, str]

        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        elif isinstance(self.copyright_, str):
            copyright_ = (None, str(self.copyright_).encode(), "text/plain")
        else:
            copyright_ = (None, str(self.copyright_).encode(), "text/plain")

        packager: Unset | tuple[None, bytes, str]

        if isinstance(self.packager, Unset):
            packager = UNSET
        elif isinstance(self.packager, str):
            packager = (None, str(self.packager).encode(), "text/plain")
        else:
            packager = (None, str(self.packager).encode(), "text/plain")

        publication_date: Unset | tuple[None, bytes, str]

        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        elif isinstance(self.publication_date, datetime.date):
            publication_date = self.publication_date.isoformat().encode()
        else:
            publication_date = (None, str(self.publication_date).encode(), "text/plain")

        builtin = self.builtin if isinstance(self.builtin, Unset) else (None, str(self.builtin).encode(), "text/plain")

        objects_meta = (
            self.objects_meta
            if isinstance(self.objects_meta, Unset)
            else (None, str(self.objects_meta).encode(), "text/plain")
        )

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "locales": locales,
                "dependencies": dependencies,
                "created_at": created_at,
                "updated_at": updated_at,
                "urn": urn,
                "version": version,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if packager is not UNSET:
            field_dict["packager"] = packager
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if builtin is not UNSET:
            field_dict["builtin"] = builtin
        if objects_meta is not UNSET:
            field_dict["objects_meta"] = objects_meta
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        locales = cast(list[Any], d.pop("locales"))

        dependencies = cast(list[str], d.pop("dependencies"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_urn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        urn = _parse_urn(d.pop("urn"))

        version = d.pop("version")

        is_published = d.pop("is_published", UNSET)

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_provider(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        locale = d.pop("locale", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        def _parse_copyright_(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        copyright_ = _parse_copyright_(d.pop("copyright", UNSET))

        def _parse_packager(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        packager = _parse_packager(d.pop("packager", UNSET))

        def _parse_publication_date(data: object) -> None | Unset | datetime.date:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_date_type_0 = isoparse(data).date()

                return publication_date_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.date, data)

        publication_date = _parse_publication_date(d.pop("publication_date", UNSET))

        builtin = d.pop("builtin", UNSET)

        objects_meta = d.pop("objects_meta", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        loaded_library_detailed = cls(
            id=id,
            name=name,
            description=description,
            annotation=annotation,
            locales=locales,
            dependencies=dependencies,
            created_at=created_at,
            updated_at=updated_at,
            urn=urn,
            version=version,
            is_published=is_published,
            ref_id=ref_id,
            provider=provider,
            locale=locale,
            default_locale=default_locale,
            copyright_=copyright_,
            packager=packager,
            publication_date=publication_date,
            builtin=builtin,
            objects_meta=objects_meta,
            folder=folder,
        )

        loaded_library_detailed.additional_properties = d
        return loaded_library_detailed

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
