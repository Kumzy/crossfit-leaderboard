# type: ignore
"""

Revision ID: f744cc1eae0e
Revises: 6f0b61e05385
Create Date: 2024-07-13 19:17:09.331745+00:00

"""
from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

import sqlalchemy as sa
from alembic import op
from advanced_alchemy.types import EncryptedString, EncryptedText, GUID, ORA_JSONB, DateTimeUTC
from sqlalchemy import Text  # noqa: F401
from sqlalchemy.dialects import postgresql
if TYPE_CHECKING:
    from collections.abc import Sequence

__all__ = ["downgrade", "upgrade", "schema_upgrades", "schema_downgrades", "data_upgrades", "data_downgrades"]

sa.GUID = GUID
sa.DateTimeUTC = DateTimeUTC
sa.ORA_JSONB = ORA_JSONB
sa.EncryptedString = EncryptedString
sa.EncryptedText = EncryptedText

# revision identifiers, used by Alembic.
revision = 'f744cc1eae0e'
down_revision = '6f0b61e05385'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        with op.get_context().autocommit_block():
            schema_upgrades()
            data_upgrades()

def downgrade() -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        with op.get_context().autocommit_block():
            data_downgrades()
            schema_downgrades()

def schema_upgrades() -> None:
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('competition', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registration_date_start', sa.DateTimeUTC(timezone=True), nullable=False))
        batch_op.add_column(sa.Column('registration_date_end', sa.DateTimeUTC(timezone=True), nullable=False))
        batch_op.add_column(sa.Column('competition_status', sa.String(length=50), nullable=False))
        batch_op.alter_column('date_start',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
        batch_op.alter_column('date_end',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
        batch_op.create_index(batch_op.f('ix_competition_competition_status'), ['competition_status'], unique=False)

    # ### end Alembic commands ###

def schema_downgrades() -> None:
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('competition', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_competition_competition_status'))
        batch_op.alter_column('date_end',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
        batch_op.alter_column('date_start',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
        batch_op.drop_column('competition_status')
        batch_op.drop_column('registration_date_end')
        batch_op.drop_column('registration_date_start')

    # ### end Alembic commands ###

def data_upgrades() -> None:
    """Add any optional data upgrade migrations here!"""

def data_downgrades() -> None:
    """Add any optional data downgrade migrations here!"""