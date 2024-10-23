from __future__ import annotations


async def load_external_data() -> None:
    """Import/Synchronize Database Fixtures."""

    from pathlib import Path

    from advanced_alchemy.utils.fixtures import open_fixture_async
    from sqlalchemy import select
    from sqlalchemy.orm import load_only
    from structlog import get_logger

    from app.config import get_settings
    from app.config.app import alchemy
    from app.db.models import Country, Currency
    from app.domain.countries.services import CountryService
    from app.domain.currencies.services import CurrencyService

    settings = get_settings()
    logger = get_logger()
    fixtures_path = Path(settings.db.FIXTURE_PATH)
    """Add currencies"""
    async with CurrencyService.new(
        statement=select(Currency).options(load_only(Currency.id, Currency.code, Currency.name)),
        config=alchemy,
    ) as service:
        fixture_data = await open_fixture_async(fixtures_path, "currency")
        await service.upsert_many(match_fields=["code"], data=fixture_data, auto_commit=True)
        await logger.ainfo("Currencies updated")
    """Add countries"""
    async with CountryService.new(
            statement=select(Country).options(load_only(Country.id, Country.code, Country.name)),
            config=alchemy,
    ) as service:
        fixture_data = await open_fixture_async(fixtures_path, "country")
        await service.upsert_many(match_fields=["code"], data=fixture_data, auto_commit=True)
        await logger.ainfo("Countries updated")
