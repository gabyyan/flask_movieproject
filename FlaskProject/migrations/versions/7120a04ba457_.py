"""empty message

Revision ID: 7120a04ba457
Revises: b26c0ac1a2ba
Create Date: 2018-09-08 18:20:50.129830

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7120a04ba457'
down_revision = 'b26c0ac1a2ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movie', 'playNum',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movie', 'playNum',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###