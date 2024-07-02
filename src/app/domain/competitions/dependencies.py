"""Competition Controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import selectinload

from app.db.models import Competition
from app.domain.competitions.services import CompetitionService

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_competitions_service(db_session: AsyncSession) -> AsyncGenerator[CompetitionService, None]:
    """Construct repository and service objects for the request."""
    async with CompetitionService.new(
        session=db_session,
        load=[
            selectinload(Competition.divisions),
        ],
    ) as service:
        yield service
