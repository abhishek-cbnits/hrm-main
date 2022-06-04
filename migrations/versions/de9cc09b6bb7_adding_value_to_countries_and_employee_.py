"""Adding value to countries and employee database

Revision ID: de9cc09b6bb7
Revises: 48db4f99d3ae
Create Date: 2022-04-21 12:03:24.342999

"""
import hashlib
import psycopg2 as ps
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = 'de9cc09b6bb7'
down_revision = '48db4f99d3ae'
branch_labels = None
depends_on = None


def upgrade():

    # seeding data into countries table
    password="abc123"
    password = hashlib.md5(password.encode()).hexdigest()
    
    
    # op.execute(text("INSERT INTO countries(country_id, country_name)"),)

    op.execute("INSERT INTO countries(country_id, country_name) VALUES ('085c430e-6a11-435b-a794-77422dc8fb92', 'india')")
    op.execute("INSERT INTO countries(country_id, country_name) VALUES ('085c430e-6a11-435b-a794-77422dc8fb93', 'usa')")

    # seeding data into employees table
    op.execute("INSERT INTO employees(employee_id, country_id, employee_code, first_name, last_name, employee_role, email, phno, password, gender, otp) VALUES ('6189f2f2-8dc8-4f1b-a528-5ac8c4d0d571','085c430e-6a11-435b-a794-77422dc8fb92', 'emp123', 'hr', 'admin', 'hr', 'hr@admin.com', '9920345678', '" + password +"', 'female', '22345')")

     


def downgrade():
    pass

    # op.execute("DELETE FROM countries WHERE (country_id = '085c430e-6a11-435b-a794-77422dc8fb92')")
    # op.execute("DELETE FROM countries WHERE (country_id = '085c430e-6a11-435b-a794-77422dc8fb93')")
    # op.execute("DELETE FROM employees WHERE (employee_id = '82c8be2f-9ef4-48fa-adad-b8fe924e67af')")
