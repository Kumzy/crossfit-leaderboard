from __future__ import annotations

from typing import TYPE_CHECKING, Any

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from app.config import constants
from app.db.models import Division, User
from app.lib import crypt

from .repositories import DivisionRepository

if TYPE_CHECKING:
    from collections.abc import Iterable

    from advanced_alchemy.repository._util import LoadSpec
    from sqlalchemy.orm import InstrumentedAttribute


class DivisionService(SQLAlchemyAsyncRepositoryService[Division]):
    """Handles database operations for divisions."""

    repository_type = DivisionRepository
    default_role = constants.DEFAULT_USER_ROLE

    def __init__(self, **repo_kwargs: Any) -> None:
        self.repository: DivisionRepository = self.repository_type(**repo_kwargs)
        self.model_type = self.repository.model_type

    async def create(
        self,
        data: Division | dict[str, Any],
        auto_commit: bool | None = None,
        auto_expunge: bool | None = None,
        auto_refresh: bool | None = None,
        load: LoadSpec | None = None,
        execution_options: dict[str, Any] | None = None,
    ) -> Division:
        """Create a new Competition."""
        if isinstance(data, dict):
            data = await self.to_model(data, "create")
        return await super().create(
            data=data,
            auto_commit=auto_commit,
            auto_expunge=auto_expunge,
            auto_refresh=auto_refresh,
            load=load,
            execution_options=execution_options,
        )

    async def update(
        self,
        data: Division | dict[str, Any],
        item_id: Any | None = None,
        attribute_names: Iterable[str] | None = None,
        with_for_update: bool | None = None,
        auto_commit: bool | None = None,
        auto_expunge: bool | None = None,
        auto_refresh: bool | None = None,
        id_attribute: str | InstrumentedAttribute | None = None,
        load: LoadSpec | None = None,
        execution_options: dict[str, Any] | None = None,
    ) -> Division:
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

    async def to_model(self, data: User | dict[str, Any], operation: str | None = None) -> User:
        if isinstance(data, dict) and "password" in data:
            password: bytes | str | None = data.pop("password", None)
            if password is not None:
                data.update({"hashed_password": await crypt.get_password_hash(password)})
        return await super().to_model(data, operation)
