import pytest
from pages.ui.previous_order import previouseorder
import allure
from utils.marks import layer

pytestmark = [
    layer("web")
]


@pytest.mark.web
def test_previouse_order():
    with allure.step('Авторизовываемся на сайте и ищем предыдущий заказ'):
        previouseorder.open_previous_order()

    with allure.step('Проверяем предыдущий заказ'):
        previouseorder.assert_previous_order()
