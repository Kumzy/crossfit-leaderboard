from __future__ import annotations

from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import Division


class DivisionRepository(SQLAlchemyAsyncRepository[Division]):
    """Division SQLAlchemy Repository."""

    model_type = Division
