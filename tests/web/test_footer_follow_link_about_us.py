import allure
import pytest

from pages.web.footer_follow_link_about_us import footer_link


@pytest.mark.web
def test_link_about_us():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        footer_link.open()

    with allure.step('Переходим по ссылке about us'):
        footer_link.follow_link()

    with allure.step('Проверяем правильность перехода'):
        footer_link.assert_follow_link()
