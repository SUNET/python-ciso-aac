from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="ChangePassword")


@_attrs_define
class ChangePassword:
    """Serializer for password change endpoint.

    Attributes:
        old_password (str):
        new_password (str):
        confirm_new_password (str):
    """

    old_password: str
    new_password: str
    confirm_new_password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_password = self.old_password

        new_password = self.new_password

        confirm_new_password = self.confirm_new_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old_password": old_password,
                "new_password": new_password,
                "confirm_new_password": confirm_new_password,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        old_password = (None, str(self.old_password).encode(), "text/plain")

        new_password = (None, str(self.new_password).encode(), "text/plain")

        confirm_new_password = (None, str(self.confirm_new_password).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "old_password": old_password,
                "new_password": new_password,
                "confirm_new_password": confirm_new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        old_password = d.pop("old_password")

        new_password = d.pop("new_password")

        confirm_new_password = d.pop("confirm_new_password")

        change_password = cls(
            old_password=old_password,
            new_password=new_password,
            confirm_new_password=confirm_new_password,
        )

        change_password.additional_properties = d
        return change_password

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
