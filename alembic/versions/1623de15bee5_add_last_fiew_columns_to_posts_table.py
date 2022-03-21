"""add last fiew columns to posts table

Revision ID: 1623de15bee5
Revises: b29fc5dc3142
Create Date: 2022-03-21 22:29:09.983391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1623de15bee5"
down_revision = "b29fc5dc3142"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
