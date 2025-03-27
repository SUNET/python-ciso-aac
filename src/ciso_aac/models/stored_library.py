import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoredLibrary")


@_attrs_define
class StoredLibrary:
    """
    Attributes:
        id (UUID):
        name (str):
        description (Union[None, str]):
        urn (Union[None, str]):
        version (int):
        locales (list[Any]):
        ref_id (Union[None, Unset, str]):
        locale (Union[Unset, str]):  Default: 'en'.
        packager (Union[None, Unset, str]): Packager of the library
        provider (Union[None, Unset, str]):
        publication_date (Union[None, Unset, datetime.date]):
        builtin (Union[Unset, bool]):
        objects_meta (Union[Unset, Any]):
        is_loaded (Union[Unset, bool]):
        copyright_ (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    description: Union[None, str]
    urn: Union[None, str]
    version: int
    locales: list[Any]
    ref_id: Union[None, Unset, str] = UNSET
    locale: Union[Unset, str] = "en"
    packager: Union[None, Unset, str] = UNSET
    provider: Union[None, Unset, str] = UNSET
    publication_date: Union[None, Unset, datetime.date] = UNSET
    builtin: Union[Unset, bool] = UNSET
    objects_meta: Union[Unset, Any] = UNSET
    is_loaded: Union[Unset, bool] = UNSET
    copyright_: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: Union[None, str]
        description = self.description

        urn: Union[None, str]
        urn = self.urn

        version = self.version

        locales = self.locales

        ref_id: Union[None, Unset, str]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        locale = self.locale

        packager: Union[None, Unset, str]
        if isinstance(self.packager, Unset):
            packager = UNSET
        else:
            packager = self.packager

        provider: Union[None, Unset, str]
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        publication_date: Union[None, Unset, str]
        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        elif isinstance(self.publication_date, datetime.date):
            publication_date = self.publication_date.isoformat()
        else:
            publication_date = self.publication_date

        builtin = self.builtin

        objects_meta = self.objects_meta

        is_loaded = self.is_loaded

        copyright_: Union[None, Unset, str]
        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        else:
            copyright_ = self.copyright_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "urn": urn,
                "version": version,
                "locales": locales,
            }
        )
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if packager is not UNSET:
            field_dict["packager"] = packager
        if provider is not UNSET:
            field_dict["provider"] = provider
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if builtin is not UNSET:
            field_dict["builtin"] = builtin
        if objects_meta is not UNSET:
            field_dict["objects_meta"] = objects_meta
        if is_loaded is not UNSET:
            field_dict["is_loaded"] = is_loaded
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_

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

        def _parse_urn(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        urn = _parse_urn(d.pop("urn"))

        version = d.pop("version")

        locales = cast(list[Any], d.pop("locales"))

        def _parse_ref_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        locale = d.pop("locale", UNSET)

        def _parse_packager(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        packager = _parse_packager(d.pop("packager", UNSET))

        def _parse_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_publication_date(data: object) -> Union[None, Unset, datetime.date]:
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
            return cast(Union[None, Unset, datetime.date], data)

        publication_date = _parse_publication_date(d.pop("publication_date", UNSET))

        builtin = d.pop("builtin", UNSET)

        objects_meta = d.pop("objects_meta", UNSET)

        is_loaded = d.pop("is_loaded", UNSET)

        def _parse_copyright_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        copyright_ = _parse_copyright_(d.pop("copyright", UNSET))

        stored_library = cls(
            id=id,
            name=name,
            description=description,
            urn=urn,
            version=version,
            locales=locales,
            ref_id=ref_id,
            locale=locale,
            packager=packager,
            provider=provider,
            publication_date=publication_date,
            builtin=builtin,
            objects_meta=objects_meta,
            is_loaded=is_loaded,
            copyright_=copyright_,
        )

        stored_library.additional_properties = d
        return stored_library

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
