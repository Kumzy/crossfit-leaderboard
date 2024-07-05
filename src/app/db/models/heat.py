from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column

if TYPE_CHECKING:
    from datetime import datetime


class Heat(UUIDAuditBase):
    """A heat class."""

    __tablename__ = "heat"
    __pii_columns__ = {"name"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    date_start: Mapped[datetime | None] = mapped_column(nullable=True, default=None)
