import pytest
from asia_12go_project.pages.ui.change_profile_info import change_profile_info
import allure
from asia_12go_project.utils.marks import layer

pytestmark = [
    layer("web")
]


@pytest.mark.web
def test_change_profile_info():
    with allure.step('Авторизовываемся на сайте'):
        change_profile_info.auth()

    with allure.step('Изменяем имя пользователя в профиле'):
        change_profile_info.change_name()

    with allure.step('Проверяем данные'):
        change_profile_info.assert_change_name()
