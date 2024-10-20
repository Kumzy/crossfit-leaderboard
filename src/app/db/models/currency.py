from __future__ import annotations

from advanced_alchemy.base import UUIDBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Currency(UUIDBase):
    """A currency class."""

    __tablename__ = "currency"
    code: Mapped[str] = mapped_column(String(length=3), index=False, nullable=False)
    name: Mapped[str] = mapped_column(index=False, nullable=False)
