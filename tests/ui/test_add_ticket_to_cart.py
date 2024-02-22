import pytest
from asia_12go_project.data.ui.user_data import flight
from asia_12go_project.pages.ui.add_ticket_to_cart_page import add_ticket_to_cart
import allure
from asia_12go_project.utils.marks import layer

pytestmark = [
    layer("web")
]


@pytest.mark.web
def test_add_ticket():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        add_ticket_to_cart.open()

    with allure.step('Ищем подходящий рейс'):
        add_ticket_to_cart.search_flight()

    with allure.step('Добавляем билет в карзину'):
        add_ticket_to_cart.add_ticket_to_cart()

    with allure.step('Проверяем билет'):
        add_ticket_to_cart.assert_ticket(flight)
