import json
from datetime import datetime

import os.path

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
    parsed = datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = parsed.strftime(formatted_date)
    return formatted_date


def get_last_five_successful_operations(sort_list: list) -> list:
    """
     last five successful operations
    :return: last_five_successful_operations: last five successful operations
    """
    successful_operations = [op for op in sort_list if op["state"] == "EXECUTED"]
    last_five_successful_operations = successful_operations[:5]

    return last_five_successful_operations


def sort_by_date(json_dict=None):
    """
    sort the list in the order we want
    :param json_dict: json dict
    :return: sort_list: sort list
    """
    sort_list = sorted(json_dict, key=lambda x: x.get("date"), reverse=True)
    return sort_list


# def mask_card(operations):
#     from_card = operations.get('from', '')
#     from_card_masked = f'{from_card[:4]} {from_card[4:8]}**{from_card[-4:]}'
#     return from_card_masked


# def mask_account(operations):
#     to_account = operations.get('to', '')
#     to_account_masked = f'**{to_account[-4:]}'
#     return to_account_masked


# def print_info(operations):
#     for op in operations:
#         print(f"{date_format(op['date'])} {op['description']}\n"
#               f"{mask_card} -> Счет {mask_account}\n"
#               f"{operations["operationAmount"]["amount"]}\n"
#               f"{operations["operationAmount"]["currency"]}")

def mask_card(operation_credintials: str) -> str:
    """
    Маскирует номер счета/карты

    Args:
    operation_credintials (str) - полные реквизиты счета/банковской карты
    Return:
    Замаскированный счет/номер карты
    """

    # Если по ключу получили значение
    if operation_credintials:

    # Берем счет, пример: Visa Classic 6831982476737658
    # Разбиваем строку по пробелам и берем все до последнего элемента - это название счета
        credintials_name = " ".join(operation_credintials.split(" ")[:-1])  # Visa Classic
        # Последний элемент - всегда цифры
        credintials_number = operation_credintials.split(" ")[-1]  # 6831982476737658

    # Если номер состоит из 16 цифр - это номер карты. Маскируем как карту
    if len(credintials_number) == 16:
        # Берем первые 6 чисел и последние 4. Отсальное звездочки
        number_hide = credintials_number[:6] + "*" * 6 + credintials_number[:-4]
        # Разбиваем единое число на блоки по 4 цифры
        number_sep = [number_hide[i:i + 4] for i in range(0, len(credintials_number), 4)]
        #Возвращаем полный счет с именем и замаскированными цифрами
        return f'{credintials_name} {" ".join(number_sep)}'
        # Если номер состоит из 20 цифр - это номер счета
        elif len(credintials_number) == 20:
        # Просто берем последние 4 цифры, остальное заменяем на две звездочки
        return f'{credintials_name} {credintials_number.replace(credintials_number[:-4], "**")}'

        # Если по ключу не было получено значение - то возвращаем просто строку N/A (неопределённы)
        return "N/A"

def print_info(operations):
    for op in operations:
        print(f"{date_format(op['date'])} {op['description']}\n"
              f"{mask_card(op.get('from'))} -> {mask_card(op.get('to'))}\n")


