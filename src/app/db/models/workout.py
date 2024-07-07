from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .division import Division


class Workout(UUIDAuditBase):
    """A workout class."""

    __tablename__ = "workout"
    __pii_columns__ = {"name", "description"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    division_id: Mapped[UUID] = mapped_column(ForeignKey("division.id", ondelete="cascade"), nullable=False)
    # -----------
    # ORM Relationships
    # ------------
    division: Mapped[Division] = relationship(
        back_populates="workouts",
        foreign_keys="Workout.division_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
