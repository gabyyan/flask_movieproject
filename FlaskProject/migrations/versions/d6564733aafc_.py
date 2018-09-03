"""empty message

Revision ID: d6564733aafc
Revises: 6739eeedb73c
Create Date: 2018-08-29 17:42:04.484473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6564733aafc'
down_revision = '6739eeedb73c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movie', 'addTime',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('preview', 'addTime',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('tag', 'addTime',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tag', 'addTime',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('preview', 'addTime',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('movie', 'addTime',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###