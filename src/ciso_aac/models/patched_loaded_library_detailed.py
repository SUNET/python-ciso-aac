import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLoadedLibraryDetailed")


@_attrs_define
class PatchedLoadedLibraryDetailed:
    """
    Attributes:
        id (Union[Unset, UUID]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        annotation (Union[None, Unset, str]):
        locales (Union[Unset, list[Any]]):
        dependencies (Union[Unset, list[str]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_published (Union[Unset, bool]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        locale (Union[Unset, str]):  Default: 'en'.
        default_locale (Union[Unset, bool]):
        urn (Union[None, Unset, str]):
        copyright_ (Union[None, Unset, str]):
        version (Union[Unset, int]):
        packager (Union[None, Unset, str]): Packager of the library
        publication_date (Union[None, Unset, datetime.date]):
        builtin (Union[Unset, bool]):
        objects_meta (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
    """

    id: Unset | UUID = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    annotation: None | Unset | str = UNSET
    locales: Unset | list[Any] = UNSET
    dependencies: Unset | list[str] = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    is_published: Unset | bool = UNSET
    ref_id: None | Unset | str = UNSET
    provider: None | Unset | str = UNSET
    locale: Unset | str = "en"
    default_locale: Unset | bool = UNSET
    urn: None | Unset | str = UNSET
    copyright_: None | Unset | str = UNSET
    version: Unset | int = UNSET
    packager: None | Unset | str = UNSET
    publication_date: None | Unset | datetime.date = UNSET
    builtin: Unset | bool = UNSET
    objects_meta: Unset | Any = UNSET
    folder: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        annotation: None | Unset | str
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        locales: Unset | list[Any] = UNSET
        if not isinstance(self.locales, Unset):
            locales = self.locales

        dependencies: Unset | list[str] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

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

        urn: None | Unset | str
        if isinstance(self.urn, Unset):
            urn = UNSET
        else:
            urn = self.urn

        copyright_: None | Unset | str
        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        else:
            copyright_ = self.copyright_

        version = self.version

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if locales is not UNSET:
            field_dict["locales"] = locales
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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
        if urn is not UNSET:
            field_dict["urn"] = urn
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if version is not UNSET:
            field_dict["version"] = version
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
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        annotation: Unset | tuple[None, bytes, str]

        if isinstance(self.annotation, Unset):
            annotation = UNSET
        elif isinstance(self.annotation, str):
            annotation = (None, str(self.annotation).encode(), "text/plain")
        else:
            annotation = (None, str(self.annotation).encode(), "text/plain")

        locales: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.locales, Unset):
            _temp_locales = self.locales
            locales = (None, json.dumps(_temp_locales).encode(), "application/json")

        dependencies: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.dependencies, Unset):
            _temp_dependencies = self.dependencies
            dependencies = (None, json.dumps(_temp_dependencies).encode(), "application/json")

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

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

        urn: Unset | tuple[None, bytes, str]

        if isinstance(self.urn, Unset):
            urn = UNSET
        elif isinstance(self.urn, str):
            urn = (None, str(self.urn).encode(), "text/plain")
        else:
            urn = (None, str(self.urn).encode(), "text/plain")

        copyright_: Unset | tuple[None, bytes, str]

        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        elif isinstance(self.copyright_, str):
            copyright_ = (None, str(self.copyright_).encode(), "text/plain")
        else:
            copyright_ = (None, str(self.copyright_).encode(), "text/plain")

        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")

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

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if locales is not UNSET:
            field_dict["locales"] = locales
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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
        if urn is not UNSET:
            field_dict["urn"] = urn
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if version is not UNSET:
            field_dict["version"] = version
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
        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_annotation(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        locales = cast(list[Any], d.pop("locales", UNSET))

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Unset | datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Unset | datetime.datetime
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

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

        def _parse_urn(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        urn = _parse_urn(d.pop("urn", UNSET))

        def _parse_copyright_(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        copyright_ = _parse_copyright_(d.pop("copyright", UNSET))

        version = d.pop("version", UNSET)

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

        patched_loaded_library_detailed = cls(
            id=id,
            name=name,
            description=description,
            annotation=annotation,
            locales=locales,
            dependencies=dependencies,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            ref_id=ref_id,
            provider=provider,
            locale=locale,
            default_locale=default_locale,
            urn=urn,
            copyright_=copyright_,
            version=version,
            packager=packager,
            publication_date=publication_date,
            builtin=builtin,
            objects_meta=objects_meta,
            folder=folder,
        )

        patched_loaded_library_detailed.additional_properties = d
        return patched_loaded_library_detailed

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
