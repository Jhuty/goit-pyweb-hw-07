"""Remove date column from Group

Revision ID: b08d4a6c04cc
Revises: ff447f18f3c9
Create Date: 2024-07-21 20:33:12.287953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b08d4a6c04cc'
down_revision: Union[str, None] = 'ff447f18f3c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
