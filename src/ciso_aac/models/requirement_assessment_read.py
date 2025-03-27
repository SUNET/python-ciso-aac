import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.result_enum import ResultEnum
from ..models.status_ab_4_enum import StatusAb4Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filtered_node import FilteredNode


T = TypeVar("T", bound="RequirementAssessmentRead")


@_attrs_define
class RequirementAssessmentRead:
    """
    Attributes:
        id (UUID):
        name (str):
        description (str):
        evidences (list[str]):
        compliance_assessment (str):
        folder (str):
        assessable (bool):
        requirement (FilteredNode):
        security_exceptions (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        eta (Union[None, Unset, datetime.date]):
        due_date (Union[None, Unset, datetime.date]):
        status (Union[Unset, StatusAb4Enum]): * `to_do` - To do
            * `in_progress` - In progress
            * `in_review` - In review
            * `done` - Done
        result (Union[Unset, ResultEnum]): * `not_assessed` - Not assessed
            * `partially_compliant` - Partially compliant
            * `non_compliant` - Non-compliant
            * `compliant` - Compliant
            * `not_applicable` - Not applicable
        is_scored (Union[Unset, bool]):
        score (Union[None, Unset, int]):
        documentation_score (Union[None, Unset, int]):
        observation (Union[None, Unset, str]):
        selected (Union[Unset, bool]):
        mapping_inference (Union[Unset, Any]):
        answer (Union[Unset, Any]):
        applied_controls (Union[Unset, list[UUID]]):
    """

    id: UUID
    name: str
    description: str
    evidences: list[str]
    compliance_assessment: str
    folder: str
    assessable: bool
    requirement: "FilteredNode"
    security_exceptions: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Unset | bool = UNSET
    eta: None | Unset | datetime.date = UNSET
    due_date: None | Unset | datetime.date = UNSET
    status: Unset | StatusAb4Enum = UNSET
    result: Unset | ResultEnum = UNSET
    is_scored: Unset | bool = UNSET
    score: None | Unset | int = UNSET
    documentation_score: None | Unset | int = UNSET
    observation: None | Unset | str = UNSET
    selected: Unset | bool = UNSET
    mapping_inference: Unset | Any = UNSET
    answer: Unset | Any = UNSET
    applied_controls: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        evidences = self.evidences

        compliance_assessment = self.compliance_assessment

        folder = self.folder

        assessable = self.assessable

        requirement = self.requirement.to_dict()

        security_exceptions = self.security_exceptions

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        eta: None | Unset | str
        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat()
        else:
            eta = self.eta

        due_date: None | Unset | str
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        result: Unset | str = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        is_scored = self.is_scored

        score: None | Unset | int
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        documentation_score: None | Unset | int
        if isinstance(self.documentation_score, Unset):
            documentation_score = UNSET
        else:
            documentation_score = self.documentation_score

        observation: None | Unset | str
        if isinstance(self.observation, Unset):
            observation = UNSET
        else:
            observation = self.observation

        selected = self.selected

        mapping_inference = self.mapping_inference

        answer = self.answer

        applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "evidences": evidences,
                "compliance_assessment": compliance_assessment,
                "folder": folder,
                "assessable": assessable,
                "requirement": requirement,
                "security_exceptions": security_exceptions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if eta is not UNSET:
            field_dict["eta"] = eta
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if is_scored is not UNSET:
            field_dict["is_scored"] = is_scored
        if score is not UNSET:
            field_dict["score"] = score
        if documentation_score is not UNSET:
            field_dict["documentation_score"] = documentation_score
        if observation is not UNSET:
            field_dict["observation"] = observation
        if selected is not UNSET:
            field_dict["selected"] = selected
        if mapping_inference is not UNSET:
            field_dict["mapping_inference"] = mapping_inference
        if answer is not UNSET:
            field_dict["answer"] = answer
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filtered_node import FilteredNode

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        evidences = cast(list[str], d.pop("evidences"))

        compliance_assessment = d.pop("compliance_assessment")

        folder = d.pop("folder")

        assessable = d.pop("assessable")

        requirement = FilteredNode.from_dict(d.pop("requirement"))

        security_exceptions = cast(list[str], d.pop("security_exceptions"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_published = d.pop("is_published", UNSET)

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

        def _parse_due_date(data: object) -> None | Unset | datetime.date:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data).date()

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.date, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        _status = d.pop("status", UNSET)
        status: Unset | StatusAb4Enum
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusAb4Enum(_status)

        _result = d.pop("result", UNSET)
        result: Unset | ResultEnum
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ResultEnum(_result)

        is_scored = d.pop("is_scored", UNSET)

        def _parse_score(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_documentation_score(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        documentation_score = _parse_documentation_score(d.pop("documentation_score", UNSET))

        def _parse_observation(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        observation = _parse_observation(d.pop("observation", UNSET))

        selected = d.pop("selected", UNSET)

        mapping_inference = d.pop("mapping_inference", UNSET)

        answer = d.pop("answer", UNSET)

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

        requirement_assessment_read = cls(
            id=id,
            name=name,
            description=description,
            evidences=evidences,
            compliance_assessment=compliance_assessment,
            folder=folder,
            assessable=assessable,
            requirement=requirement,
            security_exceptions=security_exceptions,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            eta=eta,
            due_date=due_date,
            status=status,
            result=result,
            is_scored=is_scored,
            score=score,
            documentation_score=documentation_score,
            observation=observation,
            selected=selected,
            mapping_inference=mapping_inference,
            answer=answer,
            applied_controls=applied_controls,
        )

        requirement_assessment_read.additional_properties = d
        return requirement_assessment_read

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
