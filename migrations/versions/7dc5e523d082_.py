"""empty message

Revision ID: 7dc5e523d082
Revises: 
Create Date: 2019-12-15 00:56:56.283825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dc5e523d082'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('api', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('source', sa.String(length=30), nullable=False),
    sa.Column('destination', sa.String(length=30), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('traveltime', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('checked', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('action')
    # ### end Alembic commands ###
