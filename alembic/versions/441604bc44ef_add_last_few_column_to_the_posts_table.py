"""add Last few Column to the  posts table

Revision ID: 441604bc44ef
Revises: 63dfed71fb38
Create Date: 2026-09-26 16:49:14.479947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '441604bc44ef'
down_revision: Union[str, Sequence[str], None] = '63dfed71fb38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published',sa.Boolean(),server_default='TRUE', nullable=False),)
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                  server_default=sa.text('now()'), nullable= False)
    
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts','created_at')
    pass
