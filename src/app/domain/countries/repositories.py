from __future__ import annotations

from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import Country


class CountryRepository(SQLAlchemyAsyncRepository[Country]):
    """Country Repository."""

    model_type = Country
