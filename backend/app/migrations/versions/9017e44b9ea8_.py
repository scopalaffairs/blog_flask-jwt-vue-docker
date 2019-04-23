"""empty message

Revision ID: 9017e44b9ea8
Revises: 874a7362faac
Create Date: 2019-04-23 18:54:31.480684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9017e44b9ea8'
down_revision = '874a7362faac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('header_img', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogposts', 'header_img')
    # ### end Alembic commands ###