
from sqlalchemy import Table, Column, Integer, ForeignKey,UniqueConstraint
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/data_eng_challenge'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100))

    def __init__(self, department):
        self.department = department

class DepartmentsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'department')

department_schema = DepartmentsSchema()
departments_schema = DepartmentsSchema(many=True) 


class Hired_Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    datetime = db.Column(db.String(10))
    department_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)

    def __init__(self, name, datetime,department_id,job_id):
        self.name = name
        self.datetime = datetime
        self.department_id = department_id
        self.job_id = job_id

class Hired_EmployeesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'datetime','department_id','job_id')

hired_employee_schema = Hired_EmployeesSchema()
hired_employees_schema = Hired_EmployeesSchema(many=True) 


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(50))

    def __init__(self, job):
        self.job = job

class JobsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'job')

job_schema = JobsSchema()
jobs_schema = JobsSchema(many=True) 


db.create_all()