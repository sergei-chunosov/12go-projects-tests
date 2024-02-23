import allure
import pytest
from asia_12go_project.utils.api_requests import post_request, delete_request


@pytest.mark.api
def test_add_ticket_to_cart_by_api():
    with allure.step('Добавляем билет в карзину через API'):
        url = '/api/nuxt/en/cart'
        payload = {
            "trips": [
                {
                    "tripId": "TH01xL01xR004a00l028QSB9",
                    "datetime": "2024-02-27-06-10-00"
                }
            ],
            "fromSlug": "bangkok",
            "toSlug": "koh-samui",
            "hash": "null",
            "seats": 1
        }

        response = post_request(url, json=payload)

        assert response.status_code == 200
        assert 'hash' in response.text

        return response.json()['hash']


@pytest.mark.api
def test_delete_ticket_from_cart():
    with allure.step('Удаляем билет из карзины через API'):
        hash = test_add_ticket_to_cart_by_api()
        url = '/api/nuxt/en/cart'
        payload = {
            "datetime": "2024-02-27-06-10-00",
            "hash": hash,
            "tripKey": "TH01xL01xR004a00l028QSB9"
        }
        response = delete_request(url, json=payload)

        assert response.status_code == 200
        assert len(response.json()['hash']) == 0
