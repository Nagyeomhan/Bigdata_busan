"""empty message

Revision ID: 16627ab681f8
Revises: 
Create Date: 2022-10-18 15:35:01.404394

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '16627ab681f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('input', sa.Column('lot', sa.Integer(), nullable=False))
    op.add_column('input', sa.Column('time', sa.DateTime(), nullable=False))
    op.add_column('input', sa.Column('ph', sa.Float(), nullable=False))
    op.add_column('input', sa.Column('temp', sa.Float(), nullable=False))
    op.add_column('input', sa.Column('voltage', sa.Float(), nullable=False))
    op.drop_column('input', 'Lot')
    op.drop_column('input', 'Voltage')
    op.drop_column('input', 'Temp')
    op.drop_column('input', 'Time')
    op.drop_column('input', 'pH')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('input', sa.Column('pH', mysql.FLOAT(), nullable=False))
    op.add_column('input', sa.Column('Time', mysql.DATETIME(), nullable=False))
    op.add_column('input', sa.Column('Temp', mysql.FLOAT(), nullable=False))
    op.add_column('input', sa.Column('Voltage', mysql.FLOAT(), nullable=False))
    op.add_column('input', sa.Column('Lot', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('input', 'voltage')
    op.drop_column('input', 'temp')
    op.drop_column('input', 'ph')
    op.drop_column('input', 'time')
    op.drop_column('input', 'lot')
    # ### end Alembic commands ###