"""empty message

Revision ID: fa683db3c711
Revises: 815b8eb15ef6
Create Date: 2018-09-04 10:55:13.202056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa683db3c711'
down_revision = '815b8eb15ef6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'nickname',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('user', 'userName',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'userName',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('user', 'nickname',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###