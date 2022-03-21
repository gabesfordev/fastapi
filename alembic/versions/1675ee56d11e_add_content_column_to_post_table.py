"""add content column to post table

Revision ID: 1675ee56d11e
Revises: 323100db8638
Create Date: 2022-03-21 21:56:03.260551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1675ee56d11e"
down_revision = "323100db8638"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
