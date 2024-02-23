import pytest
from asia_12go_project.pages.ui.previous_order_page import previouse_order
import allure


@pytest.mark.web
def test_previous_order():
    with allure.step('Авторизовываемся на сайте и ищем предыдущий заказ'):
        previouse_order.open_previous_order()

    with allure.step('Проверяем предыдущий заказ'):
        previouse_order.assert_previous_order()
