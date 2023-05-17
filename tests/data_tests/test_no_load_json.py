from utils.services import load_json


def test_no_correct_json():
    assert load_json(filename='data_tests/no_correct.json') == []