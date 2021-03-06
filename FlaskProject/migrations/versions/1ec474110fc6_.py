"""empty message

Revision ID: 1ec474110fc6
Revises: 9eff55524c0b
Create Date: 2018-09-03 10:33:29.871505

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1ec474110fc6'
down_revision = '9eff55524c0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movie', 'url',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=600),
               existing_nullable=False)
    op.alter_column('user', 'nickname',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('user', 'pwd',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=32),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'pwd',
               existing_type=sa.String(length=32),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('user', 'nickname',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('movie', 'url',
               existing_type=sa.String(length=600),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###
