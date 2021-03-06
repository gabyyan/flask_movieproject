"""empty message

Revision ID: 14f5e0614691
Revises: e5218b9eb779
Create Date: 2018-09-09 10:27:23.387914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f5e0614691'
down_revision = 'e5218b9eb779'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('addTime', sa.DateTime(), nullable=False))
    op.create_index(op.f('ix_admin_addTime'), 'admin', ['addTime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_admin_addTime'), table_name='admin')
    op.drop_column('admin', 'addTime')
    # ### end Alembic commands ###
