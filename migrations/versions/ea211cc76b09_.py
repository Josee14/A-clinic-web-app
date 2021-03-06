"""empty message

Revision ID: ea211cc76b09
Revises: 772d23b04ba8
Create Date: 2021-07-31 16:51:26.558950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea211cc76b09'
down_revision = '772d23b04ba8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appointments', 'status')
    # ### end Alembic commands ###
