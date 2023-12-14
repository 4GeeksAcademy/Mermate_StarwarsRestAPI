"""empty message

Revision ID: f01edb1dff53
Revises: 04c5968566c9
Create Date: 2023-12-14 20:25:46.615660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f01edb1dff53'
down_revision = '04c5968566c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=False),
    sa.Column('terrain', sa.String(length=80), nullable=False),
    sa.Column('population', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name')
    )
    op.drop_table('planet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('planet_name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('diameter', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('climate', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('terrain', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('population', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='planet_pkey'),
    sa.UniqueConstraint('planet_name', name='planet_planet_name_key')
    )
    op.drop_table('planets')
    # ### end Alembic commands ###
