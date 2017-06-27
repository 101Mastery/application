"""empty message

Revision ID: 34ee895cd05e
Revises: 0b1eb612cbc2
Create Date: 2017-06-25 22:04:05.004729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34ee895cd05e'
down_revision = '0b1eb612cbc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_creator')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_creator', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
