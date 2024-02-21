import pytest

from pages.mobile.set_direction import set_directions
import allure


@pytest.mark.mobile
def test_set_directions():
    with allure.step('Задаем необходимые направления'):
        set_directions.set_directions()

    with allure.step('Проверяем выбранные направления'):
        set_directions.assert_directions()
