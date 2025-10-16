"""Pydantic models for the CISO Assistant API."""

from datetime import datetime

from pydantic import BaseModel, Field


class ApiToken(BaseModel):
    """API Token for authentication."""

    token: str = Field(..., description="API token value")


class ParentFolder(BaseModel):
    """Parent folder schema."""

    name: str = Field(..., description="Parent folder name", alias="str")
    id: str = Field(..., description="Parent folder UUID")


class FolderRead(BaseModel):
    """Folder read schema."""

    id: str = Field(..., description="Folder UUID")
    parent_folder: ParentFolder | None = Field(None, description="Parent folder")
    content_type: str = Field(..., description="Content type")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Update timestamp")
    is_published: bool = Field(default=False, description="Published status")
    name: str = Field(..., max_length=200, description="Folder name")
    description: str | None = Field(None, description="Folder description")
    builtin: bool = Field(default=False, description="Built-in folder")


class PagedFolderRead(BaseModel):
    """Paginated folder list response."""

    count: int = Field(..., description="Total count of folders")
    next: str | None = Field(None, description="Next page URL")
    previous: str | None = Field(None, description="Previous page URL")
    results: list[FolderRead] = Field(..., description="List of folders")


class FolderWrite(BaseModel):
    """Folder write schema for creating/updating folders."""

    name: str = Field(..., max_length=200, description="Folder name")
    description: str | None = Field(None, description="Folder description")
    parent_folder: ParentFolder | None = Field(None, description="Parent folder")
    is_published: bool = Field(default=False, description="Published status")


class AssetRead(BaseModel):
    """Asset read schema."""

    id: str = Field(..., description="Asset UUID")
    folder: str = Field(..., description="Folder UUID")
    parent_assets: list[str] = Field(default_factory=list, description="Parent asset UUIDs")
    children_assets: list[str] = Field(default_factory=list, description="Children asset UUIDs")
    owner: list[str] = Field(default_factory=list, description="Owner UUIDs")
    filtering_labels: list[str] = Field(default_factory=list, description="Filtering label UUIDs")
    type: str = Field(..., description="Asset type")
    security_exceptions: list[str] = Field(default_factory=list, description="Security exception UUIDs")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Update timestamp")
    name: str = Field(..., max_length=200, description="Asset name")
    description: str | None = Field(None, description="Asset description")
    business_value: str = Field(..., max_length=200, description="Business value")
    reference_link: str | None = Field(None, description="External reference link")


class PagedAssetRead(BaseModel):
    """Paginated asset list response."""

    count: int = Field(..., description="Total count of assets")
    next: str | None = Field(None, description="Next page URL")
    previous: str | None = Field(None, description="Previous page URL")
    results: list[AssetRead] = Field(..., description="List of assets")


class AssetWrite(BaseModel):
    """Asset write schema for creating/updating assets."""

    name: str = Field(..., max_length=200, description="Asset name")
    description: str | None = Field(None, description="Asset description")
    business_value: str = Field(..., max_length=200, description="Business value")
    type: str = Field(..., description="Asset type")
    folder: str = Field(..., description="Folder UUID")
    parent_assets: list[str] = Field(default_factory=list, description="Parent asset UUIDs")
    reference_link: str | None = Field(None, max_length=2048, description="External reference link")
    filtering_labels: list[str] = Field(default_factory=list, description="Filtering label UUIDs")
    is_published: bool = Field(default=False, description="Published status")


class EvidenceRead(BaseModel):
    """Evidence read schema."""

    id: str = Field(..., description="Evidence UUID")
    attachment: str = Field(..., description="Attachment URL or path")
    size: str = Field(..., description="Attachment size")
    folder: str = Field(..., description="Folder UUID")
    applied_controls: list[str] = Field(default_factory=list, description="Applied control UUIDs")
    requirement_assessments: list[str] = Field(default_factory=list, description="Requirement assessment UUIDs")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Update timestamp")
    name: str = Field(..., max_length=200, description="Evidence name")
    description: str | None = Field(None, description="Evidence description")
    link: str | None = Field(None, max_length=2048, description="Link to evidence")
    is_published: bool = Field(default=False, description="Published status")


class PagedEvidenceRead(BaseModel):
    """Paginated evidence list response."""

    count: int = Field(..., description="Total count of evidences")
    next: str | None = Field(None, description="Next page URL")
    previous: str | None = Field(None, description="Previous page URL")
    results: list[EvidenceRead] = Field(..., description="List of evidences")


class EvidenceWrite(BaseModel):
    """Evidence write schema for creating/updating evidences."""

    name: str = Field(..., max_length=200, description="Evidence name")
    description: str | None = Field(None, description="Evidence description")
    attachment: str | None = Field(None, description="Attachment URL or path")
    link: str | None = Field(None, max_length=2048, description="Link to evidence")
    folder: str = Field(..., description="Folder UUID")
    applied_controls: list[str] = Field(default_factory=list, description="Applied control UUIDs")
    requirement_assessments: list[str] = Field(default_factory=list, description="Requirement assessment UUIDs")
    is_published: bool = Field(default=False, description="Published status")
