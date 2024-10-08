"""InitialTables

Revision ID: 7c1dffba9c0f
Revises: 
Create Date: 2024-09-27 20:27:24.239303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c1dffba9c0f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('balance', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('estimatedDate', sa.DateTime(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('interestRate', sa.DECIMAL(precision=1, scale=2), nullable=False),
    sa.Column('monthlyPayment', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=False),
    sa.Column('endDate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('saved', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('monthlySaving', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('interestRate', sa.DECIMAL(precision=1, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('net', sa.Enum('POSITIVE', 'NEGATIVE', name='netvalue'), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('savings')
    op.drop_table('loans')
    op.drop_table('goals')
    op.drop_table('users')
    # ### end Alembic commands ###
