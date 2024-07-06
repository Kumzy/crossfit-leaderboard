from __future__ import annotations

from uuid import UUID  # noqa: TCH003

import msgspec

from app.db.models.division_scoring_type import DivisionScoringType
from app.lib.schema import CamelizedBaseStruct

__all__ = (
    "Division",
    "DivisionCreate",
    "DivisionUpdate",
)


class Division(CamelizedBaseStruct):
    """Division properties to use for a response."""
    id: UUID
    name: str
    competition_id: UUID
    is_team: bool
    division_scoring_type: DivisionScoringType = DivisionScoringType.RANK
    team_size: int | None = None
    description: str | None = None


class DivisionCreate(CamelizedBaseStruct):
    """Division properties to use for a creation."""
    name: str
    competition_id: UUID
    division_scoring_type: DivisionScoringType = DivisionScoringType.RANK
    is_team: bool = False
    team_size: int | None = None
    description: str | None = None


class DivisionUpdate(CamelizedBaseStruct, omit_defaults=True):
    """Division properties to use for an update."""
    name: str | None | msgspec.UnsetType = msgspec.UNSET
    description: str | None | msgspec.UnsetType = msgspec.UNSET
    team_size: int | None | msgspec.UnsetType = msgspec.UNSET
