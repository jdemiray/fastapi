"""remove phone_number from posts

Revision ID: 45a546c93c13
Revises: 0d745e32a875
Create Date: 2024-11-05 19:21:32.755858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45a546c93c13'
down_revision: Union[str, None] = '0d745e32a875'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the phone_number column from the posts table
    op.drop_column('posts', 'phone_number')


def downgrade() -> None:
    # Optionally, add the column back in the downgrade
    op.add_column('posts', sa.Column('phone_number', sa.String(length=20)))
