from __future__ import annotations

from enum import Enum


class CompetitionStatus(str, Enum):
    """Valid Values for competition statuses."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"
