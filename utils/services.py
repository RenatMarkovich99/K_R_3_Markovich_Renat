import json


file_ = '../question/questions.json'


def load_json(file_path):
    with open('file_path', 'r') as f:
        date = json.load(f)
    return date

