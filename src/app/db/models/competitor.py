from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from datetime import date

    from .team_member import TeamMember


class Competitor(UUIDAuditBase, SlugKey):
    """A competitor class to register athletes"""

    __tablename__ = "competitor"
    __pii_columns__ = {"firstname", "lastname"}

    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    firstname: Mapped[str | None] = mapped_column(nullable=True, default=None)
    lastname: Mapped[str | None] = mapped_column(nullable=True, default=None)
    age: Mapped[int | None] = mapped_column(nullable=True, default=None)
    weight: Mapped[int | None] = mapped_column(nullable=True, default=None)
    height: Mapped[int | None] = mapped_column(nullable=True, default=None)
    affiliate: Mapped[str | None] = mapped_column(nullable=True, default=None)
    avatar_url: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    verified_at: Mapped[date] = mapped_column(nullable=True, default=None)
    # -----------
    # ORM Relationships
    # ------------
    teams: Mapped[list[TeamMember]] = relationship(
        back_populates="user",
        lazy="selectin",
        uselist=True,
        cascade="all, delete",
        viewonly=True,
    )
