import pytest
from asia_12go_project.pages.ui.logout_page import logout
import allure


@pytest.mark.web
def test_logout():
    with allure.step('Авторизовываемся на сайте и ищем предыдущий заказ'):
        logout.open_profile()

    with allure.step('Проверяем предыдущий заказ'):
        logout.assert_empty_profile()
