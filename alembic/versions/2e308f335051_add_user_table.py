"""add user table

Revision ID: 2e308f335051
Revises: 0dc9392d0d05
Create Date: 2024-11-05 16:55:23.306974

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = '2e308f335051'
down_revision = '0dc9392d0d05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = inspect(conn)

    # Check if the 'users' table already exists
    if 'users' not in inspector.get_table_names():
        op.create_table(
            'users',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('email', sa.String(), nullable=False),
            sa.Column('password', sa.String(), nullable=False),
            sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
            sa.UniqueConstraint('email')
        )


def downgrade() -> None:
    op.drop_table('users')
