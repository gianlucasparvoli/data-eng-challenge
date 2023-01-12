import fastavro
import json
import os
import requests

def backupFromAvro(name):    
    try:
        data = []
        with open(f"backup/{name}.avro", "rb") as fo:
            for record in fastavro.reader(fo):
                data.append(record)

        json_final = []
        for d in data:
            dataJsonParsed = json.dumps(d).replace("}", "", 1).replace('{"_":',"")
            json_final.append(dataJsonParsed)

        r = requests.post(f"http://localhost:5000/{name}/batch", json=json_final)
        print(f"Status Code: {r.status_code}, Response: {r.json()}")  
    except Exception as e:
        print(f"Error: ", e)
backupFromAvro('department')
backupFromAvro('hired_employee')
backupFromAvro('job')