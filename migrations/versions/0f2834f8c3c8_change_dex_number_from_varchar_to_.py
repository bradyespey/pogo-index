"""Change dex_number from VARCHAR to INTEGER in shinies and specials

Revision ID: 0f2834f8c3c8
Revises: 9ae7b8274197
Create Date: 2024-10-22 12:27:34.084876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f2834f8c3c8'
down_revision = '9ae7b8274197'
branch_labels = None
depends_on = None


def upgrade():
    # Changing dex_number from VARCHAR to INTEGER for shinies
    with op.batch_alter_table('shinies', schema=None) as batch_op:
        batch_op.alter_column(
            'dex_number',
            existing_type=sa.VARCHAR(length=10),
            type_=sa.Integer(),
            postgresql_using="dex_number::integer",
            existing_nullable=True
        )
    
    # Changing dex_number from VARCHAR to INTEGER for specials
    with op.batch_alter_table('specials', schema=None) as batch_op:
        batch_op.alter_column(
            'dex_number',
            existing_type=sa.VARCHAR(length=10),
            type_=sa.Integer(),
            postgresql_using="dex_number::integer",
            existing_nullable=True
        )


def downgrade():
    # Revert changes if needed
    with op.batch_alter_table('shinies', schema=None) as batch_op:
        batch_op.alter_column(
            'dex_number',
            existing_type=sa.Integer(),
            type_=sa.VARCHAR(length=10),
            existing_nullable=True
        )
    
    with op.batch_alter_table('specials', schema=None) as batch_op:
        batch_op.alter_column(
            'dex_number',
            existing_type=sa.Integer(),
            type_=sa.VARCHAR(length=10),
            existing_nullable=True
        )
