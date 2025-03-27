import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAssetWrite")


@_attrs_define
class PatchedAssetWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        ebios_rm_studies (Union[Unset, list[Union[None, UUID]]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        business_value (Union[Unset, str]):
        type_ (Union[Unset, TypeEnum]): * `PR` - Primary
            * `SP` - Support
        reference_link (Union[None, Unset, str]): External url for action follow-up (eg. Jira ticket)
        security_objectives (Union[Unset, Any]): The security objectives of the asset
        disaster_recovery_objectives (Union[Unset, Any]): The disaster recovery objectives of the asset
        ref_id (Union[Unset, str]):
        is_published (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        filtering_labels (Union[Unset, list[UUID]]):
        parent_assets (Union[Unset, list[UUID]]):
        owner (Union[Unset, list[UUID]]):
        security_exceptions (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    ebios_rm_studies: Unset | list[None | UUID] = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    business_value: Unset | str = UNSET
    type_: Unset | TypeEnum = UNSET
    reference_link: None | Unset | str = UNSET
    security_objectives: Unset | Any = UNSET
    disaster_recovery_objectives: Unset | Any = UNSET
    ref_id: Unset | str = UNSET
    is_published: Unset | bool = UNSET
    folder: Unset | UUID = UNSET
    filtering_labels: Unset | list[UUID] = UNSET
    parent_assets: Unset | list[UUID] = UNSET
    owner: Unset | list[UUID] = UNSET
    security_exceptions: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        ebios_rm_studies: Unset | list[None | str] = UNSET
        if not isinstance(self.ebios_rm_studies, Unset):
            ebios_rm_studies = []
            for ebios_rm_studies_item_data in self.ebios_rm_studies:
                ebios_rm_studies_item: None | str
                if isinstance(ebios_rm_studies_item_data, UUID):
                    ebios_rm_studies_item = str(ebios_rm_studies_item_data)
                else:
                    ebios_rm_studies_item = ebios_rm_studies_item_data
                ebios_rm_studies.append(ebios_rm_studies_item)

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        business_value = self.business_value

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        reference_link: None | Unset | str
        if isinstance(self.reference_link, Unset):
            reference_link = UNSET
        else:
            reference_link = self.reference_link

        security_objectives = self.security_objectives

        disaster_recovery_objectives = self.disaster_recovery_objectives

        ref_id = self.ref_id

        is_published = self.is_published

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        filtering_labels: Unset | list[str] = UNSET
        if not isinstance(self.filtering_labels, Unset):
            filtering_labels = []
            for filtering_labels_item_data in self.filtering_labels:
                filtering_labels_item = str(filtering_labels_item_data)
                filtering_labels.append(filtering_labels_item)

        parent_assets: Unset | list[str] = UNSET
        if not isinstance(self.parent_assets, Unset):
            parent_assets = []
            for parent_assets_item_data in self.parent_assets:
                parent_assets_item = str(parent_assets_item_data)
                parent_assets.append(parent_assets_item)

        owner: Unset | list[str] = UNSET
        if not isinstance(self.owner, Unset):
            owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                owner.append(owner_item)

        security_exceptions: Unset | list[str] = UNSET
        if not isinstance(self.security_exceptions, Unset):
            security_exceptions = []
            for security_exceptions_item_data in self.security_exceptions:
                security_exceptions_item = str(security_exceptions_item_data)
                security_exceptions.append(security_exceptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ebios_rm_studies is not UNSET:
            field_dict["ebios_rm_studies"] = ebios_rm_studies
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if business_value is not UNSET:
            field_dict["business_value"] = business_value
        if type_ is not UNSET:
            field_dict["type"] = type_
        if reference_link is not UNSET:
            field_dict["reference_link"] = reference_link
        if security_objectives is not UNSET:
            field_dict["security_objectives"] = security_objectives
        if disaster_recovery_objectives is not UNSET:
            field_dict["disaster_recovery_objectives"] = disaster_recovery_objectives
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if filtering_labels is not UNSET:
            field_dict["filtering_labels"] = filtering_labels
        if parent_assets is not UNSET:
            field_dict["parent_assets"] = parent_assets
        if owner is not UNSET:
            field_dict["owner"] = owner
        if security_exceptions is not UNSET:
            field_dict["security_exceptions"] = security_exceptions

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        ebios_rm_studies: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.ebios_rm_studies, Unset):
            _temp_ebios_rm_studies = []
            for ebios_rm_studies_item_data in self.ebios_rm_studies:
                ebios_rm_studies_item: None | str
                if isinstance(ebios_rm_studies_item_data, UUID):
                    ebios_rm_studies_item = str(ebios_rm_studies_item_data)
                else:
                    ebios_rm_studies_item = ebios_rm_studies_item_data
                _temp_ebios_rm_studies.append(ebios_rm_studies_item)
            ebios_rm_studies = (None, json.dumps(_temp_ebios_rm_studies).encode(), "application/json")

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        business_value = (
            self.business_value
            if isinstance(self.business_value, Unset)
            else (None, str(self.business_value).encode(), "text/plain")
        )

        type_: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        reference_link: Unset | tuple[None, bytes, str]

        if isinstance(self.reference_link, Unset):
            reference_link = UNSET
        elif isinstance(self.reference_link, str):
            reference_link = (None, str(self.reference_link).encode(), "text/plain")
        else:
            reference_link = (None, str(self.reference_link).encode(), "text/plain")

        security_objectives = (
            self.security_objectives
            if isinstance(self.security_objectives, Unset)
            else (None, str(self.security_objectives).encode(), "text/plain")
        )

        disaster_recovery_objectives = (
            self.disaster_recovery_objectives
            if isinstance(self.disaster_recovery_objectives, Unset)
            else (None, str(self.disaster_recovery_objectives).encode(), "text/plain")
        )

        ref_id = self.ref_id if isinstance(self.ref_id, Unset) else (None, str(self.ref_id).encode(), "text/plain")

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        filtering_labels: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.filtering_labels, Unset):
            _temp_filtering_labels = []
            for filtering_labels_item_data in self.filtering_labels:
                filtering_labels_item = str(filtering_labels_item_data)
                _temp_filtering_labels.append(filtering_labels_item)
            filtering_labels = (None, json.dumps(_temp_filtering_labels).encode(), "application/json")

        parent_assets: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.parent_assets, Unset):
            _temp_parent_assets = []
            for parent_assets_item_data in self.parent_assets:
                parent_assets_item = str(parent_assets_item_data)
                _temp_parent_assets.append(parent_assets_item)
            parent_assets = (None, json.dumps(_temp_parent_assets).encode(), "application/json")

        owner: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.owner, Unset):
            _temp_owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                _temp_owner.append(owner_item)
            owner = (None, json.dumps(_temp_owner).encode(), "application/json")

        security_exceptions: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.security_exceptions, Unset):
            _temp_security_exceptions = []
            for security_exceptions_item_data in self.security_exceptions:
                security_exceptions_item = str(security_exceptions_item_data)
                _temp_security_exceptions.append(security_exceptions_item)
            security_exceptions = (None, json.dumps(_temp_security_exceptions).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ebios_rm_studies is not UNSET:
            field_dict["ebios_rm_studies"] = ebios_rm_studies
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if business_value is not UNSET:
            field_dict["business_value"] = business_value
        if type_ is not UNSET:
            field_dict["type"] = type_
        if reference_link is not UNSET:
            field_dict["reference_link"] = reference_link
        if security_objectives is not UNSET:
            field_dict["security_objectives"] = security_objectives
        if disaster_recovery_objectives is not UNSET:
            field_dict["disaster_recovery_objectives"] = disaster_recovery_objectives
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if filtering_labels is not UNSET:
            field_dict["filtering_labels"] = filtering_labels
        if parent_assets is not UNSET:
            field_dict["parent_assets"] = parent_assets
        if owner is not UNSET:
            field_dict["owner"] = owner
        if security_exceptions is not UNSET:
            field_dict["security_exceptions"] = security_exceptions

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

        ebios_rm_studies = []
        _ebios_rm_studies = d.pop("ebios_rm_studies", UNSET)
        for ebios_rm_studies_item_data in _ebios_rm_studies or []:

            def _parse_ebios_rm_studies_item(data: object) -> None | UUID:
                if data is None:
                    return data
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    ebios_rm_studies_item_type_0 = UUID(data)

                    return ebios_rm_studies_item_type_0
                except:  # noqa: E722
                    pass
                return cast(None | UUID, data)

            ebios_rm_studies_item = _parse_ebios_rm_studies_item(ebios_rm_studies_item_data)

            ebios_rm_studies.append(ebios_rm_studies_item)

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

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        business_value = d.pop("business_value", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | TypeEnum
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TypeEnum(_type_)

        def _parse_reference_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        reference_link = _parse_reference_link(d.pop("reference_link", UNSET))

        security_objectives = d.pop("security_objectives", UNSET)

        disaster_recovery_objectives = d.pop("disaster_recovery_objectives", UNSET)

        ref_id = d.pop("ref_id", UNSET)

        is_published = d.pop("is_published", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        filtering_labels = []
        _filtering_labels = d.pop("filtering_labels", UNSET)
        for filtering_labels_item_data in _filtering_labels or []:
            filtering_labels_item = UUID(filtering_labels_item_data)

            filtering_labels.append(filtering_labels_item)

        parent_assets = []
        _parent_assets = d.pop("parent_assets", UNSET)
        for parent_assets_item_data in _parent_assets or []:
            parent_assets_item = UUID(parent_assets_item_data)

            parent_assets.append(parent_assets_item)

        owner = []
        _owner = d.pop("owner", UNSET)
        for owner_item_data in _owner or []:
            owner_item = UUID(owner_item_data)

            owner.append(owner_item)

        security_exceptions = []
        _security_exceptions = d.pop("security_exceptions", UNSET)
        for security_exceptions_item_data in _security_exceptions or []:
            security_exceptions_item = UUID(security_exceptions_item_data)

            security_exceptions.append(security_exceptions_item)

        patched_asset_write = cls(
            id=id,
            ebios_rm_studies=ebios_rm_studies,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            business_value=business_value,
            type_=type_,
            reference_link=reference_link,
            security_objectives=security_objectives,
            disaster_recovery_objectives=disaster_recovery_objectives,
            ref_id=ref_id,
            is_published=is_published,
            folder=folder,
            filtering_labels=filtering_labels,
            parent_assets=parent_assets,
            owner=owner,
            security_exceptions=security_exceptions,
        )

        patched_asset_write.additional_properties = d
        return patched_asset_write

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
