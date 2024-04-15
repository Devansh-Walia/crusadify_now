"""Added Pages and Template Table

Revision ID: 1d0360cef4bd
Revises: dcaf18b60b4c
Create Date: 2024-04-14 19:09:33.990084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d0360cef4bd'
down_revision: Union[str, None] = 'dcaf18b60b4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'pages', ['id'])
    op.create_unique_constraint(None, 'templates', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'templates', type_='unique')
    op.drop_constraint(None, 'pages', type_='unique')
    # ### end Alembic commands ###
