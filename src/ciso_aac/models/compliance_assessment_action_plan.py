import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.status_2e9_enum import Status2E9Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceAssessmentActionPlan")


@_attrs_define
class ComplianceAssessmentActionPlan:
    """
    Attributes:
        id (UUID):
        name (str):
        folder (str):
        priority (str):
        category (str):
        csf_function (str):
        effort (str):
        cost (float):
        ranking_score (int):
        requirement_assessments (str):
        reference_control (str):
        evidences (list[str]):
        owner (list[str]):
        ref_id (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        status (Union[BlankEnum, Status2E9Enum, Unset]):
        eta (Union[None, Unset, datetime.date]): Estimated Time of Arrival
        expiry_date (Union[None, Unset, datetime.date]): Date after which the applied control is no longer valid
    """

    id: UUID
    name: str
    folder: str
    priority: str
    category: str
    csf_function: str
    effort: str
    cost: float
    ranking_score: int
    requirement_assessments: str
    reference_control: str
    evidences: list[str]
    owner: list[str]
    ref_id: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    status: BlankEnum | Status2E9Enum | Unset = UNSET
    eta: None | Unset | datetime.date = UNSET
    expiry_date: None | Unset | datetime.date = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        folder = self.folder

        priority = self.priority

        category = self.category

        csf_function = self.csf_function

        effort = self.effort

        cost = self.cost

        ranking_score = self.ranking_score

        requirement_assessments = self.requirement_assessments

        reference_control = self.reference_control

        evidences = self.evidences

        owner = self.owner

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: Unset | str
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status2E9Enum):
            status = self.status.value
        else:
            status = self.status.value

        eta: None | Unset | str
        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat()
        else:
            eta = self.eta

        expiry_date: None | Unset | str
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "folder": folder,
                "priority": priority,
                "category": category,
                "csf_function": csf_function,
                "effort": effort,
                "cost": cost,
                "ranking_score": ranking_score,
                "requirement_assessments": requirement_assessments,
                "reference_control": reference_control,
                "evidences": evidences,
                "owner": owner,
            }
        )
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if eta is not UNSET:
            field_dict["eta"] = eta
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        folder = d.pop("folder")

        priority = d.pop("priority")

        category = d.pop("category")

        csf_function = d.pop("csf_function")

        effort = d.pop("effort")

        cost = d.pop("cost")

        ranking_score = d.pop("ranking_score")

        requirement_assessments = d.pop("requirement_assessments")

        reference_control = d.pop("reference_control")

        evidences = cast(list[str], d.pop("evidences"))

        owner = cast(list[str], d.pop("owner"))

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> BlankEnum | Status2E9Enum | Unset:
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

        def _parse_eta(data: object) -> None | Unset | datetime.date:
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
            return cast(None | Unset | datetime.date, data)

        eta = _parse_eta(d.pop("eta", UNSET))

        def _parse_expiry_date(data: object) -> None | Unset | datetime.date:
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
            return cast(None | Unset | datetime.date, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        compliance_assessment_action_plan = cls(
            id=id,
            name=name,
            folder=folder,
            priority=priority,
            category=category,
            csf_function=csf_function,
            effort=effort,
            cost=cost,
            ranking_score=ranking_score,
            requirement_assessments=requirement_assessments,
            reference_control=reference_control,
            evidences=evidences,
            owner=owner,
            ref_id=ref_id,
            description=description,
            status=status,
            eta=eta,
            expiry_date=expiry_date,
        )

        compliance_assessment_action_plan.additional_properties = d
        return compliance_assessment_action_plan

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
