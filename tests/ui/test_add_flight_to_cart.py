import pytest
from asia_12go_project.data.ui.user_data import flight
from asia_12go_project.pages.ui.add_flight_to_cart import search_tickets
import allure
from asia_12go_project.utils.marks import layer

pytestmark = [
    layer("web")
]


@pytest.mark.web
def test_add_ticket():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        search_tickets.open()

    with allure.step('Ищем подходящий рейс'):
        search_tickets.search_flight()

    with allure.step('Добавляем билет в карзину'):
        search_tickets.add_ticket_to_cart()

    with allure.step('Проверяем билет'):
        search_tickets.assert_ticket(flight)
