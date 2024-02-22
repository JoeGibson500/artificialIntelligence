"""initial migration

Revision ID: a0a7640a3df3
Revises: 
Create Date: 2023-10-20 18:50:51.505953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0a7640a3df3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenditure',
    sa.Column('expenditure_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('desc', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('expenditure_id')
    )
    with op.batch_alter_table('expenditure', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_expenditure_desc'), ['desc'], unique=True)

    op.create_table('income',
    sa.Column('income_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('desc', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('income_id')
    )
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_income_desc'), ['desc'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_income_desc'))

    op.drop_table('income')
    with op.batch_alter_table('expenditure', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_expenditure_desc'))

    op.drop_table('expenditure')
    # ### end Alembic commands ###