import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.status_2e9_enum import Status2E9Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppliedControlRead")


@_attrs_define
class AppliedControlRead:
    """
    Attributes:
        id (UUID):
        folder (str):
        reference_control (str):
        priority (str):
        category (str):
        csf_function (str):
        evidences (list[str]):
        effort (str):
        cost (float):
        ranking_score (int):
        owner (list[str]):
        security_exceptions (list[str]):
        state (str):
        findings_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        findings (Union[Unset, list[UUID]]):
        description (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        status (Union[BlankEnum, Status2E9Enum, Unset]):
        start_date (Union[None, Unset, datetime.date]): Start date (useful for timeline)
        eta (Union[None, Unset, datetime.date]): Estimated Time of Arrival
        expiry_date (Union[None, Unset, datetime.date]): Date after which the applied control is no longer valid
        link (Union[None, Unset, str]): External url for action follow-up (eg. Jira ticket)
        progress_field (Union[Unset, int]):
        is_published (Union[Unset, bool]):
    """

    id: UUID
    folder: str
    reference_control: str
    priority: str
    category: str
    csf_function: str
    evidences: list[str]
    effort: str
    cost: float
    ranking_score: int
    owner: list[str]
    security_exceptions: list[str]
    state: str
    findings_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    findings: Union[Unset, list[UUID]] = UNSET
    description: Union[None, Unset, str] = UNSET
    ref_id: Union[None, Unset, str] = UNSET
    status: Union[BlankEnum, Status2E9Enum, Unset] = UNSET
    start_date: Union[None, Unset, datetime.date] = UNSET
    eta: Union[None, Unset, datetime.date] = UNSET
    expiry_date: Union[None, Unset, datetime.date] = UNSET
    link: Union[None, Unset, str] = UNSET
    progress_field: Union[Unset, int] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        folder = self.folder

        reference_control = self.reference_control

        priority = self.priority

        category = self.category

        csf_function = self.csf_function

        evidences = self.evidences

        effort = self.effort

        cost = self.cost

        ranking_score = self.ranking_score

        owner = self.owner

        security_exceptions = self.security_exceptions

        state = self.state

        findings_count = self.findings_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        findings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.findings, Unset):
            findings = []
            for findings_item_data in self.findings:
                findings_item = str(findings_item_data)
                findings.append(findings_item)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id: Union[None, Unset, str]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        status: Union[Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status2E9Enum):
            status = self.status.value
        else:
            status = self.status.value

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        eta: Union[None, Unset, str]
        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat()
        else:
            eta = self.eta

        expiry_date: Union[None, Unset, str]
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        progress_field = self.progress_field

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "folder": folder,
                "reference_control": reference_control,
                "priority": priority,
                "category": category,
                "csf_function": csf_function,
                "evidences": evidences,
                "effort": effort,
                "cost": cost,
                "ranking_score": ranking_score,
                "owner": owner,
                "security_exceptions": security_exceptions,
                "state": state,
                "findings_count": findings_count,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if findings is not UNSET:
            field_dict["findings"] = findings
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if eta is not UNSET:
            field_dict["eta"] = eta
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if link is not UNSET:
            field_dict["link"] = link
        if progress_field is not UNSET:
            field_dict["progress_field"] = progress_field
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        folder = d.pop("folder")

        reference_control = d.pop("reference_control")

        priority = d.pop("priority")

        category = d.pop("category")

        csf_function = d.pop("csf_function")

        evidences = cast(list[str], d.pop("evidences"))

        effort = d.pop("effort")

        cost = d.pop("cost")

        ranking_score = d.pop("ranking_score")

        owner = cast(list[str], d.pop("owner"))

        security_exceptions = cast(list[str], d.pop("security_exceptions"))

        state = d.pop("state")

        findings_count = d.pop("findings_count")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        findings = []
        _findings = d.pop("findings", UNSET)
        for findings_item_data in _findings or []:
            findings_item = UUID(findings_item_data)

            findings.append(findings_item)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_ref_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_status(data: object) -> Union[BlankEnum, Status2E9Enum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = Status2E9Enum(data)

                return status_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            status_type_1 = BlankEnum(data)

            return status_type_1

        status = _parse_status(d.pop("status", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_eta(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                eta_type_0 = isoparse(data).date()

                return eta_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        eta = _parse_eta(d.pop("eta", UNSET))

        def _parse_expiry_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = isoparse(data).date()

                return expiry_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        def _parse_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link = _parse_link(d.pop("link", UNSET))

        progress_field = d.pop("progress_field", UNSET)

        is_published = d.pop("is_published", UNSET)

        applied_control_read = cls(
            id=id,
            folder=folder,
            reference_control=reference_control,
            priority=priority,
            category=category,
            csf_function=csf_function,
            evidences=evidences,
            effort=effort,
            cost=cost,
            ranking_score=ranking_score,
            owner=owner,
            security_exceptions=security_exceptions,
            state=state,
            findings_count=findings_count,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            findings=findings,
            description=description,
            ref_id=ref_id,
            status=status,
            start_date=start_date,
            eta=eta,
            expiry_date=expiry_date,
            link=link,
            progress_field=progress_field,
            is_published=is_published,
        )

        applied_control_read.additional_properties = d
        return applied_control_read

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
