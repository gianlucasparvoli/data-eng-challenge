from fastavro import writer, reader, schema
from rec_avro import to_rec_avro_destructive, from_rec_avro_destructive, rec_avro_schema
import requests, json

def dictionary_obj(obj, name):
    try:
        obj = json.dumps(obj)

        json_objects = json.loads(obj)
        
        # For efficiency, to_rec_avro_destructive() destroys rec, and reuses it's
        # data structures to construct avro_objects 
        avro_objects = (to_rec_avro_destructive(rec) for rec in json_objects)

        # store records in avro
        with open(f"backup/{name}.avro", 'wb') as f_out:
            try:
                writer(f_out, schema.parse_schema(rec_avro_schema()), avro_objects)
            except Exception as e:
                print(f"Error: ", e)

        #load records from avro
        with open(f"backup/{name}.avro", 'rb') as f_in:
            try:
                # For efficiency, from_rec_avro_destructive(rec) destroys rec, and 
                # reuses it's data structures to construct it's output
                loaded_json = [from_rec_avro_destructive(rec) for rec in reader(f_in)]
            except Exception as e:
                print(f"Error: ", e)

        assert loaded_json == json_objects
        return json_objects
    except Exception as e:
        print(f"Error: ", e)

def get_all_data(table):
    try:
        get_all_hired_employees_r = requests.get(url = f'http://localhost:5000/{table}')
        get_all_hired_employees = get_all_hired_employees_r.json()
        dictionary_obj(get_all_hired_employees, table)
    except Exception as e:
        print(f"Error: ", e)

get_all_data('department')
get_all_data('hired_employee')
get_all_data('job')