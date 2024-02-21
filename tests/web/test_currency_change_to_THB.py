import pytest

from pages.web.currency_change_to_THB import change_currency
import allure


@pytest.mark.web
def test_currency():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        change_currency.open()

    with allure.step('Выбираем необходимую валюту'):
        change_currency.change_currency()

    with allure.step('Проверяем выбранную валюту'):
        change_currency.assert_currency()
