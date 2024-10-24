# type: ignore
"""add competition and division

Revision ID: 945e69b87a72
Revises: a22cc7704d14
Create Date: 2024-07-02 12:09:25.715426+00:00

"""
from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

import sqlalchemy as sa
from alembic import op
from advanced_alchemy.types import EncryptedString, EncryptedText, GUID, ORA_JSONB, DateTimeUTC
from sqlalchemy import Text  # noqa: F401

if TYPE_CHECKING:
    from collections.abc import Sequence

__all__ = ["downgrade", "upgrade", "schema_upgrades", "schema_downgrades", "data_upgrades", "data_downgrades"]

sa.GUID = GUID
sa.DateTimeUTC = DateTimeUTC
sa.ORA_JSONB = ORA_JSONB
sa.EncryptedString = EncryptedString
sa.EncryptedText = EncryptedText

# revision identifiers, used by Alembic.
revision = '945e69b87a72'
down_revision = 'a22cc7704d14'
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
    op.create_table('competition',
    sa.Column('id', sa.GUID(length=16), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('date_start', sa.DateTimeUTC(timezone=True), nullable=True),
    sa.Column('date_end', sa.DateTimeUTC(timezone=True), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('sa_orm_sentinel', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTimeUTC(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTimeUTC(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_competition')),
    sa.UniqueConstraint('slug', name='uq_competition_slug')
    )
    with op.batch_alter_table('competition', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_competition_name'), ['name'], unique=False)
        batch_op.create_index('ix_competition_slug_unique', ['slug'], unique=True)

    op.create_table('division',
    sa.Column('id', sa.GUID(length=16), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('competition_id', sa.GUID(length=16), nullable=False),
    sa.Column('is_team', sa.Boolean(), nullable=False),
    sa.Column('team_size', sa.Integer(), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('sa_orm_sentinel', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTimeUTC(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTimeUTC(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['competition_id'], ['competition.id'], name=op.f('fk_division_competition_id_competition'), ondelete='cascade'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_division')),
    sa.UniqueConstraint('slug', name='uq_division_slug')
    )
    with op.batch_alter_table('division', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_division_name'), ['name'], unique=False)
        batch_op.create_index('ix_division_slug_unique', ['slug'], unique=True)

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.create_index('ix_role_slug_unique', ['slug'], unique=True)

    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.create_index('ix_tag_slug_unique', ['slug'], unique=True)

    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.create_index('ix_team_slug_unique', ['slug'], unique=True)

    with op.batch_alter_table('user_account', schema=None) as batch_op:
        batch_op.create_table_comment(
        'User accounts for application access',
        existing_comment=None
    )

    with op.batch_alter_table('user_account_oauth', schema=None) as batch_op:
        batch_op.create_table_comment(
        'Registered OAUTH2 Accounts for Users',
        existing_comment=None
    )

    with op.batch_alter_table('user_account_role', schema=None) as batch_op:
        batch_op.create_table_comment(
        'Links a user to a specific role.',
        existing_comment=None
    )

    # ### end Alembic commands ###

def schema_downgrades() -> None:
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_account_role', schema=None) as batch_op:
        batch_op.drop_table_comment(
        existing_comment='Links a user to a specific role.'
    )

    with op.batch_alter_table('user_account_oauth', schema=None) as batch_op:
        batch_op.drop_table_comment(
        existing_comment='Registered OAUTH2 Accounts for Users'
    )

    with op.batch_alter_table('user_account', schema=None) as batch_op:
        batch_op.drop_table_comment(
        existing_comment='User accounts for application access'
    )

    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.drop_index('ix_team_slug_unique')

    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_index('ix_tag_slug_unique')

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.drop_index('ix_role_slug_unique')

    with op.batch_alter_table('division', schema=None) as batch_op:
        batch_op.drop_index('ix_division_slug_unique')
        batch_op.drop_index(batch_op.f('ix_division_name'))

    op.drop_table('division')
    with op.batch_alter_table('competition', schema=None) as batch_op:
        batch_op.drop_index('ix_competition_slug_unique')
        batch_op.drop_index(batch_op.f('ix_competition_name'))

    op.drop_table('competition')
    # ### end Alembic commands ###

def data_upgrades() -> None:
    """Add any optional data upgrade migrations here!"""

def data_downgrades() -> None:
    """Add any optional data downgrade migrations here!"""
