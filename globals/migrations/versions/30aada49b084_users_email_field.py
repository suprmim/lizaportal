"""users: email field

Revision ID: 30aada49b084
Revises: e5daadfbf710
Create Date: 2017-02-21 12:27:41.911483

"""

# revision identifiers, used by Alembic.
revision = '30aada49b084'
down_revision = 'e5daadfbf710'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    ### end Alembic commands ###
