"""create post table

Revision ID: 0dc9392d0d05
Revises: 
Create Date: 2024-11-05 16:49:23.306974

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = '0dc9392d0d05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = inspect(conn)

    # Check if the column 'owner_id' already exists
    if 'owner_id' not in [col['name'] for col in inspector.get_columns('posts')]:
        op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))

    # Add foreign key constraint after adding the column
    op.create_foreign_key(
        'post_users_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
