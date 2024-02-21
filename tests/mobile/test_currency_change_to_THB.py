import pytest

from pages.mobile.currency_change_to_THB import change_currency
import allure


@pytest.mark.mobile
def test_currency():
    with allure.step('Выбираем необходимую валюту'):
        change_currency.change_currency()

    with allure.step('Проверяем выбранную валюту'):
        change_currency.assert_currency()
