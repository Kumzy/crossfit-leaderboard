from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import TYPE_CHECKING

from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .competition_status import CompetitionStatus

if TYPE_CHECKING:
    from .division import Division


class Competition(UUIDAuditBase, SlugKey):
    """A competition class."""

    __tablename__ = "competition"
    __pii_columns__ = {"name", "description"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    date_start: Mapped[datetime | None] = mapped_column(nullable=False, default=None)
    date_end: Mapped[datetime | None] = mapped_column(nullable=False, default=None)
    registration_date_start: Mapped[datetime | None] = mapped_column(nullable=False, default=None)
    registration_date_end: Mapped[datetime | None] = mapped_column(nullable=False, default=None)

    # -----------
    # ORM Relationships
    # ------------
    divisions: Mapped[list[Division]] = relationship(
        back_populates="competition",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    competition_status: Mapped[CompetitionStatus] = mapped_column(
        String(length=50),
        default=CompetitionStatus.DRAFT,
        nullable=False,
        index=True,
    )
