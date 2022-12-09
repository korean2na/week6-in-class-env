"""Added car model

Revision ID: e1a65206923e
Revises: a78aaab01f55
Create Date: 2022-12-06 14:59:53.811747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1a65206923e'
down_revision = 'a78aaab01f55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('selling_price', sa.Float(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
