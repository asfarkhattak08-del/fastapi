"""add users table

Revision ID: 7c81af6e0235
Revises: 1019080c9ac5
Create Date: 2026-09-26 15:31:48.362537

"""
from tokenize import String
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '7c81af6e0235'
down_revision: Union[str, Sequence[str], None] = '1019080c9ac5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable= False),
                    sa.Column('email', sa.String(), nullable= False),
                    sa.Column('password', sa.String(), nullable= False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable= False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
