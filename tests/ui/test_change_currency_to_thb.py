import pytest
from asia_12go_project.pages.ui.currency_change_currency_to_thb_page import change_currency
import allure


@pytest.mark.web
def test_change_currency():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        change_currency.open()

    with allure.step('Выбираем необходимую валюту'):
        change_currency.change_currency()

    with allure.step('Проверяем выбранную валюту'):
        change_currency.assert_currency()
