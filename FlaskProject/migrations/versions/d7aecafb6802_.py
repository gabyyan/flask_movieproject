"""empty message

Revision ID: d7aecafb6802
Revises: d836e2a13371
Create Date: 2018-09-07 09:42:33.464447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7aecafb6802'
down_revision = 'd836e2a13371'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('admin', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'role', 'admin', ['admin'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'role', type_='foreignkey')
    op.drop_column('role', 'admin')
    # ### end Alembic commands ###