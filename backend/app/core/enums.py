"""Enum definitions for the application."""

from enum import Enum, auto


class StrEnum(str, Enum):
    """String enum base class."""

    def _generate_next_value_(name, start, count, last_values):
        """Generate the next value for auto()."""
        return name.lower()

    def __str__(self) -> str:
        """Return the string value of the enum."""
        return self.value


class UserRole(StrEnum):
    """User role enum."""

    VIEWER = auto()
    EDITOR = auto()
