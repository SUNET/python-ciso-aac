from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from ciso_assistant_client.models.base import BaseDetail, BasePagedRead, BaseWrite
from ciso_assistant_client.models.folders import ParentFolder

__author__ = "lundberg"


class AssetType(str, Enum):
    PRIMARY = "Primary"
    SUPPORT = "Support"
    PRIMARY_WRITE = "PR"
    SUPPORT_WRITE = "SP"


class Dependency(BaseModel):
    id: str = Field(..., description="Asset UUID")
    name: str = Field(..., description="Asset name", alias="str")


class AssetRead(BaseDetail):
    """Asset read schema."""

    folder: ParentFolder = Field(..., description="Folder UUID")
    path: list[ParentFolder] = Field(..., description="Folder paths")
    parent_assets: list[Dependency] = Field(default_factory=list, description="Parent asset UUIDs")
    children_assets: list[Dependency] = Field(default_factory=list, description="Children asset UUIDs")
    owner: list[str] = Field(default_factory=list, description="Owner UUIDs")
    filtering_labels: list[str] = Field(default_factory=list, description="Filtering label UUIDs")
    type: AssetType = Field(..., description="Asset type")
    security_exceptions: list[str] = Field(default_factory=list, description="Security exception UUIDs")
    reference_link: str | None = Field(None, description="External reference link")


class PagedAssetRead(BasePagedRead):
    """Paginated asset list response."""

    results: list[AssetRead] = Field(..., description="List of assets")


class AssetWrite(BaseWrite):
    """Asset write schema for creating/updating assets."""

    type: str = Field(..., description="Asset type")
    folder: str = Field(..., description="Folder UUID")
    parent_assets: list[str] = Field(default_factory=list, description="Parent asset UUIDs")
    reference_link: str | None = Field(default=None, max_length=2048, description="External reference link")
    filtering_labels: list[str] = Field(default_factory=list, description="Filtering label UUIDs")


class AssetWriteResponse(BaseWrite):
    id: str = Field(..., description="Asset UUID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Update timestamp")
    folder: str = Field(..., description="Folder UUID")
    parent_assets: list[str] = Field(default_factory=list, description="Parent asset UUIDs")
