import pytest

from pages.mobile.set_direction import set_directions
from pages.mobile.mirroring_direction import mirroringdirection
import allure


@pytest.mark.mobile
def test_language_change():
    with allure.step('Задаем необходимые направления'):
        set_directions.set_directions()

    with allure.step('Проверяем выбранные направления'):
        set_directions.assert_directions()

    with allure.step('Меняем направления местами'):
        mirroringdirection.mirroring_directions()

    with allure.step('Проверяем зеркальную смену направления'):
        mirroringdirection.assert_mirroring_directions()
