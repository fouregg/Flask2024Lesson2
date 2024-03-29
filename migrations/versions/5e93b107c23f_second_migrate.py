"""second migrate

Revision ID: 5e93b107c23f
Revises: 6ca739a9af82
Create Date: 2024-03-12 11:04:07.743258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e93b107c23f'
down_revision = '6ca739a9af82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', mysql.VARCHAR(length=100), nullable=True))

    # ### end Alembic commands ###
