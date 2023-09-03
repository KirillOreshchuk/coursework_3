import json


def load_operations(json_file):
    """Загружает данные из файла json"""
    with open(json_file) as file:
        operations = json.load(file)

    return operations


operations = load_operations("operations.json")


def sorted_list_operations(some_list):
    "сортирует список словарей по дате (начиная с последней операции)"
    sorted_list_operations = sorted(some_list, key=lambda x: x["date"], reverse=True)

    return sorted_list_operations


sorted_list_operations = sorted_list_operations(operations)


def hide_card_number(full_card_data):
    """Делит номер карты на 4 части и скрывет 6 цифр (наячиная с 7)"""
    card_number = full_card_data.split(" ")[-1]
    hide_part = (len(card_number[6:-4]))
    hide_number = card_number[:6] + (hide_part * "*") + card_number[-4:]

    part, part_size = len(hide_number), len(hide_number) // 4
    digit_part_card = (" ".join([hide_number[i:i+part_size] for i in range(0, part, part_size)]))

    result = " ".join(full_card_data.split(" ")[:-1]) + " " + digit_part_card

    return result


def hide_account(full_account_data):
    """Маскирует номер счета"""
    account_number = full_account_data.split()[-1]
    hide_part = len(account_number[-6:-4]) * "*"
    hide_account_number = hide_part + account_number[-4:]

    result = full_account_data.split()[0] + " " + hide_account_number

    return result

print(hide_account("Счет 35158586384610753655"))










