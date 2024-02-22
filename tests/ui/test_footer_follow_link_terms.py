import allure
import pytest
from asia_12go_project.pages.ui.footer_follow_link_terms_page import footer_terms
from asia_12go_project.utils.marks import layer

pytestmark = [
    layer("web")
]

@pytest.mark.web
def test_link_about_us():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        footer_terms.open()

    with allure.step('Переходим по ссылке Terms and Conditions'):
        footer_terms.follow_link()

    with allure.step('Проверяем правильность перехода'):
        footer_terms.assert_follow_link()
