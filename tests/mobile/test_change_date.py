import pytest
from asia_12go_project.pages.mobile.change_date import changedate
import allure


@pytest.mark.mobile
def test_change_date():
    with allure.step('Устанавливаем необходимую дату'):
        changedate.set_date()

    with allure.step('Проверяем выбранную дату'):
        changedate.assert_date()
