import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_40b_enum import Status40BEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedFindingWrite")


@_attrs_define
class PatchedFindingWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
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
        folder (Union[Unset, UUID]):
        findings_assessment (Union[Unset, UUID]):
        filtering_labels (Union[Unset, list[UUID]]):
        vulnerabilities (Union[Unset, list[UUID]]):
        reference_controls (Union[Unset, list[UUID]]):
        applied_controls (Union[Unset, list[UUID]]):
        owner (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    ref_id: Unset | str = UNSET
    severity: Unset | int = UNSET
    status: Unset | Status40BEnum = UNSET
    folder: Unset | UUID = UNSET
    findings_assessment: Unset | UUID = UNSET
    filtering_labels: Unset | list[UUID] = UNSET
    vulnerabilities: Unset | list[UUID] = UNSET
    reference_controls: Unset | list[UUID] = UNSET
    applied_controls: Unset | list[UUID] = UNSET
    owner: Unset | list[UUID] = UNSET
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

        severity = self.severity

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        findings_assessment: Unset | str = UNSET
        if not isinstance(self.findings_assessment, Unset):
            findings_assessment = str(self.findings_assessment)

        filtering_labels: Unset | list[str] = UNSET
        if not isinstance(self.filtering_labels, Unset):
            filtering_labels = []
            for filtering_labels_item_data in self.filtering_labels:
                filtering_labels_item = str(filtering_labels_item_data)
                filtering_labels.append(filtering_labels_item)

        vulnerabilities: Unset | list[str] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = str(vulnerabilities_item_data)
                vulnerabilities.append(vulnerabilities_item)

        reference_controls: Unset | list[str] = UNSET
        if not isinstance(self.reference_controls, Unset):
            reference_controls = []
            for reference_controls_item_data in self.reference_controls:
                reference_controls_item = str(reference_controls_item_data)
                reference_controls.append(reference_controls_item)

        applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

        owner: Unset | list[str] = UNSET
        if not isinstance(self.owner, Unset):
            owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                owner.append(owner_item)

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
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if folder is not UNSET:
            field_dict["folder"] = folder
        if findings_assessment is not UNSET:
            field_dict["findings_assessment"] = findings_assessment
        if filtering_labels is not UNSET:
            field_dict["filtering_labels"] = filtering_labels
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if reference_controls is not UNSET:
            field_dict["reference_controls"] = reference_controls
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if owner is not UNSET:
            field_dict["owner"] = owner

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

        severity = (
            self.severity if isinstance(self.severity, Unset) else (None, str(self.severity).encode(), "text/plain")
        )

        status: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        findings_assessment: Unset | bytes = UNSET
        if not isinstance(self.findings_assessment, Unset):
            findings_assessment = str(self.findings_assessment)

        filtering_labels: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.filtering_labels, Unset):
            _temp_filtering_labels = []
            for filtering_labels_item_data in self.filtering_labels:
                filtering_labels_item = str(filtering_labels_item_data)
                _temp_filtering_labels.append(filtering_labels_item)
            filtering_labels = (None, json.dumps(_temp_filtering_labels).encode(), "application/json")

        vulnerabilities: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            _temp_vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = str(vulnerabilities_item_data)
                _temp_vulnerabilities.append(vulnerabilities_item)
            vulnerabilities = (None, json.dumps(_temp_vulnerabilities).encode(), "application/json")

        reference_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.reference_controls, Unset):
            _temp_reference_controls = []
            for reference_controls_item_data in self.reference_controls:
                reference_controls_item = str(reference_controls_item_data)
                _temp_reference_controls.append(reference_controls_item)
            reference_controls = (None, json.dumps(_temp_reference_controls).encode(), "application/json")

        applied_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            _temp_applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                _temp_applied_controls.append(applied_controls_item)
            applied_controls = (None, json.dumps(_temp_applied_controls).encode(), "application/json")

        owner: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.owner, Unset):
            _temp_owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                _temp_owner.append(owner_item)
            owner = (None, json.dumps(_temp_owner).encode(), "application/json")

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
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if folder is not UNSET:
            field_dict["folder"] = folder
        if findings_assessment is not UNSET:
            field_dict["findings_assessment"] = findings_assessment
        if filtering_labels is not UNSET:
            field_dict["filtering_labels"] = filtering_labels
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if reference_controls is not UNSET:
            field_dict["reference_controls"] = reference_controls
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if owner is not UNSET:
            field_dict["owner"] = owner

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

        severity = d.pop("severity", UNSET)

        _status = d.pop("status", UNSET)
        status: Unset | Status40BEnum
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status40BEnum(_status)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        _findings_assessment = d.pop("findings_assessment", UNSET)
        findings_assessment: Unset | UUID
        if isinstance(_findings_assessment, Unset):
            findings_assessment = UNSET
        else:
            findings_assessment = UUID(_findings_assessment)

        filtering_labels = []
        _filtering_labels = d.pop("filtering_labels", UNSET)
        for filtering_labels_item_data in _filtering_labels or []:
            filtering_labels_item = UUID(filtering_labels_item_data)

            filtering_labels.append(filtering_labels_item)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = UUID(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        reference_controls = []
        _reference_controls = d.pop("reference_controls", UNSET)
        for reference_controls_item_data in _reference_controls or []:
            reference_controls_item = UUID(reference_controls_item_data)

            reference_controls.append(reference_controls_item)

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

        owner = []
        _owner = d.pop("owner", UNSET)
        for owner_item_data in _owner or []:
            owner_item = UUID(owner_item_data)

            owner.append(owner_item)

        patched_finding_write = cls(
            id=id,
            is_published=is_published,
            name=name,
            description=description,
            ref_id=ref_id,
            severity=severity,
            status=status,
            folder=folder,
            findings_assessment=findings_assessment,
            filtering_labels=filtering_labels,
            vulnerabilities=vulnerabilities,
            reference_controls=reference_controls,
            applied_controls=applied_controls,
            owner=owner,
        )

        patched_finding_write.additional_properties = d
        return patched_finding_write

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
