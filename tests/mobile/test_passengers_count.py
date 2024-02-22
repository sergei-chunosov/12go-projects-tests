import pytest
from asia_12go_project.pages.mobile.passengers_count_page import passengers_count
import allure


@pytest.mark.mobile
def test_passengers_count():
    with allure.step('Устанавливаем количество пассажиров'):
        passengers_count.set_passengers_count()

    with allure.step('Проверяем количество пассажиров'):
        passengers_count.assert_passengers_count()
