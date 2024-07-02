from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from uuid import UUID  # noqa: TCH003

import msgspec

from app.db.models.division import Division
from app.lib.schema import CamelizedBaseStruct

__all__ = (
    "Competition",
    "CompetitionCreate",
    "CompetitionUpdate",
)


class Competition(CamelizedBaseStruct):
    """Competition properties to use for a response."""

    id: UUID
    name: str | None = None
    description: str = False
    divisions: list[Division] = []


class CompetitionCreate(CamelizedBaseStruct):
    name: str
    description: str | None = None
    date_start: datetime | None = None
    date_end: datetime | None = None


class CompetitionUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | None | msgspec.UnsetType = msgspec.UNSET
    description: str | None | msgspec.UnsetType = msgspec.UNSET
    date_start: datetime | None | msgspec.UnsetType = msgspec.UNSET
    date_end: datetime | None | msgspec.UnsetType = msgspec.UNSET
