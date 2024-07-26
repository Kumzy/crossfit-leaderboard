
from typing import Any

from litestar import Controller, Request, get
from litestar_vite.inertia import share
from msgspec import Struct


class Message(Struct):
    message: str


class WebController(Controller):
    """Web Controller."""

    include_in_schema = False
    opt = {"exclude_from_auth": True}

    @get(
        component="Home",
        path="/",
        name="home",
    )
    async def home(self, path: str | None = None) -> Message:
        """Serve site root."""
        return Message("Welcome back.")

    @get(
        component="Dashboard",
        path="/dashboard",
        name="dashboard",
        include_in_schema=False,
    )
    async def dashboard(self, path: str | None = None) -> Message:
        """Serve site root."""
        return Message("Welcome back.")

    @get(
        component="Leaderboard",
        path="/leaderboard",
        name="leaderboard",
        include_in_schema=False,
    )
    async def leaderboard(self, request: Request[Any, Any, Any]) -> dict[str, Any]:
        """Serve leaderboard page."""
        share(request,"auth", {"user": "nobody"})
        return {"thing": "value"}
