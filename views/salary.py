from flask import request, jsonify, make_response
import sqlalchemy as sa
from help.jwtdecorater import token_required
from models.db import Database
from models.employee import Employee
from models.salary import Salary
import datetime
import re

db = Database.db()

@token_required
class Salary_view:

    today = datetime.datetime.now()

    def date_format_validate(check_date):
        
        pattern_date = (r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
        match = re.match(pattern_date, check_date)
        return bool(match)

    def date_comparison(start_date, end_date):

        y1, m1, d1 = [int(x) for x in start_date.split('-')]
        y2, m2, d2 = [int(x) for x in end_date.split('-')]
        start_date = datetime.date(y1,m1,d1)
        end_date = datetime.date(y2, m2, d2)
        print(start_date)
        print(end_date)

        return (start_date < end_date)


    def create_financial_year():
        
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        created_by = request.form.get('created_by').lower()
        created_at = Salary_view.today.strftime("%d/%m/%Y %H:%M:%S")
        deleted_by = sa.sql.null()
        deleted_at = sa.sql.null()

        # employee role validation 
        if not(created_by == 'hr'):
            return({'message' : 'unsuccessful, employee is not hr'}), 401

        # date format validation 
        if not (Salary_view.date_format_validate(start_date) and Salary_view.date_format_validate(end_date)):
            return jsonify({'message' : 'unsuccessful, date format not valid'}), 400
        
        # date comparison 
        if not Salary_view.date_comparison(start_date, end_date):
            return jsonify({'message' : 'unsuccessful, end date must be greater than start_date'}), 400

        employees = Employee.query.filter_by(employee_role = created_by).first()
        financial_year = Salary(start_date, end_date, employees.employee_id, created_at, deleted_by, deleted_at)
        Database.db().session.add(financial_year)
        Database.db().session.commit()
            
        return jsonify({'message': 'financial year created successfully'}), 200

        # return jsonify({'message' : 'unsuccessful'}), 401

        
    '''def delete_financial_year(today):
        deleted_by = request.form.get('deleted_by').lower()
        deleted_at = today.strftime("%d/%m/%Y %H:%M:%S")'''




        