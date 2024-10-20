from __future__ import annotations

from uuid import UUID  # noqa: TCH003

from app.lib.schema import CamelizedBaseStruct

__all__ = (
    "Currency",
)


class Currency(CamelizedBaseStruct):
    """Currency properties to use for a response."""

    id: UUID
    code: str | None = None
    name: str | None = None
