"""followers

Revision ID: 500d744d2668
Revises: 8388415d2247
Create Date: 2021-11-27 18:28:12.433414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500d744d2668'
down_revision = '8388415d2247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
