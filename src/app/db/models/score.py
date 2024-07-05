from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .workout import Workout


class Score(UUIDAuditBase):
    """A score class."""

    __tablename__ = "score"
    __table_args__ = {
        "comment": "Manage scores and tiebreaks",
    }
    score: Mapped[int] = mapped_column(nullable=False, index=True)
    tiebreak: Mapped[int | None] = mapped_column(nullable=True, default=None)
    workout_id: Mapped[UUID] = mapped_column(ForeignKey("workout.id", ondelete="cascade"), nullable=False)
    time: Mapped[int | None] = mapped_column(nullable=True, default=None)
    # -----------
    # ORM Relationships
    # ------------
    workout: Mapped[Workout] = relationship(
        back_populates="score",
        foreign_keys="Workout.workout_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )

    @hybrid_property
    def time_minute(self) -> int | None:
        """Return minutes part of the time."""
        if self.time is not None and self.time > 0:
            return self.time // 60
        return None

    @hybrid_property
    def time_second(self) -> int | None:
        """Return seconds part of the time."""
        if self.time is not None and self.time > 0:
            return self.time % 60
        return None

    @hybrid_property
    def tiebreak_minute(self) -> int | None:
        """Return minutes part of the tiebreak."""
        if self.tiebreak is not None and self.tiebreak > 0:
            return self.tiebreak // 60
        return None

    @hybrid_property
    def tiebreak_second(self) -> int | None:
        """Return seconds part of the tiebreak."""
        if self.tiebreak is not None and self.tiebreak > 0:
            return self.tiebreak % 60
        return None
