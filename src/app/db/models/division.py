from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .division_scoring_type import DivisionScoringType

if TYPE_CHECKING:
    from .competition import Competition
    from .workout import Workout


class Division(UUIDAuditBase, SlugKey):
    """A division class."""

    __tablename__ = "division"
    __pii_columns__ = {"name", "description"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    competition_id: Mapped[UUID] = mapped_column(ForeignKey("competition.id", ondelete="cascade"), nullable=False)
    is_team: Mapped[bool] = mapped_column(default=False, nullable=False)
    team_size: Mapped[int | None] = mapped_column(nullable=True)
    # -----------
    # ORM Relationships
    # ------------
    division_scoring_type: Mapped[DivisionScoringType] = mapped_column(
        String(length=50),
        default=DivisionScoringType.RANK,
        nullable=False,
        index=True,
    )
    competition: Mapped[Competition] = relationship(
        back_populates="divisions",
        foreign_keys="Division.competition_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    workouts: Mapped[list[Workout]] = relationship(
        back_populates="division",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
