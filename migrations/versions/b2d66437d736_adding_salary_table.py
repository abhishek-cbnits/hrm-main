"""Adding salary table

Revision ID: b2d66437d736
Revises: de9cc09b6bb7
Create Date: 2022-04-28 13:22:22.187581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import datetime


# revision identifiers, used by Alembic.
revision = 'b2d66437d736'
down_revision = 'de9cc09b6bb7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'salary_fy', 
        sa.Column('id', UUID, primary_key=True),
        sa.Column('start_date', sa.Date, nullable = False),
        sa.Column('end_date', sa.Date, nullable = False),
        sa.Column('created_by', UUID, sa.ForeignKey('employees.employee_id'), nullable = False),
        sa.Column('created_at', sa.DateTime(), nullable = False),
        sa.Column('deleted_by', UUID, sa.ForeignKey('employees.employee_id'), nullable = True),
        sa.Column('deleted_at', sa.DateTime(), nullable = True),
    )


def downgrade():
    op.drop_table('salary_fy')
