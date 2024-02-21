import pytest
from asia_12go_projects_tests.pages.ui.logout import logout
import allure
from asia_12go_projects_tests.utils.marks import layer

pytestmark = [
    layer("web")
]


@pytest.mark.web
def test_logout():
    with allure.step('Авторизовываемся на сайте и ищем предыдущий заказ'):
        logout.open_profile()

    with allure.step('Проверяем предыдущий заказ'):
        logout.assert_empty_profile()
