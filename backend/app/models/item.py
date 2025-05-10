"""Item model module."""

from sqlalchemy import Boolean, Column, String, Text

from app.models.base import BaseModel


class Item(BaseModel):
    """Item model."""

    name = Column(String(255), index=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean(), default=True)
