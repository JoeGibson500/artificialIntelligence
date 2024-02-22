"""empty message

Revision ID: e77a2e9473ab
Revises: a0a7640a3df3
Create Date: 2023-10-20 18:57:10.090699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e77a2e9473ab'
down_revision = 'a0a7640a3df3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('expenditure', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_user_id', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_user_id', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_id', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('expenditure', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_id', type_='foreignkey')
        batch_op.drop_column('user_id')

    op.drop_table('user')
    # ### end Alembic commands ###
