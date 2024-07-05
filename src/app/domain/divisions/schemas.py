from __future__ import annotations

from uuid import UUID  # noqa: TCH003

import msgspec

from app.lib.schema import CamelizedBaseStruct

__all__ = (
    "Division",
    "DivisionCreate",
    "DivisionUpdate",
)


class Division(CamelizedBaseStruct):
    """Competition properties to use for a response."""

    id: UUID
    name: str | None = None
    description: str | None = None


class DivisionCreate(CamelizedBaseStruct):
    name: str
    description: str | None = None


class DivisionUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | None | msgspec.UnsetType = msgspec.UNSET
    description: str | None | msgspec.UnsetType = msgspec.UNSET
