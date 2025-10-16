from pydantic import Field

from ciso_assistant_client.models.base import BaseDetail, BasePagedRead, BaseWrite

__author__ = "lundberg"


class AssetRead(BaseDetail):
    """Asset read schema."""

    folder: str = Field(..., description="Folder UUID")
    parent_assets: list[str] = Field(default_factory=list, description="Parent asset UUIDs")
    children_assets: list[str] = Field(default_factory=list, description="Children asset UUIDs")
    owner: list[str] = Field(default_factory=list, description="Owner UUIDs")
    filtering_labels: list[str] = Field(default_factory=list, description="Filtering label UUIDs")
    type: str = Field(..., description="Asset type")
    security_exceptions: list[str] = Field(default_factory=list, description="Security exception UUIDs")
    business_value: str = Field(..., max_length=200, description="Business value")
    reference_link: str | None = Field(None, description="External reference link")


class PagedAssetRead(BasePagedRead):
    """Paginated asset list response."""

    results: list[AssetRead] = Field(..., description="List of assets")


class AssetWrite(BaseWrite):
    """Asset write schema for creating/updating assets."""

    business_value: str = Field(..., max_length=200, description="Business value")
    type: str = Field(..., description="Asset type")
    folder: str = Field(..., description="Folder UUID")
    parent_assets: list[str] = Field(default_factory=list, description="Parent asset UUIDs")
    reference_link: str | None = Field(None, max_length=2048, description="External reference link")
    filtering_labels: list[str] = Field(default_factory=list, description="Filtering label UUIDs")
