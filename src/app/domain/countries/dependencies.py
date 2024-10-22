from __future__ import annotations

from typing import TYPE_CHECKING

from app.domain.countries.services import CountryService

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_countries_service(
    db_session: AsyncSession | None = None,
) -> AsyncGenerator[CountryService, None]:
    """Provide Country service.

    Args:
        db_session (AsyncSession | None, optional): current database session. Defaults to None.

    Returns:
        CountryService: A Countries service object
    """
    async with CountryService.new(
        session=db_session,
    ) as service:
        yield service
