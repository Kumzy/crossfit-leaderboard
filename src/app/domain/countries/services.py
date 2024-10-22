from __future__ import annotations

from typing import Any

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from app.db.models import Country

from .repositories import CountryRepository


class CountryService(SQLAlchemyAsyncRepositoryService[Country]):
    """Handles basic lookup operations for a Country."""

    repository_type = CountryRepository
    match_fields = ["code"]

    def __init__(self, **repo_kwargs: Any) -> None:
        self.repository: CountryRepository = self.repository_type(**repo_kwargs)
        self.model_type = self.repository.model_type
