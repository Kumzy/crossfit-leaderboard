"""Competition Controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.exceptions import NotFoundException
from litestar.params import Dependency, Parameter

from app.domain.accounts.guards import requires_superuser
from app.domain.divisions import urls
from app.domain.divisions.dependencies import provide_divisions_service
from app.domain.divisions.schemas import Division, DivisionCreate, DivisionUpdate
from app.domain.divisions.services import DivisionService

if TYPE_CHECKING:
    from uuid import UUID

    from advanced_alchemy.filters import FilterTypes
    from advanced_alchemy.service import OffsetPagination


class DivisionController(Controller):
    """Division Controller."""

    tags = ["Divisions"]
    dependencies = {"divisions_service": Provide(provide_divisions_service)}
    signature_namespace = {"DivisionService": DivisionService}
    dto = None
    return_dto = None

    @get(
        operation_id="ListDivisions",
        name="divisions:list",
        summary="List Divisions",
        description="Retrieve the divisions of a competition.",
        path=urls.DIVISION_LIST,
        cache=60,
    )
    async def list_divisions(
        self,
        divisions_service: DivisionService,
        competition_id: Annotated[
            UUID,
            Parameter(
                title="Competition ID",
                description="The competition that the division belongs to.",
            ),
        ],
        filters: Annotated[list[FilterTypes], Dependency(skip_validation=True)],
    ) -> OffsetPagination[Division]:
        """List competitions."""
        results, total = await divisions_service.list_and_count(*filters, competition_id=competition_id)
        return divisions_service.to_schema(data=results, total=total, schema_type=Division, filters=filters)

    @get(
        operation_id="GetDivision",
        name="divisions:get",
        path=urls.DIVISION_DETAIL,
        summary="Retrieve the details of a division.",
    )
    async def get_division(
        self,
        divisions_service: DivisionService,
        competition_id: Annotated[
            UUID,
            Parameter(
                title="Competition ID",
                description="The competition to retrieve.",
            ),
        ],
        division_id: Annotated[
            UUID,
            Parameter(
                title="Division ID",
                description="The division id.",
            ),
        ],
    ) -> Division:
        """Get a division."""
        db_obj = await divisions_service.get_one(division_id=division_id, competition_id=competition_id)
        if db_obj.competition is None or db_obj.competition.id != competition_id:
            msg = "Division not found"
            raise NotFoundException(msg)
        return divisions_service.to_schema(db_obj, schema_type=Division)

    @post(
        operation_id="CreateDivision",
        name="divisions:create",
        summary="Create a new division.",
        cache_control=None,
        guards=[requires_superuser],
        path=urls.DIVISION_CREATE,
    )
    async def create_division(
        self,
        divisions_service: DivisionService,
        data: DivisionCreate,
    ) -> Division:
        """Create a new division."""
        db_obj = await divisions_service.create(data.to_dict())
        return divisions_service.to_schema(db_obj, schema_type=Division)

    @patch(
        operation_id="UpdateDivision",
        name="divisions:update",
        path=urls.DIVISION_UPDATE,
    )
    async def update_division(
        self,
        data: DivisionUpdate,
        divisions_service: DivisionService,
        competition_id: Annotated[
            UUID,
            Parameter(
                title="Competition ID",
                description="The competition to retrieve.",
            ),
        ],
        division_id: UUID = Parameter(
            title="Competition ID",
            description="The competition to update.",
        ),
    ) -> Division:
        """Update a division."""
        db_obj = await divisions_service.update(item_id=division_id, data=data.to_dict())
        if db_obj.competition is None or db_obj.competition.id != competition_id:
            msg = "Division not found"
            raise NotFoundException(msg)

        return divisions_service.to_schema(db_obj, schema_type=Division)

    @delete(
        operation_id="DeleteDivision",
        name="divisions:delete",
        path=urls.DIVISION_DELETE,
        summary="Remove a division",
        description="Removes a division and all associated data from the system.",
    )
    async def delete_competition(
        self,
        divisions_service: DivisionService,
        division_id: Annotated[
            UUID,
            Parameter(
                title="Division ID",
                description="The division to delete.",
            ),
        ],
    ) -> None:
        """Delete a division from the system."""
        _ = await divisions_service.delete(division_id)
