import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.treatment_enum import TreatmentEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRiskScenarioWrite")


@_attrs_define
class PatchedRiskScenarioWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        risk_matrix (Union[Unset, UUID]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        existing_controls (Union[Unset, str]): The existing controls to manage this risk. Edit the risk scenario to add
            extra applied controls.
        current_proba (Union[Unset, int]):
        current_impact (Union[Unset, int]):
        current_level (Union[Unset, int]): The risk level given the current measures. Automatically updated on Save,
            based on the chosen risk matrix
        residual_proba (Union[Unset, int]):
        residual_impact (Union[Unset, int]):
        residual_level (Union[Unset, int]): The risk level when all the extra measures are done. Automatically updated
            on Save, based on the chosen risk matrix
        treatment (Union[Unset, TreatmentEnum]): * `open` - Open
            * `mitigate` - Mitigate
            * `accept` - Accept
            * `avoid` - Avoid
            * `transfer` - Transfer
        ref_id (Union[Unset, str]):
        qualifications (Union[Unset, Any]):
        strength_of_knowledge (Union[Unset, int]): The strength of the knowledge supporting the assessment
        justification (Union[None, Unset, str]):
        risk_assessment (Union[Unset, UUID]):
        assets (Union[Unset, list[UUID]]): Assets impacted by the risk scenario
        vulnerabilities (Union[Unset, list[UUID]]): Vulnerabities exploited by the risk scenario
        applied_controls (Union[Unset, list[UUID]]):
        threats (Union[Unset, list[UUID]]):
        existing_applied_controls (Union[Unset, list[UUID]]):
        owner (Union[Unset, list[UUID]]):
        security_exceptions (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    risk_matrix: Unset | UUID = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    existing_controls: Unset | str = UNSET
    current_proba: Unset | int = UNSET
    current_impact: Unset | int = UNSET
    current_level: Unset | int = UNSET
    residual_proba: Unset | int = UNSET
    residual_impact: Unset | int = UNSET
    residual_level: Unset | int = UNSET
    treatment: Unset | TreatmentEnum = UNSET
    ref_id: Unset | str = UNSET
    qualifications: Unset | Any = UNSET
    strength_of_knowledge: Unset | int = UNSET
    justification: None | Unset | str = UNSET
    risk_assessment: Unset | UUID = UNSET
    assets: Unset | list[UUID] = UNSET
    vulnerabilities: Unset | list[UUID] = UNSET
    applied_controls: Unset | list[UUID] = UNSET
    threats: Unset | list[UUID] = UNSET
    existing_applied_controls: Unset | list[UUID] = UNSET
    owner: Unset | list[UUID] = UNSET
    security_exceptions: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        risk_matrix: Unset | str = UNSET
        if not isinstance(self.risk_matrix, Unset):
            risk_matrix = str(self.risk_matrix)

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        existing_controls = self.existing_controls

        current_proba = self.current_proba

        current_impact = self.current_impact

        current_level = self.current_level

        residual_proba = self.residual_proba

        residual_impact = self.residual_impact

        residual_level = self.residual_level

        treatment: Unset | str = UNSET
        if not isinstance(self.treatment, Unset):
            treatment = self.treatment.value

        ref_id = self.ref_id

        qualifications = self.qualifications

        strength_of_knowledge = self.strength_of_knowledge

        justification: None | Unset | str
        if isinstance(self.justification, Unset):
            justification = UNSET
        else:
            justification = self.justification

        risk_assessment: Unset | str = UNSET
        if not isinstance(self.risk_assessment, Unset):
            risk_assessment = str(self.risk_assessment)

        assets: Unset | list[str] = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                assets.append(assets_item)

        vulnerabilities: Unset | list[str] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = str(vulnerabilities_item_data)
                vulnerabilities.append(vulnerabilities_item)

        applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

        threats: Unset | list[str] = UNSET
        if not isinstance(self.threats, Unset):
            threats = []
            for threats_item_data in self.threats:
                threats_item = str(threats_item_data)
                threats.append(threats_item)

        existing_applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.existing_applied_controls, Unset):
            existing_applied_controls = []
            for existing_applied_controls_item_data in self.existing_applied_controls:
                existing_applied_controls_item = str(existing_applied_controls_item_data)
                existing_applied_controls.append(existing_applied_controls_item)

        owner: Unset | list[str] = UNSET
        if not isinstance(self.owner, Unset):
            owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                owner.append(owner_item)

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
        if risk_matrix is not UNSET:
            field_dict["risk_matrix"] = risk_matrix
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if existing_controls is not UNSET:
            field_dict["existing_controls"] = existing_controls
        if current_proba is not UNSET:
            field_dict["current_proba"] = current_proba
        if current_impact is not UNSET:
            field_dict["current_impact"] = current_impact
        if current_level is not UNSET:
            field_dict["current_level"] = current_level
        if residual_proba is not UNSET:
            field_dict["residual_proba"] = residual_proba
        if residual_impact is not UNSET:
            field_dict["residual_impact"] = residual_impact
        if residual_level is not UNSET:
            field_dict["residual_level"] = residual_level
        if treatment is not UNSET:
            field_dict["treatment"] = treatment
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications
        if strength_of_knowledge is not UNSET:
            field_dict["strength_of_knowledge"] = strength_of_knowledge
        if justification is not UNSET:
            field_dict["justification"] = justification
        if risk_assessment is not UNSET:
            field_dict["risk_assessment"] = risk_assessment
        if assets is not UNSET:
            field_dict["assets"] = assets
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if threats is not UNSET:
            field_dict["threats"] = threats
        if existing_applied_controls is not UNSET:
            field_dict["existing_applied_controls"] = existing_applied_controls
        if owner is not UNSET:
            field_dict["owner"] = owner
        if security_exceptions is not UNSET:
            field_dict["security_exceptions"] = security_exceptions

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        risk_matrix: Unset | bytes = UNSET
        if not isinstance(self.risk_matrix, Unset):
            risk_matrix = str(self.risk_matrix)

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

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        existing_controls = (
            self.existing_controls
            if isinstance(self.existing_controls, Unset)
            else (None, str(self.existing_controls).encode(), "text/plain")
        )

        current_proba = (
            self.current_proba
            if isinstance(self.current_proba, Unset)
            else (None, str(self.current_proba).encode(), "text/plain")
        )

        current_impact = (
            self.current_impact
            if isinstance(self.current_impact, Unset)
            else (None, str(self.current_impact).encode(), "text/plain")
        )

        current_level = (
            self.current_level
            if isinstance(self.current_level, Unset)
            else (None, str(self.current_level).encode(), "text/plain")
        )

        residual_proba = (
            self.residual_proba
            if isinstance(self.residual_proba, Unset)
            else (None, str(self.residual_proba).encode(), "text/plain")
        )

        residual_impact = (
            self.residual_impact
            if isinstance(self.residual_impact, Unset)
            else (None, str(self.residual_impact).encode(), "text/plain")
        )

        residual_level = (
            self.residual_level
            if isinstance(self.residual_level, Unset)
            else (None, str(self.residual_level).encode(), "text/plain")
        )

        treatment: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.treatment, Unset):
            treatment = (None, str(self.treatment.value).encode(), "text/plain")

        ref_id = self.ref_id if isinstance(self.ref_id, Unset) else (None, str(self.ref_id).encode(), "text/plain")

        qualifications = (
            self.qualifications
            if isinstance(self.qualifications, Unset)
            else (None, str(self.qualifications).encode(), "text/plain")
        )

        strength_of_knowledge = (
            self.strength_of_knowledge
            if isinstance(self.strength_of_knowledge, Unset)
            else (None, str(self.strength_of_knowledge).encode(), "text/plain")
        )

        justification: Unset | tuple[None, bytes, str]

        if isinstance(self.justification, Unset):
            justification = UNSET
        elif isinstance(self.justification, str):
            justification = (None, str(self.justification).encode(), "text/plain")
        else:
            justification = (None, str(self.justification).encode(), "text/plain")

        risk_assessment: Unset | bytes = UNSET
        if not isinstance(self.risk_assessment, Unset):
            risk_assessment = str(self.risk_assessment)

        assets: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.assets, Unset):
            _temp_assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                _temp_assets.append(assets_item)
            assets = (None, json.dumps(_temp_assets).encode(), "application/json")

        vulnerabilities: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            _temp_vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = str(vulnerabilities_item_data)
                _temp_vulnerabilities.append(vulnerabilities_item)
            vulnerabilities = (None, json.dumps(_temp_vulnerabilities).encode(), "application/json")

        applied_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            _temp_applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                _temp_applied_controls.append(applied_controls_item)
            applied_controls = (None, json.dumps(_temp_applied_controls).encode(), "application/json")

        threats: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.threats, Unset):
            _temp_threats = []
            for threats_item_data in self.threats:
                threats_item = str(threats_item_data)
                _temp_threats.append(threats_item)
            threats = (None, json.dumps(_temp_threats).encode(), "application/json")

        existing_applied_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.existing_applied_controls, Unset):
            _temp_existing_applied_controls = []
            for existing_applied_controls_item_data in self.existing_applied_controls:
                existing_applied_controls_item = str(existing_applied_controls_item_data)
                _temp_existing_applied_controls.append(existing_applied_controls_item)
            existing_applied_controls = (None, json.dumps(_temp_existing_applied_controls).encode(), "application/json")

        owner: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.owner, Unset):
            _temp_owner = []
            for owner_item_data in self.owner:
                owner_item = str(owner_item_data)
                _temp_owner.append(owner_item)
            owner = (None, json.dumps(_temp_owner).encode(), "application/json")

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
        if risk_matrix is not UNSET:
            field_dict["risk_matrix"] = risk_matrix
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if existing_controls is not UNSET:
            field_dict["existing_controls"] = existing_controls
        if current_proba is not UNSET:
            field_dict["current_proba"] = current_proba
        if current_impact is not UNSET:
            field_dict["current_impact"] = current_impact
        if current_level is not UNSET:
            field_dict["current_level"] = current_level
        if residual_proba is not UNSET:
            field_dict["residual_proba"] = residual_proba
        if residual_impact is not UNSET:
            field_dict["residual_impact"] = residual_impact
        if residual_level is not UNSET:
            field_dict["residual_level"] = residual_level
        if treatment is not UNSET:
            field_dict["treatment"] = treatment
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications
        if strength_of_knowledge is not UNSET:
            field_dict["strength_of_knowledge"] = strength_of_knowledge
        if justification is not UNSET:
            field_dict["justification"] = justification
        if risk_assessment is not UNSET:
            field_dict["risk_assessment"] = risk_assessment
        if assets is not UNSET:
            field_dict["assets"] = assets
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if threats is not UNSET:
            field_dict["threats"] = threats
        if existing_applied_controls is not UNSET:
            field_dict["existing_applied_controls"] = existing_applied_controls
        if owner is not UNSET:
            field_dict["owner"] = owner
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

        _risk_matrix = d.pop("risk_matrix", UNSET)
        risk_matrix: Unset | UUID
        if isinstance(_risk_matrix, Unset):
            risk_matrix = UNSET
        else:
            risk_matrix = UUID(_risk_matrix)

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

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        existing_controls = d.pop("existing_controls", UNSET)

        current_proba = d.pop("current_proba", UNSET)

        current_impact = d.pop("current_impact", UNSET)

        current_level = d.pop("current_level", UNSET)

        residual_proba = d.pop("residual_proba", UNSET)

        residual_impact = d.pop("residual_impact", UNSET)

        residual_level = d.pop("residual_level", UNSET)

        _treatment = d.pop("treatment", UNSET)
        treatment: Unset | TreatmentEnum
        if isinstance(_treatment, Unset):
            treatment = UNSET
        else:
            treatment = TreatmentEnum(_treatment)

        ref_id = d.pop("ref_id", UNSET)

        qualifications = d.pop("qualifications", UNSET)

        strength_of_knowledge = d.pop("strength_of_knowledge", UNSET)

        def _parse_justification(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        justification = _parse_justification(d.pop("justification", UNSET))

        _risk_assessment = d.pop("risk_assessment", UNSET)
        risk_assessment: Unset | UUID
        if isinstance(_risk_assessment, Unset):
            risk_assessment = UNSET
        else:
            risk_assessment = UUID(_risk_assessment)

        assets = []
        _assets = d.pop("assets", UNSET)
        for assets_item_data in _assets or []:
            assets_item = UUID(assets_item_data)

            assets.append(assets_item)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = UUID(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

        threats = []
        _threats = d.pop("threats", UNSET)
        for threats_item_data in _threats or []:
            threats_item = UUID(threats_item_data)

            threats.append(threats_item)

        existing_applied_controls = []
        _existing_applied_controls = d.pop("existing_applied_controls", UNSET)
        for existing_applied_controls_item_data in _existing_applied_controls or []:
            existing_applied_controls_item = UUID(existing_applied_controls_item_data)

            existing_applied_controls.append(existing_applied_controls_item)

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

        patched_risk_scenario_write = cls(
            id=id,
            risk_matrix=risk_matrix,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            name=name,
            description=description,
            existing_controls=existing_controls,
            current_proba=current_proba,
            current_impact=current_impact,
            current_level=current_level,
            residual_proba=residual_proba,
            residual_impact=residual_impact,
            residual_level=residual_level,
            treatment=treatment,
            ref_id=ref_id,
            qualifications=qualifications,
            strength_of_knowledge=strength_of_knowledge,
            justification=justification,
            risk_assessment=risk_assessment,
            assets=assets,
            vulnerabilities=vulnerabilities,
            applied_controls=applied_controls,
            threats=threats,
            existing_applied_controls=existing_applied_controls,
            owner=owner,
            security_exceptions=security_exceptions,
        )

        patched_risk_scenario_write.additional_properties = d
        return patched_risk_scenario_write

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
