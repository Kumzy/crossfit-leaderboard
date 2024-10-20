from __future__ import annotations

from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import Currency


class CurrencyRepository(SQLAlchemyAsyncRepository[Currency]):
    """Currency Repository."""

    model_type = Currency
