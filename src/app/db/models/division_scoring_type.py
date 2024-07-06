from __future__ import annotations

from enum import Enum


class DivisionScoringType(str, Enum):
    """Valid Values for Division scoring types."""

    RANK = "RANK"
    POINT = "POINT"
