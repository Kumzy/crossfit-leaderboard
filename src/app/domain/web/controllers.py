
from litestar import Controller, Request, get
from litestar.connection.base import AuthT, StateT, UserT
from litestar.plugins.flash import flash  # pyright: ignore[reportUnknownVariableType]
from msgspec import Struct


class Message(Struct):
    message: str


class WebController(Controller):
    """Web Controller."""

    include_in_schema = False
    opt = {"exclude_from_auth": True}

    @get("/", component="Home")
    async def index(self, request: Request[UserT, AuthT, StateT]) -> Message:
        """Serve site root."""
        flash(request, "Oh no! I've been flashed!", category="error")
        return Message(message="welcome")

    @get("/dashboard", component="Dashboard")
    async def dashboard(self, request: Request[UserT, AuthT, StateT]) -> Message:
        """Serve site root."""
        flash(request, "Oh no! I've been flashed!", category="error")
        return Message(message="dashboard details")
