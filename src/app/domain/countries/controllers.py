from __future__ import annotations

from litestar import Controller
from litestar.di import Provide

from app.domain.countries.dependencies import provide_countries_service
from app.domain.countries.services import CountryService


class CountryController(Controller):
    """Handles the interactions within the Country objects."""

    dependencies = {"currencies_service": Provide(provide_countries_service)}
    signature_namespace = {"CountryService": CountryService}
    tags = ["Countries"]
