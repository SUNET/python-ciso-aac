import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..models.name_enum import NameEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SSOSettingsWrite")


@_attrs_define
class SSOSettingsWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_enabled (Union[Unset, bool]):
        provider (Union[None, Unset, str]):
        provider_id (Union[None, Unset, str]):
        client_id (Union[None, Unset, str]):
        provider_name (Union[None, Unset, str]):
        attribute_mapping_uid (Union[None, Unset, list[Union[None, str]]]):
        attribute_mapping_email_verified (Union[None, Unset, list[Union[None, str]]]):
        attribute_mapping_email (Union[None, Unset, list[Union[None, str]]]):
        idp_entity_id (Union[None, Unset, str]):
        metadata_url (Union[None, Unset, str]):
        sso_url (Union[None, Unset, str]):
        slo_url (Union[None, Unset, str]):
        x509cert (Union[None, Unset, str]):
        sp_entity_id (Union[None, Unset, str]):
        allow_repeat_attribute_name (Union[Unset, bool]):
        allow_single_label_domains (Union[Unset, bool]):
        authn_request_signed (Union[Unset, bool]):
        digest_algorithm (Union[None, Unset, str]):
        logout_request_signed (Union[Unset, bool]):
        logout_response_signed (Union[Unset, bool]):
        metadata_signed (Union[Unset, bool]):
        name_id_encrypted (Union[Unset, bool]):
        reject_deprecated_algorithm (Union[Unset, bool]):
        reject_idp_initiated_sso (Union[Unset, bool]):
        signature_algorithm (Union[None, Unset, str]):
        want_assertion_encrypted (Union[Unset, bool]):
        want_assertion_signed (Union[Unset, bool]):
        want_attribute_statement (Union[Unset, bool]):
        want_message_signed (Union[Unset, bool]):
        want_name_id (Union[Unset, bool]):
        want_name_id_encrypted (Union[Unset, bool]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, NameEnum]): * `general` - General
            * `sso` - SSO
        secret (Union[Unset, str]): API secret, client secret, or consumer secret
        key (Union[Unset, str]): Key
        settings (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_enabled: Unset | bool = UNSET
    provider: None | Unset | str = UNSET
    provider_id: None | Unset | str = UNSET
    client_id: None | Unset | str = UNSET
    provider_name: None | Unset | str = UNSET
    attribute_mapping_uid: None | Unset | list[None | str] = UNSET
    attribute_mapping_email_verified: None | Unset | list[None | str] = UNSET
    attribute_mapping_email: None | Unset | list[None | str] = UNSET
    idp_entity_id: None | Unset | str = UNSET
    metadata_url: None | Unset | str = UNSET
    sso_url: None | Unset | str = UNSET
    slo_url: None | Unset | str = UNSET
    x509cert: None | Unset | str = UNSET
    sp_entity_id: None | Unset | str = UNSET
    allow_repeat_attribute_name: Unset | bool = UNSET
    allow_single_label_domains: Unset | bool = UNSET
    authn_request_signed: Unset | bool = UNSET
    digest_algorithm: None | Unset | str = UNSET
    logout_request_signed: Unset | bool = UNSET
    logout_response_signed: Unset | bool = UNSET
    metadata_signed: Unset | bool = UNSET
    name_id_encrypted: Unset | bool = UNSET
    reject_deprecated_algorithm: Unset | bool = UNSET
    reject_idp_initiated_sso: Unset | bool = UNSET
    signature_algorithm: None | Unset | str = UNSET
    want_assertion_encrypted: Unset | bool = UNSET
    want_assertion_signed: Unset | bool = UNSET
    want_attribute_statement: Unset | bool = UNSET
    want_message_signed: Unset | bool = UNSET
    want_name_id: Unset | bool = UNSET
    want_name_id_encrypted: Unset | bool = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | NameEnum = UNSET
    secret: Unset | str = UNSET
    key: Unset | str = UNSET
    settings: Unset | Any = UNSET
    folder: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_enabled = self.is_enabled

        provider: None | Unset | str
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        provider_id: None | Unset | str
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        client_id: None | Unset | str
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        provider_name: None | Unset | str
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        attribute_mapping_uid: None | Unset | list[None | str]
        if isinstance(self.attribute_mapping_uid, Unset):
            attribute_mapping_uid = UNSET
        elif isinstance(self.attribute_mapping_uid, list):
            attribute_mapping_uid = []
            for attribute_mapping_uid_type_0_item_data in self.attribute_mapping_uid:
                attribute_mapping_uid_type_0_item: None | str
                attribute_mapping_uid_type_0_item = attribute_mapping_uid_type_0_item_data
                attribute_mapping_uid.append(attribute_mapping_uid_type_0_item)

        else:
            attribute_mapping_uid = self.attribute_mapping_uid

        attribute_mapping_email_verified: None | Unset | list[None | str]
        if isinstance(self.attribute_mapping_email_verified, Unset):
            attribute_mapping_email_verified = UNSET
        elif isinstance(self.attribute_mapping_email_verified, list):
            attribute_mapping_email_verified = []
            for attribute_mapping_email_verified_type_0_item_data in self.attribute_mapping_email_verified:
                attribute_mapping_email_verified_type_0_item: None | str
                attribute_mapping_email_verified_type_0_item = attribute_mapping_email_verified_type_0_item_data
                attribute_mapping_email_verified.append(attribute_mapping_email_verified_type_0_item)

        else:
            attribute_mapping_email_verified = self.attribute_mapping_email_verified

        attribute_mapping_email: None | Unset | list[None | str]
        if isinstance(self.attribute_mapping_email, Unset):
            attribute_mapping_email = UNSET
        elif isinstance(self.attribute_mapping_email, list):
            attribute_mapping_email = []
            for attribute_mapping_email_type_0_item_data in self.attribute_mapping_email:
                attribute_mapping_email_type_0_item: None | str
                attribute_mapping_email_type_0_item = attribute_mapping_email_type_0_item_data
                attribute_mapping_email.append(attribute_mapping_email_type_0_item)

        else:
            attribute_mapping_email = self.attribute_mapping_email

        idp_entity_id: None | Unset | str
        if isinstance(self.idp_entity_id, Unset):
            idp_entity_id = UNSET
        else:
            idp_entity_id = self.idp_entity_id

        metadata_url: None | Unset | str
        if isinstance(self.metadata_url, Unset):
            metadata_url = UNSET
        else:
            metadata_url = self.metadata_url

        sso_url: None | Unset | str
        if isinstance(self.sso_url, Unset):
            sso_url = UNSET
        else:
            sso_url = self.sso_url

        slo_url: None | Unset | str
        if isinstance(self.slo_url, Unset):
            slo_url = UNSET
        else:
            slo_url = self.slo_url

        x509cert: None | Unset | str
        if isinstance(self.x509cert, Unset):
            x509cert = UNSET
        else:
            x509cert = self.x509cert

        sp_entity_id: None | Unset | str
        if isinstance(self.sp_entity_id, Unset):
            sp_entity_id = UNSET
        else:
            sp_entity_id = self.sp_entity_id

        allow_repeat_attribute_name = self.allow_repeat_attribute_name

        allow_single_label_domains = self.allow_single_label_domains

        authn_request_signed = self.authn_request_signed

        digest_algorithm: None | Unset | str
        if isinstance(self.digest_algorithm, Unset):
            digest_algorithm = UNSET
        else:
            digest_algorithm = self.digest_algorithm

        logout_request_signed = self.logout_request_signed

        logout_response_signed = self.logout_response_signed

        metadata_signed = self.metadata_signed

        name_id_encrypted = self.name_id_encrypted

        reject_deprecated_algorithm = self.reject_deprecated_algorithm

        reject_idp_initiated_sso = self.reject_idp_initiated_sso

        signature_algorithm: None | Unset | str
        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        else:
            signature_algorithm = self.signature_algorithm

        want_assertion_encrypted = self.want_assertion_encrypted

        want_assertion_signed = self.want_assertion_signed

        want_attribute_statement = self.want_attribute_statement

        want_message_signed = self.want_message_signed

        want_name_id = self.want_name_id

        want_name_id_encrypted = self.want_name_id_encrypted

        is_published = self.is_published

        name: Unset | str = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        secret = self.secret

        key = self.key

        settings = self.settings

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if provider_name is not UNSET:
            field_dict["provider_name"] = provider_name
        if attribute_mapping_uid is not UNSET:
            field_dict["attribute_mapping_uid"] = attribute_mapping_uid
        if attribute_mapping_email_verified is not UNSET:
            field_dict["attribute_mapping_email_verified"] = attribute_mapping_email_verified
        if attribute_mapping_email is not UNSET:
            field_dict["attribute_mapping_email"] = attribute_mapping_email
        if idp_entity_id is not UNSET:
            field_dict["idp_entity_id"] = idp_entity_id
        if metadata_url is not UNSET:
            field_dict["metadata_url"] = metadata_url
        if sso_url is not UNSET:
            field_dict["sso_url"] = sso_url
        if slo_url is not UNSET:
            field_dict["slo_url"] = slo_url
        if x509cert is not UNSET:
            field_dict["x509cert"] = x509cert
        if sp_entity_id is not UNSET:
            field_dict["sp_entity_id"] = sp_entity_id
        if allow_repeat_attribute_name is not UNSET:
            field_dict["allow_repeat_attribute_name"] = allow_repeat_attribute_name
        if allow_single_label_domains is not UNSET:
            field_dict["allow_single_label_domains"] = allow_single_label_domains
        if authn_request_signed is not UNSET:
            field_dict["authn_request_signed"] = authn_request_signed
        if digest_algorithm is not UNSET:
            field_dict["digest_algorithm"] = digest_algorithm
        if logout_request_signed is not UNSET:
            field_dict["logout_request_signed"] = logout_request_signed
        if logout_response_signed is not UNSET:
            field_dict["logout_response_signed"] = logout_response_signed
        if metadata_signed is not UNSET:
            field_dict["metadata_signed"] = metadata_signed
        if name_id_encrypted is not UNSET:
            field_dict["name_id_encrypted"] = name_id_encrypted
        if reject_deprecated_algorithm is not UNSET:
            field_dict["reject_deprecated_algorithm"] = reject_deprecated_algorithm
        if reject_idp_initiated_sso is not UNSET:
            field_dict["reject_idp_initiated_sso"] = reject_idp_initiated_sso
        if signature_algorithm is not UNSET:
            field_dict["signature_algorithm"] = signature_algorithm
        if want_assertion_encrypted is not UNSET:
            field_dict["want_assertion_encrypted"] = want_assertion_encrypted
        if want_assertion_signed is not UNSET:
            field_dict["want_assertion_signed"] = want_assertion_signed
        if want_attribute_statement is not UNSET:
            field_dict["want_attribute_statement"] = want_attribute_statement
        if want_message_signed is not UNSET:
            field_dict["want_message_signed"] = want_message_signed
        if want_name_id is not UNSET:
            field_dict["want_name_id"] = want_name_id
        if want_name_id_encrypted is not UNSET:
            field_dict["want_name_id_encrypted"] = want_name_id_encrypted
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if secret is not UNSET:
            field_dict["secret"] = secret
        if key is not UNSET:
            field_dict["key"] = key
        if settings is not UNSET:
            field_dict["settings"] = settings
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        is_enabled = (
            self.is_enabled
            if isinstance(self.is_enabled, Unset)
            else (None, str(self.is_enabled).encode(), "text/plain")
        )

        provider: Unset | tuple[None, bytes, str]

        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, str):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (None, str(self.provider).encode(), "text/plain")

        provider_id: Unset | tuple[None, bytes, str]

        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        elif isinstance(self.provider_id, str):
            provider_id = (None, str(self.provider_id).encode(), "text/plain")
        else:
            provider_id = (None, str(self.provider_id).encode(), "text/plain")

        client_id: Unset | tuple[None, bytes, str]

        if isinstance(self.client_id, Unset):
            client_id = UNSET
        elif isinstance(self.client_id, str):
            client_id = (None, str(self.client_id).encode(), "text/plain")
        else:
            client_id = (None, str(self.client_id).encode(), "text/plain")

        provider_name: Unset | tuple[None, bytes, str]

        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        elif isinstance(self.provider_name, str):
            provider_name = (None, str(self.provider_name).encode(), "text/plain")
        else:
            provider_name = (None, str(self.provider_name).encode(), "text/plain")

        attribute_mapping_uid: Unset | tuple[None, bytes, str]

        if isinstance(self.attribute_mapping_uid, Unset):
            attribute_mapping_uid = UNSET
        elif isinstance(self.attribute_mapping_uid, list):
            _temp_attribute_mapping_uid = []
            for attribute_mapping_uid_type_0_item_data in self.attribute_mapping_uid:
                attribute_mapping_uid_type_0_item: None | str
                attribute_mapping_uid_type_0_item = attribute_mapping_uid_type_0_item_data
                _temp_attribute_mapping_uid.append(attribute_mapping_uid_type_0_item)
            attribute_mapping_uid = (None, json.dumps(_temp_attribute_mapping_uid).encode(), "application/json")
        else:
            attribute_mapping_uid = (None, str(self.attribute_mapping_uid).encode(), "text/plain")

        attribute_mapping_email_verified: Unset | tuple[None, bytes, str]

        if isinstance(self.attribute_mapping_email_verified, Unset):
            attribute_mapping_email_verified = UNSET
        elif isinstance(self.attribute_mapping_email_verified, list):
            _temp_attribute_mapping_email_verified = []
            for attribute_mapping_email_verified_type_0_item_data in self.attribute_mapping_email_verified:
                attribute_mapping_email_verified_type_0_item: None | str
                attribute_mapping_email_verified_type_0_item = attribute_mapping_email_verified_type_0_item_data
                _temp_attribute_mapping_email_verified.append(attribute_mapping_email_verified_type_0_item)
            attribute_mapping_email_verified = (
                None,
                json.dumps(_temp_attribute_mapping_email_verified).encode(),
                "application/json",
            )
        else:
            attribute_mapping_email_verified = (None, str(self.attribute_mapping_email_verified).encode(), "text/plain")

        attribute_mapping_email: Unset | tuple[None, bytes, str]

        if isinstance(self.attribute_mapping_email, Unset):
            attribute_mapping_email = UNSET
        elif isinstance(self.attribute_mapping_email, list):
            _temp_attribute_mapping_email = []
            for attribute_mapping_email_type_0_item_data in self.attribute_mapping_email:
                attribute_mapping_email_type_0_item: None | str
                attribute_mapping_email_type_0_item = attribute_mapping_email_type_0_item_data
                _temp_attribute_mapping_email.append(attribute_mapping_email_type_0_item)
            attribute_mapping_email = (None, json.dumps(_temp_attribute_mapping_email).encode(), "application/json")
        else:
            attribute_mapping_email = (None, str(self.attribute_mapping_email).encode(), "text/plain")

        idp_entity_id: Unset | tuple[None, bytes, str]

        if isinstance(self.idp_entity_id, Unset):
            idp_entity_id = UNSET
        elif isinstance(self.idp_entity_id, str):
            idp_entity_id = (None, str(self.idp_entity_id).encode(), "text/plain")
        else:
            idp_entity_id = (None, str(self.idp_entity_id).encode(), "text/plain")

        metadata_url: Unset | tuple[None, bytes, str]

        if isinstance(self.metadata_url, Unset):
            metadata_url = UNSET
        elif isinstance(self.metadata_url, str):
            metadata_url = (None, str(self.metadata_url).encode(), "text/plain")
        else:
            metadata_url = (None, str(self.metadata_url).encode(), "text/plain")

        sso_url: Unset | tuple[None, bytes, str]

        if isinstance(self.sso_url, Unset):
            sso_url = UNSET
        elif isinstance(self.sso_url, str):
            sso_url = (None, str(self.sso_url).encode(), "text/plain")
        else:
            sso_url = (None, str(self.sso_url).encode(), "text/plain")

        slo_url: Unset | tuple[None, bytes, str]

        if isinstance(self.slo_url, Unset):
            slo_url = UNSET
        elif isinstance(self.slo_url, str):
            slo_url = (None, str(self.slo_url).encode(), "text/plain")
        else:
            slo_url = (None, str(self.slo_url).encode(), "text/plain")

        x509cert: Unset | tuple[None, bytes, str]

        if isinstance(self.x509cert, Unset):
            x509cert = UNSET
        elif isinstance(self.x509cert, str):
            x509cert = (None, str(self.x509cert).encode(), "text/plain")
        else:
            x509cert = (None, str(self.x509cert).encode(), "text/plain")

        sp_entity_id: Unset | tuple[None, bytes, str]

        if isinstance(self.sp_entity_id, Unset):
            sp_entity_id = UNSET
        elif isinstance(self.sp_entity_id, str):
            sp_entity_id = (None, str(self.sp_entity_id).encode(), "text/plain")
        else:
            sp_entity_id = (None, str(self.sp_entity_id).encode(), "text/plain")

        allow_repeat_attribute_name = (
            self.allow_repeat_attribute_name
            if isinstance(self.allow_repeat_attribute_name, Unset)
            else (None, str(self.allow_repeat_attribute_name).encode(), "text/plain")
        )

        allow_single_label_domains = (
            self.allow_single_label_domains
            if isinstance(self.allow_single_label_domains, Unset)
            else (None, str(self.allow_single_label_domains).encode(), "text/plain")
        )

        authn_request_signed = (
            self.authn_request_signed
            if isinstance(self.authn_request_signed, Unset)
            else (None, str(self.authn_request_signed).encode(), "text/plain")
        )

        digest_algorithm: Unset | tuple[None, bytes, str]

        if isinstance(self.digest_algorithm, Unset):
            digest_algorithm = UNSET
        elif isinstance(self.digest_algorithm, str):
            digest_algorithm = (None, str(self.digest_algorithm).encode(), "text/plain")
        else:
            digest_algorithm = (None, str(self.digest_algorithm).encode(), "text/plain")

        logout_request_signed = (
            self.logout_request_signed
            if isinstance(self.logout_request_signed, Unset)
            else (None, str(self.logout_request_signed).encode(), "text/plain")
        )

        logout_response_signed = (
            self.logout_response_signed
            if isinstance(self.logout_response_signed, Unset)
            else (None, str(self.logout_response_signed).encode(), "text/plain")
        )

        metadata_signed = (
            self.metadata_signed
            if isinstance(self.metadata_signed, Unset)
            else (None, str(self.metadata_signed).encode(), "text/plain")
        )

        name_id_encrypted = (
            self.name_id_encrypted
            if isinstance(self.name_id_encrypted, Unset)
            else (None, str(self.name_id_encrypted).encode(), "text/plain")
        )

        reject_deprecated_algorithm = (
            self.reject_deprecated_algorithm
            if isinstance(self.reject_deprecated_algorithm, Unset)
            else (None, str(self.reject_deprecated_algorithm).encode(), "text/plain")
        )

        reject_idp_initiated_sso = (
            self.reject_idp_initiated_sso
            if isinstance(self.reject_idp_initiated_sso, Unset)
            else (None, str(self.reject_idp_initiated_sso).encode(), "text/plain")
        )

        signature_algorithm: Unset | tuple[None, bytes, str]

        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        elif isinstance(self.signature_algorithm, str):
            signature_algorithm = (None, str(self.signature_algorithm).encode(), "text/plain")
        else:
            signature_algorithm = (None, str(self.signature_algorithm).encode(), "text/plain")

        want_assertion_encrypted = (
            self.want_assertion_encrypted
            if isinstance(self.want_assertion_encrypted, Unset)
            else (None, str(self.want_assertion_encrypted).encode(), "text/plain")
        )

        want_assertion_signed = (
            self.want_assertion_signed
            if isinstance(self.want_assertion_signed, Unset)
            else (None, str(self.want_assertion_signed).encode(), "text/plain")
        )

        want_attribute_statement = (
            self.want_attribute_statement
            if isinstance(self.want_attribute_statement, Unset)
            else (None, str(self.want_attribute_statement).encode(), "text/plain")
        )

        want_message_signed = (
            self.want_message_signed
            if isinstance(self.want_message_signed, Unset)
            else (None, str(self.want_message_signed).encode(), "text/plain")
        )

        want_name_id = (
            self.want_name_id
            if isinstance(self.want_name_id, Unset)
            else (None, str(self.want_name_id).encode(), "text/plain")
        )

        want_name_id_encrypted = (
            self.want_name_id_encrypted
            if isinstance(self.want_name_id_encrypted, Unset)
            else (None, str(self.want_name_id_encrypted).encode(), "text/plain")
        )

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        name: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.name, Unset):
            name = (None, str(self.name.value).encode(), "text/plain")

        secret = self.secret if isinstance(self.secret, Unset) else (None, str(self.secret).encode(), "text/plain")

        key = self.key if isinstance(self.key, Unset) else (None, str(self.key).encode(), "text/plain")

        settings = (
            self.settings if isinstance(self.settings, Unset) else (None, str(self.settings).encode(), "text/plain")
        )

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if provider_name is not UNSET:
            field_dict["provider_name"] = provider_name
        if attribute_mapping_uid is not UNSET:
            field_dict["attribute_mapping_uid"] = attribute_mapping_uid
        if attribute_mapping_email_verified is not UNSET:
            field_dict["attribute_mapping_email_verified"] = attribute_mapping_email_verified
        if attribute_mapping_email is not UNSET:
            field_dict["attribute_mapping_email"] = attribute_mapping_email
        if idp_entity_id is not UNSET:
            field_dict["idp_entity_id"] = idp_entity_id
        if metadata_url is not UNSET:
            field_dict["metadata_url"] = metadata_url
        if sso_url is not UNSET:
            field_dict["sso_url"] = sso_url
        if slo_url is not UNSET:
            field_dict["slo_url"] = slo_url
        if x509cert is not UNSET:
            field_dict["x509cert"] = x509cert
        if sp_entity_id is not UNSET:
            field_dict["sp_entity_id"] = sp_entity_id
        if allow_repeat_attribute_name is not UNSET:
            field_dict["allow_repeat_attribute_name"] = allow_repeat_attribute_name
        if allow_single_label_domains is not UNSET:
            field_dict["allow_single_label_domains"] = allow_single_label_domains
        if authn_request_signed is not UNSET:
            field_dict["authn_request_signed"] = authn_request_signed
        if digest_algorithm is not UNSET:
            field_dict["digest_algorithm"] = digest_algorithm
        if logout_request_signed is not UNSET:
            field_dict["logout_request_signed"] = logout_request_signed
        if logout_response_signed is not UNSET:
            field_dict["logout_response_signed"] = logout_response_signed
        if metadata_signed is not UNSET:
            field_dict["metadata_signed"] = metadata_signed
        if name_id_encrypted is not UNSET:
            field_dict["name_id_encrypted"] = name_id_encrypted
        if reject_deprecated_algorithm is not UNSET:
            field_dict["reject_deprecated_algorithm"] = reject_deprecated_algorithm
        if reject_idp_initiated_sso is not UNSET:
            field_dict["reject_idp_initiated_sso"] = reject_idp_initiated_sso
        if signature_algorithm is not UNSET:
            field_dict["signature_algorithm"] = signature_algorithm
        if want_assertion_encrypted is not UNSET:
            field_dict["want_assertion_encrypted"] = want_assertion_encrypted
        if want_assertion_signed is not UNSET:
            field_dict["want_assertion_signed"] = want_assertion_signed
        if want_attribute_statement is not UNSET:
            field_dict["want_attribute_statement"] = want_attribute_statement
        if want_message_signed is not UNSET:
            field_dict["want_message_signed"] = want_message_signed
        if want_name_id is not UNSET:
            field_dict["want_name_id"] = want_name_id
        if want_name_id_encrypted is not UNSET:
            field_dict["want_name_id_encrypted"] = want_name_id_encrypted
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
        if secret is not UNSET:
            field_dict["secret"] = secret
        if key is not UNSET:
            field_dict["key"] = key
        if settings is not UNSET:
            field_dict["settings"] = settings
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_enabled = d.pop("is_enabled", UNSET)

        def _parse_provider(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_provider_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        def _parse_client_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_provider_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider_name = _parse_provider_name(d.pop("provider_name", UNSET))

        def _parse_attribute_mapping_uid(data: object) -> None | Unset | list[None | str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attribute_mapping_uid_type_0 = []
                _attribute_mapping_uid_type_0 = data
                for attribute_mapping_uid_type_0_item_data in _attribute_mapping_uid_type_0:

                    def _parse_attribute_mapping_uid_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    attribute_mapping_uid_type_0_item = _parse_attribute_mapping_uid_type_0_item(
                        attribute_mapping_uid_type_0_item_data
                    )

                    attribute_mapping_uid_type_0.append(attribute_mapping_uid_type_0_item)

                return attribute_mapping_uid_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[None | str], data)

        attribute_mapping_uid = _parse_attribute_mapping_uid(d.pop("attribute_mapping_uid", UNSET))

        def _parse_attribute_mapping_email_verified(data: object) -> None | Unset | list[None | str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attribute_mapping_email_verified_type_0 = []
                _attribute_mapping_email_verified_type_0 = data
                for attribute_mapping_email_verified_type_0_item_data in _attribute_mapping_email_verified_type_0:

                    def _parse_attribute_mapping_email_verified_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    attribute_mapping_email_verified_type_0_item = _parse_attribute_mapping_email_verified_type_0_item(
                        attribute_mapping_email_verified_type_0_item_data
                    )

                    attribute_mapping_email_verified_type_0.append(attribute_mapping_email_verified_type_0_item)

                return attribute_mapping_email_verified_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[None | str], data)

        attribute_mapping_email_verified = _parse_attribute_mapping_email_verified(
            d.pop("attribute_mapping_email_verified", UNSET)
        )

        def _parse_attribute_mapping_email(data: object) -> None | Unset | list[None | str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attribute_mapping_email_type_0 = []
                _attribute_mapping_email_type_0 = data
                for attribute_mapping_email_type_0_item_data in _attribute_mapping_email_type_0:

                    def _parse_attribute_mapping_email_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    attribute_mapping_email_type_0_item = _parse_attribute_mapping_email_type_0_item(
                        attribute_mapping_email_type_0_item_data
                    )

                    attribute_mapping_email_type_0.append(attribute_mapping_email_type_0_item)

                return attribute_mapping_email_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[None | str], data)

        attribute_mapping_email = _parse_attribute_mapping_email(d.pop("attribute_mapping_email", UNSET))

        def _parse_idp_entity_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        idp_entity_id = _parse_idp_entity_id(d.pop("idp_entity_id", UNSET))

        def _parse_metadata_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        metadata_url = _parse_metadata_url(d.pop("metadata_url", UNSET))

        def _parse_sso_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        sso_url = _parse_sso_url(d.pop("sso_url", UNSET))

        def _parse_slo_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slo_url = _parse_slo_url(d.pop("slo_url", UNSET))

        def _parse_x509cert(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        x509cert = _parse_x509cert(d.pop("x509cert", UNSET))

        def _parse_sp_entity_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        sp_entity_id = _parse_sp_entity_id(d.pop("sp_entity_id", UNSET))

        allow_repeat_attribute_name = d.pop("allow_repeat_attribute_name", UNSET)

        allow_single_label_domains = d.pop("allow_single_label_domains", UNSET)

        authn_request_signed = d.pop("authn_request_signed", UNSET)

        def _parse_digest_algorithm(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        digest_algorithm = _parse_digest_algorithm(d.pop("digest_algorithm", UNSET))

        logout_request_signed = d.pop("logout_request_signed", UNSET)

        logout_response_signed = d.pop("logout_response_signed", UNSET)

        metadata_signed = d.pop("metadata_signed", UNSET)

        name_id_encrypted = d.pop("name_id_encrypted", UNSET)

        reject_deprecated_algorithm = d.pop("reject_deprecated_algorithm", UNSET)

        reject_idp_initiated_sso = d.pop("reject_idp_initiated_sso", UNSET)

        def _parse_signature_algorithm(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        signature_algorithm = _parse_signature_algorithm(d.pop("signature_algorithm", UNSET))

        want_assertion_encrypted = d.pop("want_assertion_encrypted", UNSET)

        want_assertion_signed = d.pop("want_assertion_signed", UNSET)

        want_attribute_statement = d.pop("want_attribute_statement", UNSET)

        want_message_signed = d.pop("want_message_signed", UNSET)

        want_name_id = d.pop("want_name_id", UNSET)

        want_name_id_encrypted = d.pop("want_name_id_encrypted", UNSET)

        is_published = d.pop("is_published", UNSET)

        _name = d.pop("name", UNSET)
        name: Unset | NameEnum
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = NameEnum(_name)

        secret = d.pop("secret", UNSET)

        key = d.pop("key", UNSET)

        settings = d.pop("settings", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        sso_settings_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            is_enabled=is_enabled,
            provider=provider,
            provider_id=provider_id,
            client_id=client_id,
            provider_name=provider_name,
            attribute_mapping_uid=attribute_mapping_uid,
            attribute_mapping_email_verified=attribute_mapping_email_verified,
            attribute_mapping_email=attribute_mapping_email,
            idp_entity_id=idp_entity_id,
            metadata_url=metadata_url,
            sso_url=sso_url,
            slo_url=slo_url,
            x509cert=x509cert,
            sp_entity_id=sp_entity_id,
            allow_repeat_attribute_name=allow_repeat_attribute_name,
            allow_single_label_domains=allow_single_label_domains,
            authn_request_signed=authn_request_signed,
            digest_algorithm=digest_algorithm,
            logout_request_signed=logout_request_signed,
            logout_response_signed=logout_response_signed,
            metadata_signed=metadata_signed,
            name_id_encrypted=name_id_encrypted,
            reject_deprecated_algorithm=reject_deprecated_algorithm,
            reject_idp_initiated_sso=reject_idp_initiated_sso,
            signature_algorithm=signature_algorithm,
            want_assertion_encrypted=want_assertion_encrypted,
            want_assertion_signed=want_assertion_signed,
            want_attribute_statement=want_attribute_statement,
            want_message_signed=want_message_signed,
            want_name_id=want_name_id,
            want_name_id_encrypted=want_name_id_encrypted,
            is_published=is_published,
            name=name,
            secret=secret,
            key=key,
            settings=settings,
            folder=folder,
        )

        sso_settings_write.additional_properties = d
        return sso_settings_write

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
