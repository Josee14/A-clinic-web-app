"""empty message

Revision ID: 772d23b04ba8
Revises: 91b9b6d84b92
Create Date: 2021-07-31 16:45:38.721174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '772d23b04ba8'
down_revision = '91b9b6d84b92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('appointments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.create_foreign_key(None, 'appointments', 'user', ['user_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.create_foreign_key(None, 'appointments', 'user', ['user_id'], ['id'])
    op.alter_column('appointments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###