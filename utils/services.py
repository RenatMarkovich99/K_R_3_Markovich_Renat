import json
import os.path

PATH_TO_DATA = os.path.abspath(os.path.join("..", "data"))
PATH_TO_OPERATION_JSON = os.path.join("..", PATH_TO_DATA, 'operation.json')





def load_json():
    with open(PATH_TO_OPERATION_JSON, 'r') as f:
        date = json.load(f)
    print(date)


load_json()
