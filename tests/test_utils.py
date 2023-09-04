import pytest
from src.utils import get_date
from src.utils import get_description
from src.utils import get_full_card_data
from src.utils import get_full_account_data
from src.utils import get_amount
from src.utils import get_currency_name
from src.utils import hide_card_number
from src.utils import hide_account
from src.utils import hide_pay_info
from src.utils import right_date

@pytest.fixture
def dict1():
    return {'id': 285353808, 'state': 'EXECUTED', 'date': '2017-08-06T16:22:54.643491',
            'operationAmount': {'amount': '82946.19', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Открытие вклада', 'to': 'Счет 12189246980267075758'}

@pytest.fixture
def dict2():
    return {'id': 879660146, 'state': 'EXECUTED', 'date': '2018-07-22T07:42:32.953324',
            'operationAmount': {'amount': '92130.50', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации', 'from': 'Счет 19628854383215954147',
            'to': 'Счет 90887717138446397473'}


@pytest.fixture
def dict3():
    return {'id': 200634844, 'state': 'CANCELED', 'date': '2019-02-13T04:43:11.374324',
            'operationAmount': {'amount': '42210.20', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод организации', 'from': 'Счет 33355011456314142963', 'to': 'Счет 45735917297559088682'}


@pytest.fixture
def dict4():
    return {'id': 407169720, 'state': 'EXECUTED', 'date': '2020-02-03T14:52:08.093722',
            'operationAmount': {'amount': '67011.26', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод с карты на карту', 'from': 'MasterCard 4047671689373225',
            'to': 'Maestro 3806652527413662'}


def test_get_date(dict1):
    assert get_date(dict1) == '2017-08-06T16:22:54.643491'



def test_get_description(dict4):
    assert get_description(dict4) == 'Перевод с карты на карту'


def test_get_full_card_data(dict1):
    assert get_full_card_data(dict1) == ''

def test_get_full_card_data(dict2):
    assert get_full_card_data(dict2) == 'Счет 19628854383215954147'


def test_get_full_account_data(dict3):
    assert get_full_account_data(dict3) == 'Счет 45735917297559088682'


def test_get_amount(dict3):
    assert get_amount(dict3) == '42210.20'


def test_get_currency_name(dict2):
    assert get_currency_name(dict2) == 'USD'


def test_hide_card_number():
    assert hide_card_number('MasterCard 4047671689373225') == 'MasterCard 4047 67** **** 3225'


def test_hide_account():
    assert hide_account('Счет 33355011456314142963') == 'Счет **2963'


def test_hide_pay_info():
    assert hide_pay_info('Счет 33355011456314142963') == 'Счет **2963'
    assert hide_pay_info('') == ''
    assert hide_pay_info('MasterCard 4047671689373225') == 'MasterCard 4047 67** **** 3225'


def test_right_date():
    assert right_date('2019-02-13T04:43:11.374324') == '13.02.2019'