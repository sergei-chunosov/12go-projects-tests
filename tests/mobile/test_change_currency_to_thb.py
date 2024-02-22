import pytest

from asia_12go_project.pages.mobile.currency_change_currency_to_thb_page import change_currency
import allure


@pytest.mark.mobile
def test_change_currency():
    with allure.step('Выбираем необходимую валюту'):
        change_currency.change_currency()

    with allure.step('Проверяем выбранную валюту'):
        change_currency.assert_currency()
