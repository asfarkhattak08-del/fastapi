"""add Column to Post table

Revision ID: 1019080c9ac5
Revises: 2df861fd1ae6
Create Date: 2026-09-26 15:23:29.306767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1019080c9ac5'
down_revision: Union[str, Sequence[str], None] = '2df861fd1ae6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts',"contents")
    pass
