from __future__ import annotations

from advanced_alchemy.base import UUIDBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Country(UUIDBase):
    """A country class."""

    __tablename__ = "country"
    __pii_columns__ = {"name"}
    name: Mapped[str] = mapped_column(nullable=False, index=False)
    code: Mapped[str] = mapped_column(String(length=3), unique=True, nullable=False, index=False)
