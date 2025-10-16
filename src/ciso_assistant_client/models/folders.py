from pydantic import BaseModel, Field

from ciso_assistant_client.models.base import BaseDetail, BasePagedRead

__author__ = "lundberg"


class ParentFolder(BaseModel):
    """Parent folder schema."""

    name: str = Field(..., description="Parent folder name", alias="str")
    id: str = Field(..., description="Parent folder UUID")


class FolderRead(BaseDetail):
    """Folder read schema."""

    parent_folder: ParentFolder | None = Field(None, description="Parent folder")
    content_type: str = Field(..., description="Content type")
    is_published: bool = Field(default=False, description="Published status")
    builtin: bool = Field(default=False, description="Built-in folder")


class PagedFolderRead(BasePagedRead):
    """Paginated folder list response."""

    results: list[FolderRead] = Field(..., description="List of folders")


class FolderWrite(BaseModel):
    """Folder write schema for creating/updating folders."""

    name: str = Field(..., max_length=200, description="Folder name")
    description: str | None = Field(None, description="Folder description")
    parent_folder: ParentFolder | None = Field(None, description="Parent folder")
    is_published: bool = Field(default=False, description="Published status")
