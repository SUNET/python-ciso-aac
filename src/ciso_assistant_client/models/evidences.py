__author__ = "lundberg"

from pydantic import Field

from ciso_assistant_client.models.base import BaseDetail, BasePagedRead, BaseWrite
from ciso_assistant_client.models.folders import ParentFolder


class EvidenceRead(BaseDetail):
    """Evidence read schema."""

    attachment: str | None = Field(None, description="Attachment URL or path")
    size: str | None = Field(None, description="Attachment size")
    folder: str | ParentFolder = Field(..., description="Folder UUID or object")
    applied_controls: list[str] = Field(default_factory=list, description="Applied control UUIDs")
    requirement_assessments: list[str] = Field(default_factory=list, description="Requirement assessment UUIDs")
    link: str | None = Field(None, max_length=2048, description="Link to evidence")
    is_published: bool = Field(default=False, description="Published status")


class PagedEvidenceRead(BasePagedRead):
    """Paginated evidence list response."""

    results: list[EvidenceRead] = Field(..., description="List of evidences")


class EvidenceWrite(BaseWrite):
    """Evidence write schema for creating/updating evidences."""

    attachment: str | None = Field(None, description="Attachment URL or path")
    link: str | None = Field(None, max_length=2048, description="Link to evidence")
    folder: str = Field(..., description="Folder UUID")
    applied_controls: list[str] = Field(default_factory=list, description="Applied control UUIDs")
    requirement_assessments: list[str] = Field(default_factory=list, description="Requirement assessment UUIDs")
