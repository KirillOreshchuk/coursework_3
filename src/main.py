from src.utils import load_operations
from src.utils import sorted_list_operations
from src.utils import get_date
from src.utils import get_description
from src.utils import get_full_card_data
from src.utils import get_full_account_data
from src.utils import get_amount
from src.utils import get_currency_name
from src.utils import right_date
from src.utils import hide_pay_info
from src.utils import is_executed


def main(file_json):
    """Основная функция программы"""
    count_operations = 0
    for operation in sorted_list_operations(load_operations(file_json)):
        if count_operations < 5:
            if is_executed(operation) is True:
                count_operations += 1
                print(f"{right_date(get_date(operation))} {get_description(operation)}")
                print(f"{hide_pay_info(get_full_card_data(operation))} -> "
                      f"{hide_pay_info(get_full_account_data(operation))}")
                print(f"{get_amount(operation)} {get_currency_name(operation)}\n")

            else:
                continue
        else:
            break


if __name__ == "__main__":
    main("../operations.json")