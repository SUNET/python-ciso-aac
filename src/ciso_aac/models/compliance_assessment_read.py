import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.status_72a_enum import Status72AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceAssessmentRead")


@_attrs_define
class ComplianceAssessmentRead:
    """
    Attributes:
        id (UUID):
        perimeter (str):
        authors (list[str]):
        reviewers (list[str]):
        folder (str):
        framework (str):
        selected_implementation_groups (str):
        progress (int):
        assets (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        eta (Union[None, Unset, datetime.date]):
        due_date (Union[None, Unset, datetime.date]):
        version (Union[None, Unset, str]): Version of the compliance assessment (eg. 1.0, 2.0, etc.)
        status (Union[BlankEnum, None, Status72AEnum, Unset]):
        observation (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        min_score (Union[None, Unset, int]):
        max_score (Union[None, Unset, int]):
        scores_definition (Union[Unset, Any]):
        show_documentation_score (Union[Unset, bool]):
    """

    id: UUID
    perimeter: str
    authors: list[str]
    reviewers: list[str]
    folder: str
    framework: str
    selected_implementation_groups: str
    progress: int
    assets: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Unset | bool = UNSET
    description: None | Unset | str = UNSET
    eta: None | Unset | datetime.date = UNSET
    due_date: None | Unset | datetime.date = UNSET
    version: None | Unset | str = UNSET
    status: BlankEnum | None | Status72AEnum | Unset = UNSET
    observation: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    min_score: None | Unset | int = UNSET
    max_score: None | Unset | int = UNSET
    scores_definition: Unset | Any = UNSET
    show_documentation_score: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        perimeter = self.perimeter

        authors = self.authors

        reviewers = self.reviewers

        folder = self.folder

        framework = self.framework

        selected_implementation_groups = self.selected_implementation_groups

        progress = self.progress

        assets = self.assets

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        is_published = self.is_published

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        version: None | Unset | str
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        status: None | Unset | str
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status72AEnum):
            status = self.status.value
        elif isinstance(self.status, BlankEnum):
            status = self.status.value
        else:
            status = self.status

        observation: None | Unset | str
        if isinstance(self.observation, Unset):
            observation = UNSET
        else:
            observation = self.observation

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        min_score: None | Unset | int
        if isinstance(self.min_score, Unset):
            min_score = UNSET
        else:
            min_score = self.min_score

        max_score: None | Unset | int
        if isinstance(self.max_score, Unset):
            max_score = UNSET
        else:
            max_score = self.max_score

        scores_definition = self.scores_definition

        show_documentation_score = self.show_documentation_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "perimeter": perimeter,
                "authors": authors,
                "reviewers": reviewers,
                "folder": folder,
                "framework": framework,
                "selected_implementation_groups": selected_implementation_groups,
                "progress": progress,
                "assets": assets,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if eta is not UNSET:
            field_dict["eta"] = eta
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if observation is not UNSET:
            field_dict["observation"] = observation
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if min_score is not UNSET:
            field_dict["min_score"] = min_score
        if max_score is not UNSET:
            field_dict["max_score"] = max_score
        if scores_definition is not UNSET:
            field_dict["scores_definition"] = scores_definition
        if show_documentation_score is not UNSET:
            field_dict["show_documentation_score"] = show_documentation_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        perimeter = d.pop("perimeter")

        authors = cast(list[str], d.pop("authors"))

        reviewers = cast(list[str], d.pop("reviewers"))

        folder = d.pop("folder")

        framework = d.pop("framework")

        selected_implementation_groups = d.pop("selected_implementation_groups")

        progress = d.pop("progress")

        assets = cast(list[str], d.pop("assets"))

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

        def _parse_version(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_status(data: object) -> BlankEnum | None | Status72AEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = Status72AEnum(data)

                return status_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = BlankEnum(data)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(BlankEnum | None | Status72AEnum | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_observation(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        observation = _parse_observation(d.pop("observation", UNSET))

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_min_score(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        min_score = _parse_min_score(d.pop("min_score", UNSET))

        def _parse_max_score(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        max_score = _parse_max_score(d.pop("max_score", UNSET))

        scores_definition = d.pop("scores_definition", UNSET)

        show_documentation_score = d.pop("show_documentation_score", UNSET)

        compliance_assessment_read = cls(
            id=id,
            perimeter=perimeter,
            authors=authors,
            reviewers=reviewers,
            folder=folder,
            framework=framework,
            selected_implementation_groups=selected_implementation_groups,
            progress=progress,
            assets=assets,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            eta=eta,
            due_date=due_date,
            version=version,
            status=status,
            observation=observation,
            ref_id=ref_id,
            min_score=min_score,
            max_score=max_score,
            scores_definition=scores_definition,
            show_documentation_score=show_documentation_score,
        )

        compliance_assessment_read.additional_properties = d
        return compliance_assessment_read

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
