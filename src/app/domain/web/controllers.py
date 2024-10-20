
from typing import Any

from litestar import Controller, Request, get
from litestar.response import File
from litestar_vite.inertia import InertiaRedirect, share
from msgspec import Struct

from app.config import app as config


class Message(Struct):
    message: str


class WebController(Controller):
    """Web Controller."""

    include_in_schema = False

    @get(
        component="Home",
        path="/",
        name="home",
        exclude_from_auth=True,
    )
    async def home(self, request: Request) -> InertiaRedirect:
        """Serve site root."""
        if request.session.get("user_id", False):
            return InertiaRedirect(request, request.url_for("dashboard"))
        return InertiaRedirect(request, request.url_for("landing"))
        # return Message("Welcome back.")

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

    @get(path="/favicon.ico", name="favicon", exclude_from_auth=True, include_in_schema=False, sync_to_thread=False)
    def favicon(self) -> File:
        return File(path=f"{config.vite.public_dir}/favicon.ico")
