from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
from models.employee import Employee


db = SQLAlchemy()

class Salary(db.Model):
    __tablename__ = 'salary_fy'

    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable = False, default=uuid.uuid4)
    start_date = db.Column(db.Date(), nullable  = False)
    end_date = db.Column(db.Date(), nullable  = False)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey(Employee.employee_id), nullable  = False, default = uuid.uuid4)
    created_at = db.Column(db.DateTime(), nullable  = False)
    deleted_by = db.Column(UUID(as_uuid=True), db.ForeignKey(Employee.employee_id), nullable  = True, default = uuid.uuid4)
    deleted_at = db.Column(db.DateTime(), nullable  = True)

    def __init__(self, start_date, end_date, created_by, created_at, deleted_by, deleted_at):
        self.start_date = start_date
        self.end_date = end_date
        self.created_by = created_by
        self.created_at = created_at
        self.deleted_by = deleted_by
        self.deleted_at = deleted_at


'''class Components(db.Model):
    __tablename__ = 'salary_components'''



