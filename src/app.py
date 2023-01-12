from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
import csv, re, json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/data_eng_challenge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100))

    def __init__(self, id, department):
        self.id = id
        self.department = department

class DepartmentsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'department')

department_schema = DepartmentsSchema()
departments_schema = DepartmentsSchema(many=True) 

class Hired_Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    datetime = db.Column(db.String(40))
    department_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)

    def __init__(self, id, name, datetime,department_id,job_id):
        self.id = id
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

    def __init__(self, id, job):
      self.id = id
      self.job = job

class JobsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'job')

job_schema = JobsSchema()
jobs_schema = JobsSchema(many=True) 

@app.route('/departments', methods=['GET'])
def get_all_departments():
  all_departments = Departments.query.all()
  result = departments_schema.dump(all_departments)
  return jsonify(result)

@app.route('/department', methods=['POST'])
def create_department():
  try:
    dictionary = json.loads(request.json)
    id = dictionary["id"]
    department = dictionary["department"]

    new_department= Departments(id, department)

    db.session.add(new_department)
    db.session.commit()

    return department_schema.jsonify(new_department)
  except Exception as e:
    print(f"Error: ", e)

@app.route('/department/batch', methods=['POST'])
def create_Departments_batch():
  try:
    new_Departments = db.session.bulk_insert_mappings(Departments,request.json)
    db.session.commit()
    return departments_schema.jsonify(new_Departments)
  except Exception as e:
    print(f"Error: ", e)

@app.route('/hired_employees', methods=['GET'])
def get_all_hired_employees():
  all_hired_employees = Hired_Employees.query.all()
  result = hired_employees_schema.dump(all_hired_employees)
  return jsonify(result)

@app.route('/hired_employee', methods=['POST'])
def create_hired_employees():
  try:
    dictionary = json.loads(request.json)

    id = dictionary["id"]
    name = dictionary["name"]
    datetime = dictionary["datetime"]
    department_id = dictionary["department_id"]
    job_id = dictionary["job_id"]

    new_hired_employee= Hired_Employees(id, name, datetime,department_id,job_id)

    db.session.add(new_hired_employee)
    db.session.commit()

    return hired_employee_schema.jsonify(new_hired_employee)
  except Exception as e:
    print(f"Error: ", e)

@app.route('/hired_employee/batch', methods=['POST'])
def create_hired_employees_batch():
  try:
    new_hired_employee = db.session.bulk_insert_mappings(Hired_Employees,request.json)
    db.session.commit()
    return hired_employees_schema.jsonify(new_hired_employee)
  except Exception as e:
    print(f"Error: ", e)

@app.route('/jobs', methods=['GET'])
def get_all_job():
  all_jobs = Jobs.query.all()
  result = jobs_schema.dump(all_jobs)
  return jsonify(result)

@app.route('/job', methods=['POST'])
def create_job():
  try:
    dictionary = json.loads(request.json)
    id = dictionary["id"]
    job = dictionary["job"]

    new_job= Jobs(id,job)

    db.session.add(new_job)
    db.session.commit()

    return job_schema.jsonify(new_job)
  except Exception as e:
    print(f"Error: ", e)

@app.route('/job/batch', methods=['POST'])
def create_job_batch():
  try:
    new_jobs = db.session.bulk_insert_mappings(Jobs,request.json)
    db.session.commit()
    return jobs_schema.jsonify(new_jobs)
  except Exception as e:
    print(f"Error: ", e)


if __name__=='__main__':
    app.run(debug=True)

