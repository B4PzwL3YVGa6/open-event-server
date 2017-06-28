"""empty message

Revision ID: ca628ab9ac91
Revises: 23ff3fbdc6da
Create Date: 2016-08-24 16:55:09.605900

"""

# revision identifiers, used by Alembic.
revision = 'ca628ab9ac91'
down_revision = '23ff3fbdc6da'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image_sizes', sa.Column('type', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image_sizes', 'type')
    ### end Alembic commands ###