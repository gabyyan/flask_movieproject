"""empty message

Revision ID: 815b8eb15ef6
Revises: 1ec474110fc6
Create Date: 2018-09-03 10:35:38.179295

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '815b8eb15ef6'
down_revision = '1ec474110fc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'nickname',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'nickname',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=False)
    # ### end Alembic commands ###
