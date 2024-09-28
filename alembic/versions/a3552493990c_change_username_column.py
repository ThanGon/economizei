"""Change Username Column

Revision ID: a3552493990c
Revises: 7c1dffba9c0f
Create Date: 2024-09-27 20:54:43.982434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3552493990c'
down_revision: Union[str, None] = '7c1dffba9c0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(), nullable=False))
    op.drop_column('users', 'nome')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
