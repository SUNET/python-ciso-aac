import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetRead")


@_attrs_define
class AssetRead:
    """
    Attributes:
        id (UUID):
        folder (str):
        parent_assets (list[str]):
        children_assets (list[str]):
        owner (list[str]):
        security_objectives (Any):
        disaster_recovery_objectives (Any):
        filtering_labels (list[str]):
        type_ (str):
        security_exceptions (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        ebios_rm_studies (Union[Unset, list[Union[None, UUID]]]):
        description (Union[None, Unset, str]):
        business_value (Union[Unset, str]):
        reference_link (Union[None, Unset, str]): External url for action follow-up (eg. Jira ticket)
        ref_id (Union[Unset, str]):
        is_published (Union[Unset, bool]):
    """

    id: UUID
    folder: str
    parent_assets: list[str]
    children_assets: list[str]
    owner: list[str]
    security_objectives: Any
    disaster_recovery_objectives: Any
    filtering_labels: list[str]
    type_: str
    security_exceptions: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    ebios_rm_studies: Unset | list[None | UUID] = UNSET
    description: None | Unset | str = UNSET
    business_value: Unset | str = UNSET
    reference_link: None | Unset | str = UNSET
    ref_id: Unset | str = UNSET
    is_published: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        folder = self.folder

        parent_assets = self.parent_assets

        children_assets = self.children_assets

        owner = self.owner

        security_objectives = self.security_objectives

        disaster_recovery_objectives = self.disaster_recovery_objectives

        filtering_labels = self.filtering_labels

        type_ = self.type_

        security_exceptions = self.security_exceptions

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

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

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        business_value = self.business_value

        reference_link: None | Unset | str
        if isinstance(self.reference_link, Unset):
            reference_link = UNSET
        else:
            reference_link = self.reference_link

        ref_id = self.ref_id

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "folder": folder,
                "parent_assets": parent_assets,
                "children_assets": children_assets,
                "owner": owner,
                "security_objectives": security_objectives,
                "disaster_recovery_objectives": disaster_recovery_objectives,
                "filtering_labels": filtering_labels,
                "type": type_,
                "security_exceptions": security_exceptions,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if ebios_rm_studies is not UNSET:
            field_dict["ebios_rm_studies"] = ebios_rm_studies
        if description is not UNSET:
            field_dict["description"] = description
        if business_value is not UNSET:
            field_dict["business_value"] = business_value
        if reference_link is not UNSET:
            field_dict["reference_link"] = reference_link
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        folder = d.pop("folder")

        parent_assets = cast(list[str], d.pop("parent_assets"))

        children_assets = cast(list[str], d.pop("children_assets"))

        owner = cast(list[str], d.pop("owner"))

        security_objectives = d.pop("security_objectives")

        disaster_recovery_objectives = d.pop("disaster_recovery_objectives")

        filtering_labels = cast(list[str], d.pop("filtering_labels"))

        type_ = d.pop("type")

        security_exceptions = cast(list[str], d.pop("security_exceptions"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

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

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        business_value = d.pop("business_value", UNSET)

        def _parse_reference_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        reference_link = _parse_reference_link(d.pop("reference_link", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        is_published = d.pop("is_published", UNSET)

        asset_read = cls(
            id=id,
            folder=folder,
            parent_assets=parent_assets,
            children_assets=children_assets,
            owner=owner,
            security_objectives=security_objectives,
            disaster_recovery_objectives=disaster_recovery_objectives,
            filtering_labels=filtering_labels,
            type_=type_,
            security_exceptions=security_exceptions,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            ebios_rm_studies=ebios_rm_studies,
            description=description,
            business_value=business_value,
            reference_link=reference_link,
            ref_id=ref_id,
            is_published=is_published,
        )

        asset_read.additional_properties = d
        return asset_read

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
