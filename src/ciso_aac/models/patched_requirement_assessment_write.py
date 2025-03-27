import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..models.result_enum import ResultEnum
from ..models.status_ab_4_enum import StatusAb4Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRequirementAssessmentWrite")


@_attrs_define
class PatchedRequirementAssessmentWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
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
        folder (Union[Unset, UUID]):
        compliance_assessment (Union[Unset, UUID]):
        requirement (Union[Unset, UUID]):
        evidences (Union[Unset, list[UUID]]):
        applied_controls (Union[Unset, list[UUID]]):
        security_exceptions (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
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
    folder: Unset | UUID = UNSET
    compliance_assessment: Unset | UUID = UNSET
    requirement: Unset | UUID = UNSET
    evidences: Unset | list[UUID] = UNSET
    applied_controls: Unset | list[UUID] = UNSET
    security_exceptions: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
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

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        compliance_assessment: Unset | str = UNSET
        if not isinstance(self.compliance_assessment, Unset):
            compliance_assessment = str(self.compliance_assessment)

        requirement: Unset | str = UNSET
        if not isinstance(self.requirement, Unset):
            requirement = str(self.requirement)

        evidences: Unset | list[str] = UNSET
        if not isinstance(self.evidences, Unset):
            evidences = []
            for evidences_item_data in self.evidences:
                evidences_item = str(evidences_item_data)
                evidences.append(evidences_item)

        applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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
        if folder is not UNSET:
            field_dict["folder"] = folder
        if compliance_assessment is not UNSET:
            field_dict["compliance_assessment"] = compliance_assessment
        if requirement is not UNSET:
            field_dict["requirement"] = requirement
        if evidences is not UNSET:
            field_dict["evidences"] = evidences
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if security_exceptions is not UNSET:
            field_dict["security_exceptions"] = security_exceptions

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        eta: Unset | tuple[None, bytes, str]

        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat().encode()
        else:
            eta = (None, str(self.eta).encode(), "text/plain")

        due_date: Unset | tuple[None, bytes, str]

        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat().encode()
        else:
            due_date = (None, str(self.due_date).encode(), "text/plain")

        status: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        result: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.result, Unset):
            result = (None, str(self.result.value).encode(), "text/plain")

        is_scored = (
            self.is_scored if isinstance(self.is_scored, Unset) else (None, str(self.is_scored).encode(), "text/plain")
        )

        score: Unset | tuple[None, bytes, str]

        if isinstance(self.score, Unset):
            score = UNSET
        elif isinstance(self.score, int):
            score = (None, str(self.score).encode(), "text/plain")
        else:
            score = (None, str(self.score).encode(), "text/plain")

        documentation_score: Unset | tuple[None, bytes, str]

        if isinstance(self.documentation_score, Unset):
            documentation_score = UNSET
        elif isinstance(self.documentation_score, int):
            documentation_score = (None, str(self.documentation_score).encode(), "text/plain")
        else:
            documentation_score = (None, str(self.documentation_score).encode(), "text/plain")

        observation: Unset | tuple[None, bytes, str]

        if isinstance(self.observation, Unset):
            observation = UNSET
        elif isinstance(self.observation, str):
            observation = (None, str(self.observation).encode(), "text/plain")
        else:
            observation = (None, str(self.observation).encode(), "text/plain")

        selected = (
            self.selected if isinstance(self.selected, Unset) else (None, str(self.selected).encode(), "text/plain")
        )

        mapping_inference = (
            self.mapping_inference
            if isinstance(self.mapping_inference, Unset)
            else (None, str(self.mapping_inference).encode(), "text/plain")
        )

        answer = self.answer if isinstance(self.answer, Unset) else (None, str(self.answer).encode(), "text/plain")

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        compliance_assessment: Unset | bytes = UNSET
        if not isinstance(self.compliance_assessment, Unset):
            compliance_assessment = str(self.compliance_assessment)

        requirement: Unset | bytes = UNSET
        if not isinstance(self.requirement, Unset):
            requirement = str(self.requirement)

        evidences: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.evidences, Unset):
            _temp_evidences = []
            for evidences_item_data in self.evidences:
                evidences_item = str(evidences_item_data)
                _temp_evidences.append(evidences_item)
            evidences = (None, json.dumps(_temp_evidences).encode(), "application/json")

        applied_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            _temp_applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                _temp_applied_controls.append(applied_controls_item)
            applied_controls = (None, json.dumps(_temp_applied_controls).encode(), "application/json")

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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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
        if folder is not UNSET:
            field_dict["folder"] = folder
        if compliance_assessment is not UNSET:
            field_dict["compliance_assessment"] = compliance_assessment
        if requirement is not UNSET:
            field_dict["requirement"] = requirement
        if evidences is not UNSET:
            field_dict["evidences"] = evidences
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
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

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        _compliance_assessment = d.pop("compliance_assessment", UNSET)
        compliance_assessment: Unset | UUID
        if isinstance(_compliance_assessment, Unset):
            compliance_assessment = UNSET
        else:
            compliance_assessment = UUID(_compliance_assessment)

        _requirement = d.pop("requirement", UNSET)
        requirement: Unset | UUID
        if isinstance(_requirement, Unset):
            requirement = UNSET
        else:
            requirement = UUID(_requirement)

        evidences = []
        _evidences = d.pop("evidences", UNSET)
        for evidences_item_data in _evidences or []:
            evidences_item = UUID(evidences_item_data)

            evidences.append(evidences_item)

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

        security_exceptions = []
        _security_exceptions = d.pop("security_exceptions", UNSET)
        for security_exceptions_item_data in _security_exceptions or []:
            security_exceptions_item = UUID(security_exceptions_item_data)

            security_exceptions.append(security_exceptions_item)

        patched_requirement_assessment_write = cls(
            id=id,
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
            folder=folder,
            compliance_assessment=compliance_assessment,
            requirement=requirement,
            evidences=evidences,
            applied_controls=applied_controls,
            security_exceptions=security_exceptions,
        )

        patched_requirement_assessment_write.additional_properties = d
        return patched_requirement_assessment_write

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
