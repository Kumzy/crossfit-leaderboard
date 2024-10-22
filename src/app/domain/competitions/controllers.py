"""Competition Controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Any

from litestar import Controller, Request, Response, delete, get, patch, post
from litestar.di import Provide
from litestar.params import Dependency, Parameter

from app.domain.accounts.guards import requires_superuser
from app.domain.competitions import urls
from app.domain.competitions.dependencies import provide_competitions_service
from app.domain.competitions.schemas import Competition, CompetitionCreate, CompetitionUpdate
from app.domain.competitions.services import CompetitionService

if TYPE_CHECKING:
    from uuid import UUID

    from advanced_alchemy.filters import FilterTypes
    from advanced_alchemy.service import OffsetPagination


class CompetitionController(Controller):
    """Competition Controller."""

    tags = ["Competitions"]
    dependencies = {"competitions_service": Provide(provide_competitions_service)}
    signature_namespace = {"CompetitionService": CompetitionService}
    dto = None
    return_dto = None

    @get(
        component="competition/list",
        operation_id="ListCompetitions",
        name="competitions.list",
        summary="List Competitions",
        description="Retrieve the competitions.",
        path=urls.COMPETITION_LIST,
        cache=0,
    )
    async def list_competitions(
        self,
        competitions_service: CompetitionService,
        filters: Annotated[list[FilterTypes], Dependency(skip_validation=True)],
    ) -> OffsetPagination[Competition]:
        """List competitions."""
        results, total = await competitions_service.list_and_count(*filters)
        return competitions_service.to_schema(data=results, total=total, schema_type=Competition, filters=filters)

    @get(
        operation_id="GetCompetition",
        name="competitions.get",
        path=urls.COMPETITION_DETAIL,
        summary="Retrieve the details of a competition.",
    )
    async def get_competition(
        self,
        competitions_service: CompetitionService,
        competition_id: Annotated[
            UUID,
            Parameter(
                title="Competition ID",
                description="The competition to retrieve.",
            ),
        ],
    ) -> Competition:
        """Get a competition."""
        db_obj = await competitions_service.get(competition_id)
        return competitions_service.to_schema(db_obj, schema_type=Competition)

    @get(
        operation_id="GetCompetitionBySlug",
        name="competitions.get-by-slug",
        path=urls.COMPETITION_DETAIL_SLUG,
        summary="Retrieve the details of a competition from a slug.",
    )
    async def get_competition_by_slug(
            self,
            competitions_service: CompetitionService,
            competition_slug: Annotated[
                str,
                Parameter(
                    title="Competition Slug",
                    description="The competition to retrieve.",
                ),
            ],
    ) -> Competition:
        """Get a competition."""
        db_obj = await competitions_service.get(item_id=competition_slug, id_attribute="slug")
        return competitions_service.to_schema(db_obj, schema_type=Competition)

    @post(
        operation_id="CreateCompetition",
        name="competitions:create",
        summary="Create a new competition.",
        cache_control=None,
        guards=[requires_superuser],
        path=urls.COMPETITION_CREATE,
    )
    async def create_competition(
        self,
        competitions_service: CompetitionService,
        data: CompetitionCreate,
    ) -> Competition:
        """Create a new user."""
        db_obj = await competitions_service.create(data.to_dict())
        return competitions_service.to_schema(db_obj, schema_type=Competition)

    @patch(
        operation_id="UpdateCompetition",
        name="competitions:update",
        path=urls.COMPETITION_UPDATE,
    )
    async def update_competition(
        self,
        data: CompetitionUpdate,
        competitions_service: CompetitionService,
        competition_id: UUID = Parameter(
            title="Competition ID",
            description="The competition to update.",
        ),
    ) -> Competition:
        """Update a competition."""
        db_obj = await competitions_service.update(item_id=competition_id, data=data.to_dict())
        return competitions_service.to_schema(db_obj, schema_type=Competition)

    @delete(
        operation_id="DeleteCompetition",
        name="competitions:delete",
        path=urls.COMPETITION_DELETE,
        summary="Remove a competition",
        description="Removes a competition and all associated data from the system.",
    )
    async def delete_competition(
        self,
        competitions_service: CompetitionService,
        competition_id: Annotated[
            UUID,
            Parameter(
                title="Competition ID",
                description="The competition to delete.",
            ),
        ],
    ) -> None:
        """Delete a competition from the system."""
        _ = await competitions_service.delete(competition_id)

    @get(
        component="competition/CompetitionCreate",
        name="web:competitions:create",
        path="/competitions/create",
        cache=False,
        exclude_from_auth=False,
        include_in_schema=False,
    )
    async def show_create_competition(
            self,
            request: Request,
    ) -> Response[Any] | dict[str, str]:
        """Show the competition creation page."""
        return {}
