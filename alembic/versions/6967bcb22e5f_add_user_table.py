"""add user table

Revision ID: 6967bcb22e5f
Revises: 1675ee56d11e
Create Date: 2022-03-21 22:03:27.582935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6967bcb22e5f"
down_revision = "1675ee56d11e"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
