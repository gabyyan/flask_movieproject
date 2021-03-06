"""empty message

Revision ID: 2f0ce0ffb3fe
Revises: 8ffe136060cf
Create Date: 2018-09-06 17:10:43.363363

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2f0ce0ffb3fe'
down_revision = '8ffe136060cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin', 'name',
               existing_type=mysql.VARCHAR(charset='utf8', length=30),
               nullable=False)
    op.alter_column('auth', 'name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=30),
               nullable=False)
    op.add_column('role', sa.Column('name', sa.String(length=30), nullable=False))
    op.drop_column('role', 'adminName')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('adminName', mysql.VARCHAR(length=30), nullable=False))
    op.drop_column('role', 'name')
    op.alter_column('auth', 'name',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('admin', 'name',
               existing_type=mysql.VARCHAR(charset='utf8', length=30),
               nullable=True)
    # ### end Alembic commands ###
