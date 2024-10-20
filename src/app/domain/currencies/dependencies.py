from __future__ import annotations

from typing import TYPE_CHECKING

from app.domain.currencies.services import CurrencyService

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_currencies_service(
    db_session: AsyncSession | None = None,
) -> AsyncGenerator[CurrencyService, None]:
    """Provide Currency service.

    Args:
        db_session (AsyncSession | None, optional): current database session. Defaults to None.

    Returns:
        CurrencyService: A Currencies service object
    """
    async with CurrencyService.new(
        session=db_session,
    ) as service:
        yield service
