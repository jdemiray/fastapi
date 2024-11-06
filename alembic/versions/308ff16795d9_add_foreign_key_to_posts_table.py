"""add foreign-key to posts table

Revision ID: 308ff16795d9
Revises: 2e308f335051
Create Date: 2024-11-05 17:16:25.630873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '308ff16795d9'
down_revision: Union[str, None] = '2e308f335051'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add phone_number column to users table
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    # Drop phone_number column from users table
    op.drop_column('users', 'phone_number')
