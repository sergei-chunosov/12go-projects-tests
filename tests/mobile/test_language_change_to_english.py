import pytest

from asia_12go_project.pages.mobile.language_change_to_english import language_change
import allure


@pytest.mark.mobile
def test_language_change():
    with allure.step('Меняем язык сайта на Английский'):
        language_change.language_change()

    with allure.step('Проверяем смену языка'):
        language_change.assert_language_change()
