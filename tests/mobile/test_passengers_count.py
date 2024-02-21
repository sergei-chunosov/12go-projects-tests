import pytest
from asia_12go_projects_tests.pages.mobile.passengers_count import passengerscount
import allure


@pytest.mark.mobile
def test_passengers_count():
    with allure.step('Устанавливаем количество пассажиров'):
        passengerscount.set_passengers_count()

    with allure.step('Проверяем количество пассажиров'):
        passengerscount.assert_passengers_count()
