import json
import datetime


def load_operations(json_file):
    """Загружает данные из файла json"""
    with open(json_file) as file:
        operations = json.load(file)

    return operations


def sorted_list_operations(some_list):
    "сортирует список словарей по дате (начиная с последней операции)"
    sorted_list_operations = sorted(some_list, key=lambda x: x["date"], reverse=True)

    return sorted_list_operations


def get_date(some_dict: dict):
    """Получает дату операции"""
    return some_dict.get("date")


def get_description(some_dict: dict):
    """Получает описание типа перевода"""
    return some_dict.get("description")


def get_full_card_data(some_dict: dict):
    """Получает информацию о карте или счете, откуда сделан перевод"""
    if some_dict.get("from") != None:
        return some_dict.get("from")
    else:
        return ""


def get_full_account_data(some_dict: dict):
    """Получает информацию о карте или счете, куда сделан перевод"""
    return some_dict.get("to")


def get_amount(some_dict: dict):
    """Получает сумму операции"""
    return some_dict.get("operationAmount")["amount"]


def get_currency_name(some_dict: dict):
    """Получает валюту платежа"""
    return some_dict.get("operationAmount")["currency"]["name"]


def hide_card_number(full_card_data: str):
    """Делит номер карты на 4 части и маскирует 6 цифр (наячиная с 7)"""
    card_number = full_card_data.split(" ")[-1]
    name_card = " ".join(full_card_data.split(" ")[:-1])
    hide_number = name_card + " " + (card_number[:4] + " " +
                                     card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:])

    result = hide_number

    return result


def hide_account(full_account_data: str):
    """Маскирует номер счета"""
    account_number = full_account_data.split()[-1]
    hide_account_number = "**" + account_number[-4:]

    result = full_account_data.split()[0] + " " + hide_account_number

    return result


def hide_pay_info(data: str):
    """Определяет, какую информацию надо замаскировать(номер карты или номер счета)"""
    if "Счет" in data:
        return hide_account(data)
    elif data == "":
        return ""
    else:
        return hide_card_number(data)


def right_date(date_json: str):
    """Преобразует время в нужный формат"""
    result_date = datetime.datetime.fromisoformat(date_json).strftime("%d.%m.%Y")

    return result_date


def is_executed(some_dict: dict):
    """Проверяет операцию на исполненность"""
    if some_dict.get("state") == "EXECUTED":

        return True