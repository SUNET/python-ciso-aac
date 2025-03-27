import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_40b_enum import Status40BEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindingRead")


@_attrs_define
class FindingRead:
    """
    Attributes:
        id (UUID):
        owner (list[str]):
        findings_assessment (str):
        vulnerabilities (list[str]):
        reference_controls (list[str]):
        applied_controls (list[str]):
        filtering_labels (list[str]):
        folder (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        ref_id (Union[Unset, str]):
        severity (Union[Unset, int]): The severity of the finding
        status (Union[Unset, Status40BEnum]): * `--` - Undefined
            * `identified` - Identified
            * `confirmed` - Confirmed
            * `dismissed` - Dismissed
            * `assigned` - Assigned
            * `in_progress` - In Progress
            * `mitigated` - Mitigated
            * `resolved` - Resolved
            * `deprecated` - Deprecated
    """

    id: UUID
    owner: list[str]
    findings_assessment: str
    vulnerabilities: list[str]
    reference_controls: list[str]
    applied_controls: list[str]
    filtering_labels: list[str]
    folder: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Unset | bool = UNSET
    description: None | Unset | str = UNSET
    ref_id: Unset | str = UNSET
    severity: Unset | int = UNSET
    status: Unset | Status40BEnum = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        owner = self.owner

        findings_assessment = self.findings_assessment

        vulnerabilities = self.vulnerabilities

        reference_controls = self.reference_controls

        applied_controls = self.applied_controls

        filtering_labels = self.filtering_labels

        folder = self.folder

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        is_published = self.is_published

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id = self.ref_id

        severity = self.severity

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "owner": owner,
                "findings_assessment": findings_assessment,
                "vulnerabilities": vulnerabilities,
                "reference_controls": reference_controls,
                "applied_controls": applied_controls,
                "filtering_labels": filtering_labels,
                "folder": folder,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        owner = cast(list[str], d.pop("owner"))

        findings_assessment = d.pop("findings_assessment")

        vulnerabilities = cast(list[str], d.pop("vulnerabilities"))

        reference_controls = cast(list[str], d.pop("reference_controls"))

        applied_controls = cast(list[str], d.pop("applied_controls"))

        filtering_labels = cast(list[str], d.pop("filtering_labels"))

        folder = d.pop("folder")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        severity = d.pop("severity", UNSET)

        _status = d.pop("status", UNSET)
        status: Unset | Status40BEnum
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status40BEnum(_status)

        finding_read = cls(
            id=id,
            owner=owner,
            findings_assessment=findings_assessment,
            vulnerabilities=vulnerabilities,
            reference_controls=reference_controls,
            applied_controls=applied_controls,
            filtering_labels=filtering_labels,
            folder=folder,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            ref_id=ref_id,
            severity=severity,
            status=status,
        )

        finding_read.additional_properties = d
        return finding_read

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
