import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilteringLabelRead")


@_attrs_define
class FilteringLabelRead:
    """
    Attributes:
        id (UUID):
        folder (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        label (str):
        is_published (Union[Unset, bool]):
    """

    id: UUID
    folder: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    label: str
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        folder = self.folder

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        label = self.label

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "folder": folder,
                "created_at": created_at,
                "updated_at": updated_at,
                "label": label,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        folder = d.pop("folder")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        label = d.pop("label")

        is_published = d.pop("is_published", UNSET)

        filtering_label_read = cls(
            id=id,
            folder=folder,
            created_at=created_at,
            updated_at=updated_at,
            label=label,
            is_published=is_published,
        )

        filtering_label_read.additional_properties = d
        return filtering_label_read

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
