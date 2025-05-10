"""Workspace schema module."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WorkspaceBase(BaseModel):
    """Base schema for Workspace."""

    name: str = Field(..., description="Name of the workspace")
    description: Optional[str] = Field(None, description="Description of the workspace")
    is_active: bool = Field(True, description="Whether the workspace is active")


class WorkspaceCreate(WorkspaceBase):
    """Schema for creating a Workspace."""

    pass


class WorkspaceResponse(WorkspaceBase):
    """Schema for Workspace response."""

    id: str = Field(..., description="Unique identifier")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    class Config:
        """Pydantic config."""

        from_attributes = True
