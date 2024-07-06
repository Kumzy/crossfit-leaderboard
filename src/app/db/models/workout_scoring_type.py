from __future__ import annotations

from enum import Enum


class WorkoutScoringTypes(str, Enum):
    """Valid Values for Workout scorint types."""

    TIME = "TIME"
    WEIGHT = "WEIGHT"
    REPETITIONS = "REPETITIONS"
