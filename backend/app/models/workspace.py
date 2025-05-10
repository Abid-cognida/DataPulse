"""Workspace model module."""

from sqlalchemy import Boolean, Column, String, Text
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Workspace(BaseModel):
    """Workspace model."""

    name = Column(String(255), index=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean(), default=True)

    # Relationships
    users = relationship(
        "UserWorkspaceRole", back_populates="workspace", cascade="all, delete-orphan"
    )
