"""empty message

Revision ID: e6f0d054b7a6
Revises: c447363f7efe
Create Date: 2018-08-29 17:46:49.253860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e6f0d054b7a6'
down_revision = 'c447363f7efe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('userIp', sa.String(length=30), nullable=False),
    sa.Column('loginTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('login_log')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login_log',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('userIp', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('loginTime', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='login_log_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('login')
    # ### end Alembic commands ###
