from __future__ import annotations

from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import Competition


class CompetitionRepository(SQLAlchemyAsyncRepository[Competition]):
    """Competition SQLAlchemy Repository."""

    model_type = Competition
