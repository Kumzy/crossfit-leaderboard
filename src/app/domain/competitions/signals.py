from __future__ import annotations

from typing import TYPE_CHECKING

import structlog
from litestar.events import listener

from app.config.app import alchemy

from .dependencies import provide_competitions_service

if TYPE_CHECKING:
    from uuid import UUID

logger = structlog.get_logger()


@listener("competition_created")
async def competition_created_event_handler(
    competition_id: UUID,
) -> None:
    """Executes when a new competition is created.

    Args:
        competition_id: The primary key of the user that was created.
    """
    await logger.ainfo("Running post comptition creation flow.")
    async with alchemy.get_session() as db_session:
        service = await anext(provide_competitions_service(db_session))
        obj = await service.get_one_or_none(id=competition_id)
        if obj is None:
            await logger.aerror("Could not locate the specified competition", id=competition_id)
        else:
            await logger.ainfo("Found competition", **obj.to_dict(exclude={"hashed_password"}))
