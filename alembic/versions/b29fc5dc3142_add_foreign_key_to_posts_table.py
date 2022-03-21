"""add foreign-key to posts table

Revision ID: b29fc5dc3142
Revises: 6967bcb22e5f
Create Date: 2022-03-21 22:19:04.839046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b29fc5dc3142"
down_revision = "6967bcb22e5f"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
