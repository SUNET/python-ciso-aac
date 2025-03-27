import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedFearedEventWrite")


@_attrs_define
class PatchedFearedEventWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        ref_id (Union[Unset, str]):
        gravity (Union[Unset, int]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
        ebios_rm_study (Union[Unset, UUID]):
        assets (Union[Unset, list[UUID]]): Assets that are affected by the feared event
        qualifications (Union[Unset, list[UUID]]): Qualifications carried by the feared event
    """

    id: Unset | UUID = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    ref_id: Unset | str = UNSET
    gravity: Unset | int = UNSET
    is_selected: Unset | bool = UNSET
    justification: Unset | str = UNSET
    ebios_rm_study: Unset | UUID = UNSET
    assets: Unset | list[UUID] = UNSET
    qualifications: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = self.is_published

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id = self.ref_id

        gravity = self.gravity

        is_selected = self.is_selected

        justification = self.justification

        ebios_rm_study: Unset | str = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        assets: Unset | list[str] = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                assets.append(assets_item)

        qualifications: Unset | list[str] = UNSET
        if not isinstance(self.qualifications, Unset):
            qualifications = []
            for qualifications_item_data in self.qualifications:
                qualifications_item = str(qualifications_item_data)
                qualifications.append(qualifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
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
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if assets is not UNSET:
            field_dict["assets"] = assets
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

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

        ebios_rm_study: Unset | bytes = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        assets: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.assets, Unset):
            _temp_assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                _temp_assets.append(assets_item)
            assets = (None, json.dumps(_temp_assets).encode(), "application/json")

        qualifications: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.qualifications, Unset):
            _temp_qualifications = []
            for qualifications_item_data in self.qualifications:
                qualifications_item = str(qualifications_item_data)
                _temp_qualifications.append(qualifications_item)
            qualifications = (None, json.dumps(_temp_qualifications).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
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
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if assets is not UNSET:
            field_dict["assets"] = assets
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications

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

        is_published = d.pop("is_published", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        gravity = d.pop("gravity", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        _ebios_rm_study = d.pop("ebios_rm_study", UNSET)
        ebios_rm_study: Unset | UUID
        if isinstance(_ebios_rm_study, Unset):
            ebios_rm_study = UNSET
        else:
            ebios_rm_study = UUID(_ebios_rm_study)

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

        patched_feared_event_write = cls(
            id=id,
            is_published=is_published,
            name=name,
            description=description,
            ref_id=ref_id,
            gravity=gravity,
            is_selected=is_selected,
            justification=justification,
            ebios_rm_study=ebios_rm_study,
            assets=assets,
            qualifications=qualifications,
        )

        patched_feared_event_write.additional_properties = d
        return patched_feared_event_write

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
