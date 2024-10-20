"""User Account Controllers."""

from __future__ import annotations

from typing import Any

from advanced_alchemy.utils.text import slugify
from litestar import Controller, Request, Response, get, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.plugins.flash import flash
from litestar_vite.inertia import InertiaRedirect

from app.db.models import User as UserModel  # noqa: TCH001
from app.domain.accounts import urls
from app.domain.accounts.dependencies import provide_roles_service, provide_users_service
from app.domain.accounts.guards import requires_active_user
from app.domain.accounts.schemas import AccountLogin, AccountRegister, User
from app.domain.accounts.services import RoleService, UserService


class AccessController(Controller):
    """User login and registration."""

    tags = ["Access"]
    dependencies = {"users_service": Provide(provide_users_service), "roles_service": Provide(provide_roles_service)}
    signature_namespace = {
        "UserService": UserService,
        "RoleService": RoleService,
        "RequestEncodingType": RequestEncodingType,
        "Body": Body,
        "User": User,
    }

    @post(
        name="account:logout",
        path=urls.ACCOUNT_LOGOUT,
        exclude_from_auth=False,
        cache=False,
        summary="Logout",
    )
    async def logout(
            self,
            request: Request,
    ) -> Response | InertiaRedirect:
        """Account Logout"""
        flash(request, "You have been logged out.", category="info")
        request.clear_session()
        return InertiaRedirect(request, request.url_for("login"))

    @post(
        operation_id="AccountRegister",
        name="account:register",
        path=urls.ACCOUNT_REGISTER,
        cache=False,
        summary="Create User",
        description="Register a new account.",
    )
    async def signup(
        self,
        request: Request,
        users_service: UserService,
        roles_service: RoleService,
        data: AccountRegister,
    ) -> User:
        """User Signup."""
        user_data = data.to_dict()
        role_obj = await roles_service.get_one_or_none(slug=slugify(users_service.default_role))
        if role_obj is not None:
            user_data.update({"role_id": role_obj.id})
        user = await users_service.create(user_data)
        request.app.emit(event_id="user_created", user_id=user.id)
        return users_service.to_schema(user, schema_type=User)

    @get(
        operation_id="AccountProfile",
        name="account:profile",
        path=urls.ACCOUNT_PROFILE,
        guards=[requires_active_user],
        summary="User Profile",
        description="User profile information.",
    )
    async def profile(self, request: Request, current_user: UserModel, users_service: UserService) -> User:
        """User Profile."""
        return users_service.to_schema(current_user, schema_type=User)

    # @sentry_sdk.trace
    @get(
        component="auth/login",
        name="login",
        path="/login",
        cache=False,
        exclude_from_auth=True,
        include_in_schema=False,
    )
    async def show_login(
            self,
            request: Request,
    ) -> Response | dict | InertiaRedirect:
        """Show the user login page."""
        if request.session.get("user_id", False):
            flash(request, "Your account is already authenticated.  Welcome back!", category="info")
            return InertiaRedirect(request, request.url_for("dashboard"))
        return {}

    # @sentry_sdk.trace
    @post(component="auth/login", name="login.store", path="/login")
    async def login(
            self,
            request: Request[Any, Any, Any],
            users_service: UserService,
            data: AccountLogin,
    ) -> Response | InertiaRedirect:
        """Authenticate a user."""
        user = await users_service.authenticate(data.username, data.password)
        request.set_session({"user_id": user.email})
        flash(request, "Your account was successfully authenticated.", category="info")
        request.logger.info("Redirecting to %s ", request.url_for("dashboard"))
        return InertiaRedirect(request, request.url_for("dashboard"))
