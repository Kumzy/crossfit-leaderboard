"""Division dependencies."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import selectinload

from app.domain.divisions.services import DivisionService

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_divisions_service(db_session: AsyncSession) -> AsyncGenerator[DivisionService, None]:
    """Construct repository and service objects for the request."""
    async with DivisionService.new(
        session=db_session,
        load=[
            # selectinload(Competition.divisions),
        ],
    ) as service:
        yield service
