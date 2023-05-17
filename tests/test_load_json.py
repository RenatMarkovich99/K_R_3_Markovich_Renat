# Тесты на не корректное открытие, на корректное открытие не существующий файл
from utils.services import load_json


def test_correct_json():
    assert load_json(filename='data_tests/correct.json') == []


