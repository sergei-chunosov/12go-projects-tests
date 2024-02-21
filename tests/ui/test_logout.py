import pytest
from pages.ui.logout import logout
import allure
from utils.marks import layer

pytestmark = [
    layer("web")
]


@pytest.mark.web
def test_previouse_order():
    with allure.step('Авторизовываемся на сайте и ищем предыдущий заказ'):
        logout.open_profile()

    with allure.step('Проверяем предыдущий заказ'):
        logout.assert_empty_profile()
