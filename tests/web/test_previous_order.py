import pytest

from pages.web.previous_order import previouseorder
import allure


@pytest.mark.web
def test_previouse_order():
    with allure.step('Авторизовываемся на сайте и ищем предыдущий заказ'):
        previouseorder.open_previous_order()

    with allure.step('Проверяем предыдущий заказ'):
        previouseorder.assert_previous_order()
