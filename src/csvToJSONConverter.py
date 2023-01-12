import csv, re, json
import requests

with open('..\csv\departments.csv', mode='r') as csvFile:
    reader = csv.reader(csvFile)
    for rows in reader:
        try:
            dict_from_csv = json.dumps({"id":int(rows[0]),"department":rows[1]})
        except Exception as e:
            print(f"Error in ID {rows[0]}: ", e)
            continue
        r = requests.post('http://localhost:5000/department', json=dict_from_csv)
        print(f"Status Code: {r.status_code}, Response: {r.json()}")

with open('..\csv\hired_employees.csv', mode='r') as csvFile:
    reader = csv.reader(csvFile)
    dictToSend = []
    for rows in reader:
        try:
            dict_from_csv = {
                "id":int(rows[0]),
                "name":rows[1],
                "datetime" : rows[2],
                "department_id" : int(rows[3]), 
                "job_id" : int(rows[4])
                }
            dictToSend.append(dict_from_csv)
        except Exception as e:
            print(f"Error in ID {rows[0]}: ", e)
            continue
    r = requests.post('http://localhost:5000/hired_employee/batch', json=dictToSend)
    print(f"Status Code: {r.status_code}, Response: {r.json()}")  

with open('..\csv\jobs.csv', mode='r') as csvFile:
    reader = csv.reader(csvFile)
    dictToSend = []
    for rows in reader:
        try:
            dict_from_csv = {
                "id":int(rows[0]),
                "job":rows[1]
                }
            dictToSend.append(dict_from_csv)
        except Exception as e:
            print(f"Error in ID {rows[0]}: ", e)
            continue
    r = requests.post('http://localhost:5000/job/batch', json=dictToSend)
    print(f"Status Code: {r.status_code}, Response: {r.json()}")    

