import pytest
from asia_12go_project.pages.mobile.set_direction_page import set_directions
import allure


@pytest.mark.mobile
def test_set_directions():
    with allure.step('Задаем необходимые направления'):
        set_directions.set_directions()

    with allure.step('Проверяем выбранные направления'):
        set_directions.assert_directions()
