import pytest
from asia_12go_project.pages.mobile.change_date_page import change_date
import allure


@pytest.mark.mobile
def test_change_date():
    with allure.step('Устанавливаем необходимую дату'):
        change_date.set_date()

    with allure.step('Проверяем выбранную дату'):
        change_date.assert_date()
