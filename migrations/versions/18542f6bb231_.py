"""empty message

Revision ID: 18542f6bb231
Revises: 958f3ed97391
Create Date: 2017-06-18 01:55:57.478077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18542f6bb231'
down_revision = '958f3ed97391'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('formula', sa.Column('instructions', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('formula', 'instructions')
    # ### end Alembic commands ###
