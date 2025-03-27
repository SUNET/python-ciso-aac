import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FearedEventWrite")


@_attrs_define
class FearedEventWrite:
    """
    Attributes:
        id (UUID):
        name (str):
        ebios_rm_study (UUID):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        ref_id (Union[Unset, str]):
        gravity (Union[Unset, int]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
        assets (Union[Unset, list[UUID]]): Assets that are affected by the feared event
        qualifications (Union[Unset, list[UUID]]): Qualifications carried by the feared event
    """

    id: UUID
    name: str
    ebios_rm_study: UUID
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    ref_id: Union[Unset, str] = UNSET
    gravity: Union[Unset, int] = UNSET
    is_selected: Union[Unset, bool] = UNSET
    justification: Union[Unset, str] = UNSET
    assets: Union[Unset, list[UUID]] = UNSET
    qualifications: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        ebios_rm_study = str(self.ebios_rm_study)

        is_published = self.is_published

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id = self.ref_id

        gravity = self.gravity

        is_selected = self.is_selected

        justification = self.justification

        assets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                assets.append(assets_item)

        qualifications: Union[Unset, list[str]] = UNSET
        if not isinstance(self.qualifications, Unset):
            qualifications = []
            for qualifications_item_data in self.qualifications:
                qualifications_item = str(qualifications_item_data)
                qualifications.append(qualifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ebios_rm_study": ebios_rm_study,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if gravity is not UNSET:
            field_dict["gravity"] = gravity
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if assets is not UNSET:
            field_dict["assets"] = assets
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        name = (None, str(self.name).encode(), "text/plain")

        ebios_rm_study = str(self.ebios_rm_study)

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        description: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        ref_id = self.ref_id if isinstance(self.ref_id, Unset) else (None, str(self.ref_id).encode(), "text/plain")

        gravity = self.gravity if isinstance(self.gravity, Unset) else (None, str(self.gravity).encode(), "text/plain")

        is_selected = (
            self.is_selected
            if isinstance(self.is_selected, Unset)
            else (None, str(self.is_selected).encode(), "text/plain")
        )

        justification = (
            self.justification
            if isinstance(self.justification, Unset)
            else (None, str(self.justification).encode(), "text/plain")
        )

        assets: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.assets, Unset):
            _temp_assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                _temp_assets.append(assets_item)
            assets = (None, json.dumps(_temp_assets).encode(), "application/json")

        qualifications: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.qualifications, Unset):
            _temp_qualifications = []
            for qualifications_item_data in self.qualifications:
                qualifications_item = str(qualifications_item_data)
                _temp_qualifications.append(qualifications_item)
            qualifications = (None, json.dumps(_temp_qualifications).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "name": name,
                "ebios_rm_study": ebios_rm_study,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if gravity is not UNSET:
            field_dict["gravity"] = gravity
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if assets is not UNSET:
            field_dict["assets"] = assets
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        ebios_rm_study = UUID(d.pop("ebios_rm_study"))

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        gravity = d.pop("gravity", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        assets = []
        _assets = d.pop("assets", UNSET)
        for assets_item_data in _assets or []:
            assets_item = UUID(assets_item_data)

            assets.append(assets_item)

        qualifications = []
        _qualifications = d.pop("qualifications", UNSET)
        for qualifications_item_data in _qualifications or []:
            qualifications_item = UUID(qualifications_item_data)

            qualifications.append(qualifications_item)

        feared_event_write = cls(
            id=id,
            name=name,
            ebios_rm_study=ebios_rm_study,
            is_published=is_published,
            description=description,
            ref_id=ref_id,
            gravity=gravity,
            is_selected=is_selected,
            justification=justification,
            assets=assets,
            qualifications=qualifications,
        )

        feared_event_write.additional_properties = d
        return feared_event_write

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
