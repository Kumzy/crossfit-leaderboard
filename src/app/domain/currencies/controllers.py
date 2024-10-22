from __future__ import annotations

from litestar import Controller
from litestar.di import Provide

from app.domain.currencies.dependencies import provide_currencies_service
from app.domain.currencies.services import CurrencyService


class CurrencyController(Controller):
    """Handles the interactions within the Currency objects."""

    dependencies = {"currencies_service": Provide(provide_currencies_service)}
    signature_namespace = {"CurrencyService": CurrencyService}
    tags = ["Currencies"]
