"""Item schema module."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Base schema for Item."""

    name: str = Field(..., description="Name of the item")
    description: Optional[str] = Field(None, description="Description of the item")


class ItemCreate(ItemBase):
    """Schema for creating an Item."""

    pass


class ItemResponse(ItemBase):
    """Schema for Item response."""

    id: str = Field(..., description="Unique identifier")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    is_active: bool = Field(..., description="Whether the item is active")

    class Config:
        """Pydantic config."""

        from_attributes = True
