"""add forigen Key to post table

Revision ID: 63dfed71fb38
Revises: 7c81af6e0235
Create Date: 2026-09-26 16:42:55.591577

"""
from tkinter import CASCADE
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63dfed71fb38'
down_revision: Union[str, Sequence[str], None] = '7c81af6e0235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table= 'posts', 
                          referent_table='users', local_cols=['owner_id'],remote_cols=['id'], ondelete=CASCADE)
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
