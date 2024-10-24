from __future__ import annotations

from typing import TYPE_CHECKING, Any

from advanced_alchemy.service import (
    ModelDictT,
    SQLAlchemyAsyncRepositoryService,
)

from app.config import constants
from app.db.models import Competition

from .repositories import CompetitionRepository

if TYPE_CHECKING:
    from collections.abc import Iterable

    from advanced_alchemy.repository._util import LoadSpec
    from sqlalchemy.orm import InstrumentedAttribute


class CompetitionService(SQLAlchemyAsyncRepositoryService[Competition]):
    """Handles database operations for users."""

    repository_type = CompetitionRepository
    default_role = constants.DEFAULT_USER_ROLE

    def __init__(self, **repo_kwargs: Any) -> None:
        self.repository: CompetitionRepository = self.repository_type(**repo_kwargs)
        self.model_type = self.repository.model_type

    async def create(
        self,
        data: ModelDictT[Competition],
        *,
        load: LoadSpec | None = None,
        execution_options: dict[str, Any] | None = None,
        auto_commit: bool | None = None,
        auto_expunge: bool | None = None,
        auto_refresh: bool | None = None,
    ) -> Competition:
        """Create a new Competition."""
        if isinstance(data, dict):
            data = await self.to_model(data, "create")
        return await super().create(
            data=data,
            load=load,
            execution_options=execution_options,
            auto_commit=auto_commit,
            auto_expunge=auto_expunge,
            auto_refresh=auto_refresh,
        )

    async def update(
        self,
        data: ModelDictT[Competition],
        item_id: Any | None = None,
        *,
        id_attribute: str | InstrumentedAttribute[Any] | None = None,
        load: LoadSpec | None = None,
        execution_options: dict[str, Any] | None = None,
        attribute_names: Iterable[str] | None = None,
        with_for_update: bool | None = None,
        auto_commit: bool | None = None,
        auto_expunge: bool | None = None,
        auto_refresh: bool | None = None,
    ) -> Competition:
        if isinstance(data, dict):
            data = await self.to_model(data, "update")
        return await super().update(
            data=data,
            item_id=item_id,
            attribute_names=attribute_names,
            with_for_update=with_for_update,
            auto_commit=auto_commit,
            auto_expunge=auto_expunge,
            auto_refresh=auto_refresh,
            id_attribute=id_attribute,
            load=load,
            execution_options=execution_options,
        )
