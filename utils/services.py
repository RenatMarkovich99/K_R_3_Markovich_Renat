import json
from datetime import datetime

import os.path
from operator import itemgetter

# from data.operation.json
# PATH_TO_DATA = os.path.abspath(os.path.join("..", "data"))
# PATH_TO_OPERATION_JSON = os.path.join("..", PATH_TO_DATA, 'operation.json')
filename = '../data/operation.json'


def load_json(filename: str) -> list[dict, ...]:
    """
    Load file.
    :param filename: file json
    :return: json load file
    """
    with open(filename, 'r') as f:
        json_dict = json.load(f)
    return json_dict


def date_format(data_str: str, formatted_date: str = '%d.%m.%Y %H:%M:%S'):
    """
    Displaying the date in the correct format
    :param data_str:
    :param formatted_date:
    :return: formatted_data: date in correct format
    """
    parsed = datetime.strptime(data_str, '%d.%m.%Y %H:%M:%S')
    formatted_date = parsed.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date


def sort_by_date(json_dict=None):
    """
    sort the list in the order we want
    :param json_dict: json dict
    :return: sort_list: sort list
    """
    sort_list = sorted(json_dict, key=itemgetter('date'), reverse=True)
    return sort_list


def print_last_five_successful_operations():
    successful_operations = [op for op in json_dict['operations'] if
                             op['state'] == 'EXECUTED']
    last_five_successful_operations = successful_operations[-5:]
    for op in last_five_successful_operations:
        print(op)
