from __future__ import annotations

from typing import Any

import click

from app.db.utils import load_external_data


@click.group(name="manage", invoke_without_command=False, help="Manage application data.")
@click.pass_context
def data_management_app(_: dict[str, Any]) -> None:
    """Manage application data."""


@data_management_app.command(name="sync-data-from-source", help="Sync data from source")
def synchronize_data(
) -> None:
    """Synchronise data."""
    import anyio

    anyio.run(load_external_data)
