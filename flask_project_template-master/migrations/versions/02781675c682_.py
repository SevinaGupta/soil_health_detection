"""empty message

Revision ID: 02781675c682
Revises: 11ab1a83c519
Create Date: 2020-04-08 12:39:20.999183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02781675c682'
down_revision = '11ab1a83c519'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message_data', sa.Column('density', sa.Integer(), nullable=True))
    op.add_column('message_data', sa.Column('mositure_id', sa.Integer(), nullable=False))
    op.add_column('message_data', sa.Column('mositure_per', sa.Integer(), nullable=True))
    op.add_column('message_data', sa.Column('time', sa.Integer(), nullable=True))
    op.drop_column('message_data', 'message')
    op.drop_column('message_data', 'id')
    op.drop_column('message_data', 'prediction')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message_data', sa.Column('prediction', sa.INTEGER(), nullable=True))
    op.add_column('message_data', sa.Column('id', sa.INTEGER(), nullable=False))
    op.add_column('message_data', sa.Column('message', sa.VARCHAR(), nullable=True))
    op.drop_column('message_data', 'time')
    op.drop_column('message_data', 'mositure_per')
    op.drop_column('message_data', 'mositure_id')
    op.drop_column('message_data', 'density')
    # ### end Alembic commands ###
