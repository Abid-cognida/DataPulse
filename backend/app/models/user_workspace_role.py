"""UserWorkspaceRole model module."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.core.enums import UserRole
from app.models.base import BaseModel


class UserWorkspaceRole(BaseModel):
    """User-Workspace-Role relationship model.

    Represents the many-to-many relationship between users and workspaces with roles.
    """

    user_id = Column(String(36), ForeignKey("user.id"), nullable=False)
    workspace_id = Column(String(36), ForeignKey("workspace.id"), nullable=False)
    role = Column(String(50), nullable=False, default=UserRole.VIEWER.value)

    # Relationships
    user = relationship("User", back_populates="workspaces")
    workspace = relationship("Workspace", back_populates="users")
