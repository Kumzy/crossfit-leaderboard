from __future__ import annotations

from typing import Final

from advanced_alchemy.base import orm_registry
from sqlalchemy import Column, ForeignKey, Table

team_division: Final[Table] = Table(
    "team_division",
    orm_registry.metadata,
    Column("team_id", ForeignKey("team.id", ondelete="CASCADE"), primary_key=True),
    Column("division_id", ForeignKey("division.id", ondelete="CASCADE"), primary_key=True),
)
