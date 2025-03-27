import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.category_ae_3_enum import CategoryAe3Enum
from ..models.csf_function_enum import CsfFunctionEnum
from ..models.effort_enum import EffortEnum
from ..models.priority_enum import PriorityEnum
from ..models.status_2e9_enum import Status2E9Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppliedControlWrite")


@_attrs_define
class AppliedControlWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        findings (Union[Unset, list[UUID]]):
        description (Union[None, Unset, str]):
        priority (Union[None, PriorityEnum, Unset]):
        ref_id (Union[None, Unset, str]):
        category (Union[BlankEnum, CategoryAe3Enum, None, Unset]):
        csf_function (Union[BlankEnum, CsfFunctionEnum, None, Unset]):
        status (Union[BlankEnum, Status2E9Enum, Unset]):
        start_date (Union[None, Unset, datetime.date]): Start date (useful for timeline)
        eta (Union[None, Unset, datetime.date]): Estimated Time of Arrival
        expiry_date (Union[None, Unset, datetime.date]): Date after which the applied control is no longer valid
        link (Union[None, Unset, str]): External url for action follow-up (eg. Jira ticket)
        effort (Union[BlankEnum, EffortEnum, None, Unset]): Relative effort of the measure (using T-Shirt sizing)

            * `S` - Small
            * `M` - Medium
            * `L` - Large
            * `XL` - Extra Large
        cost (Union[None, Unset, float]): Cost of the measure (using globally-chosen currency)
        progress_field (Union[Unset, int]):
        is_published (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        reference_control (Union[None, UUID, Unset]):
        evidences (Union[Unset, list[UUID]]):
        owner (Union[Unset, list[UUID]]):
        security_exceptions (Union[Unset, list[UUID]]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    findings: Union[Unset, list[UUID]] = UNSET
    description: Union[None, Unset, str] = UNSET
    priority: Union[None, PriorityEnum, Unset] = UNSET
    ref_id: Union[None, Unset, str] = UNSET
    category: Union[BlankEnum, CategoryAe3Enum, None, Unset] = UNSET
    csf_function: Union[BlankEnum, CsfFunctionEnum, None, Unset] = UNSET
    status: Union[BlankEnum, Status2E9Enum, Unset] = UNSET
    start_date: Union[None, Unset, datetime.date] = UNSET
    eta: Union[None, Unset, datetime.date] = UNSET
    expiry_date: Union[None, Unset, datetime.date] = UNSET
    link: Union[None, Unset, str] = UNSET
    effort: Union[BlankEnum, EffortEnum, None, Unset] = UNSET
    cost: Union[None, Unset, float] = UNSET
    progress_field: Union[Unset, int] = UNSET
    is_published: Union[Unset, bool] = UNSET
    folder: Union[Unset, UUID] = UNSET
    reference_control: Union[None, UUID, Unset] = UNSET
    evidences: Union[Unset, list[UUID]] = UNSET
    owner: Union[Unset, list[UUID]] = UNSET
    security_exceptions: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

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

        priority: Union[None, Unset, int]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, PriorityEnum):
            priority = self.priority.value
        else:
            priority = self.priority

        ref_id: Union[None, Unset, str]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, CategoryAe3Enum):
            category = self.category.value
        elif isinstance(self.category, BlankEnum):
            category = self.category.value
        else:
            category = self.category

        csf_function: Union[None, Unset, str]
        if isinstance(self.csf_function, Unset):
            csf_function = UNSET
        elif isinstance(self.csf_function, CsfFunctionEnum):
            csf_function = self.csf_function.value
        elif isinstance(self.csf_function, BlankEnum):
            csf_function = self.csf_function.value
        else:
            csf_function = self.csf_function

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

        effort: Union[None, Unset, str]
        if isinstance(self.effort, Unset):
            effort = UNSET
        elif isinstance(self.effort, EffortEnum):
            effort = self.effort.value
        elif isinstance(self.effort, BlankEnum):
            effort = self.effort.value
        else:
            effort = self.effort

        cost: Union[None, Unset, float]
        if isinstance(self.cost, Unset):
            cost = UNSET
        else:
            cost = self.cost

        progress_field = self.progress_field

        is_published = self.is_published

        folder: Union[Unset, str] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        reference_control: Union[None, Unset, str]
        if isinstance(self.reference_control, Unset):
            reference_control = UNSET
        elif isinstance(self.reference_control, UUID):
            reference_control = str(self.reference_control)
        else:
            reference_control = self.reference_control

        evidences: Union[Unset, list[str]] = UNSET
        if not isinstance(self.evidences, Unset):
            evidences = []
            for evidences_item_data in self.evidences:
                evidences_item = str(evidences_item_data)
                evidences.append(evidences_item)

        owner: Union[Unset, list[str]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                owner.append(owner_item)

        security_exceptions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.security_exceptions, Unset):
            security_exceptions = []
            for security_exceptions_item_data in self.security_exceptions:
                security_exceptions_item = str(security_exceptions_item_data)
                security_exceptions.append(security_exceptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if findings is not UNSET:
            field_dict["findings"] = findings
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if category is not UNSET:
            field_dict["category"] = category
        if csf_function is not UNSET:
            field_dict["csf_function"] = csf_function
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
        if effort is not UNSET:
            field_dict["effort"] = effort
        if cost is not UNSET:
            field_dict["cost"] = cost
        if progress_field is not UNSET:
            field_dict["progress_field"] = progress_field
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if reference_control is not UNSET:
            field_dict["reference_control"] = reference_control
        if evidences is not UNSET:
            field_dict["evidences"] = evidences
        if owner is not UNSET:
            field_dict["owner"] = owner
        if security_exceptions is not UNSET:
            field_dict["security_exceptions"] = security_exceptions

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        name = (None, str(self.name).encode(), "text/plain")

        findings: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.findings, Unset):
            _temp_findings = []
            for findings_item_data in self.findings:
                findings_item = str(findings_item_data)
                _temp_findings.append(findings_item)
            findings = (None, json.dumps(_temp_findings).encode(), "application/json")

        description: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        priority: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, PriorityEnum):
            priority = (None, str(self.priority.value).encode(), "text/plain")
        elif isinstance(self.priority, None):
            priority = (None, str(self.priority).encode(), "text/plain")
        else:
            priority = (None, str(self.priority).encode(), "text/plain")

        ref_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, str):
            ref_id = (None, str(self.ref_id).encode(), "text/plain")
        else:
            ref_id = (None, str(self.ref_id).encode(), "text/plain")

        category: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, CategoryAe3Enum):
            category = (None, str(self.category.value).encode(), "text/plain")
        elif isinstance(self.category, BlankEnum):
            category = (None, str(self.category.value).encode(), "text/plain")
        elif isinstance(self.category, None):
            category = (None, str(self.category).encode(), "text/plain")
        else:
            category = (None, str(self.category).encode(), "text/plain")

        csf_function: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.csf_function, Unset):
            csf_function = UNSET
        elif isinstance(self.csf_function, CsfFunctionEnum):
            csf_function = (None, str(self.csf_function.value).encode(), "text/plain")
        elif isinstance(self.csf_function, BlankEnum):
            csf_function = (None, str(self.csf_function.value).encode(), "text/plain")
        elif isinstance(self.csf_function, None):
            csf_function = (None, str(self.csf_function).encode(), "text/plain")
        else:
            csf_function = (None, str(self.csf_function).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status2E9Enum):
            status = (None, str(self.status.value).encode(), "text/plain")
        else:
            status = (None, str(self.status.value).encode(), "text/plain")

        start_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat().encode()
        else:
            start_date = (None, str(self.start_date).encode(), "text/plain")

        eta: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat().encode()
        else:
            eta = (None, str(self.eta).encode(), "text/plain")

        expiry_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat().encode()
        else:
            expiry_date = (None, str(self.expiry_date).encode(), "text/plain")

        link: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.link, Unset):
            link = UNSET
        elif isinstance(self.link, str):
            link = (None, str(self.link).encode(), "text/plain")
        else:
            link = (None, str(self.link).encode(), "text/plain")

        effort: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.effort, Unset):
            effort = UNSET
        elif isinstance(self.effort, EffortEnum):
            effort = (None, str(self.effort.value).encode(), "text/plain")
        elif isinstance(self.effort, BlankEnum):
            effort = (None, str(self.effort.value).encode(), "text/plain")
        elif isinstance(self.effort, None):
            effort = (None, str(self.effort).encode(), "text/plain")
        else:
            effort = (None, str(self.effort).encode(), "text/plain")

        cost: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.cost, Unset):
            cost = UNSET
        elif isinstance(self.cost, float):
            cost = (None, str(self.cost).encode(), "text/plain")
        else:
            cost = (None, str(self.cost).encode(), "text/plain")

        progress_field = (
            self.progress_field
            if isinstance(self.progress_field, Unset)
            else (None, str(self.progress_field).encode(), "text/plain")
        )

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        folder: Union[Unset, bytes] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        reference_control: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.reference_control, Unset):
            reference_control = UNSET
        elif isinstance(self.reference_control, UUID):
            reference_control = str(self.reference_control)
        else:
            reference_control = (None, str(self.reference_control).encode(), "text/plain")

        evidences: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.evidences, Unset):
            _temp_evidences = []
            for evidences_item_data in self.evidences:
                evidences_item = str(evidences_item_data)
                _temp_evidences.append(evidences_item)
            evidences = (None, json.dumps(_temp_evidences).encode(), "application/json")

        owner: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.owner, Unset):
            _temp_owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                _temp_owner.append(owner_item)
            owner = (None, json.dumps(_temp_owner).encode(), "application/json")

        security_exceptions: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.security_exceptions, Unset):
            _temp_security_exceptions = []
            for security_exceptions_item_data in self.security_exceptions:
                security_exceptions_item = str(security_exceptions_item_data)
                _temp_security_exceptions.append(security_exceptions_item)
            security_exceptions = (None, json.dumps(_temp_security_exceptions).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if findings is not UNSET:
            field_dict["findings"] = findings
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if category is not UNSET:
            field_dict["category"] = category
        if csf_function is not UNSET:
            field_dict["csf_function"] = csf_function
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
        if effort is not UNSET:
            field_dict["effort"] = effort
        if cost is not UNSET:
            field_dict["cost"] = cost
        if progress_field is not UNSET:
            field_dict["progress_field"] = progress_field
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if reference_control is not UNSET:
            field_dict["reference_control"] = reference_control
        if evidences is not UNSET:
            field_dict["evidences"] = evidences
        if owner is not UNSET:
            field_dict["owner"] = owner
        if security_exceptions is not UNSET:
            field_dict["security_exceptions"] = security_exceptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

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

        def _parse_priority(data: object) -> Union[None, PriorityEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                priority_type_0 = PriorityEnum(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PriorityEnum, Unset], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_ref_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_category(data: object) -> Union[BlankEnum, CategoryAe3Enum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = CategoryAe3Enum(data)

                return category_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_1 = BlankEnum(data)

                return category_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, CategoryAe3Enum, None, Unset], data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_csf_function(data: object) -> Union[BlankEnum, CsfFunctionEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                csf_function_type_0 = CsfFunctionEnum(data)

                return csf_function_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                csf_function_type_1 = BlankEnum(data)

                return csf_function_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, CsfFunctionEnum, None, Unset], data)

        csf_function = _parse_csf_function(d.pop("csf_function", UNSET))

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

        def _parse_effort(data: object) -> Union[BlankEnum, EffortEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effort_type_0 = EffortEnum(data)

                return effort_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effort_type_1 = BlankEnum(data)

                return effort_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, EffortEnum, None, Unset], data)

        effort = _parse_effort(d.pop("effort", UNSET))

        def _parse_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost = _parse_cost(d.pop("cost", UNSET))

        progress_field = d.pop("progress_field", UNSET)

        is_published = d.pop("is_published", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, UUID]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_reference_control(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_control_type_0 = UUID(data)

                return reference_control_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        reference_control = _parse_reference_control(d.pop("reference_control", UNSET))

        evidences = []
        _evidences = d.pop("evidences", UNSET)
        for evidences_item_data in _evidences or []:
            evidences_item = UUID(evidences_item_data)

            evidences.append(evidences_item)

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

        applied_control_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            findings=findings,
            description=description,
            priority=priority,
            ref_id=ref_id,
            category=category,
            csf_function=csf_function,
            status=status,
            start_date=start_date,
            eta=eta,
            expiry_date=expiry_date,
            link=link,
            effort=effort,
            cost=cost,
            progress_field=progress_field,
            is_published=is_published,
            folder=folder,
            reference_control=reference_control,
            evidences=evidences,
            owner=owner,
            security_exceptions=security_exceptions,
        )

        applied_control_write.additional_properties = d
        return applied_control_write

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
