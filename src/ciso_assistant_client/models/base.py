"""Pydantic models for the CISO Assistant API."""

from datetime import datetime

from pydantic import BaseModel, Field

__author__ = "lundberg"


class ApiToken(BaseModel):
    """API Token for authentication."""

    token: str = Field(..., description="API token value")


class BasePagedRead(BaseModel):
    """Paginated list response."""

    count: int = Field(..., description="Total count of items")
    next: str | None = Field(None, description="Next page URL")
    previous: str | None = Field(None, description="Previous page URL")


class BaseDetail(BaseModel):
    id: str = Field(..., description="Item UUID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Update timestamp")
    name: str = Field(..., max_length=200, description="Item name")
    description: str | None = Field(None, description="Item description")


class BaseWrite(BaseModel):
    name: str = Field(..., max_length=200, description="Item name")
    description: str | None = Field(None, description="Item description")
    is_published: bool = Field(default=False, description="Published status")
