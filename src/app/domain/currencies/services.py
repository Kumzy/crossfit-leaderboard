from __future__ import annotations

from typing import Any

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from app.db.models import Currency

from .repositories import CurrencyRepository


class CurrencyService(SQLAlchemyAsyncRepositoryService[Currency]):
    """Handles basic lookup operations for a Currency."""

    repository_type = CurrencyRepository
    match_fields = ["code"]

    def __init__(self, **repo_kwargs: Any) -> None:
        self.repository: CurrencyRepository = self.repository_type(**repo_kwargs)
        self.model_type = self.repository.model_type
