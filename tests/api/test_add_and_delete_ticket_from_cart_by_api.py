import allure
import pytest
from asia_12go_project.utils.api_requests import post_request, delete_request
from asia_12go_project.utils.get_ticket_hash import get_ticket_hash


@pytest.mark.api
def test_add_ticket_to_cart_by_api():
    with allure.step('Добавляем билет в карзину через API'):
        response = get_ticket_hash()
        assert response.status_code == 200
        assert 'hash' in response.json()


@pytest.mark.api
def test_delete_ticket_from_cart():
    with allure.step('Удаляем билет из карзины через API'):
        get_response = get_ticket_hash().json()
        hash = get_response['hash']
        print('\n', hash, '\n')
        url = '/api/nuxt/en/cart'
        payload = {
            "datetime": "2024-02-27-06-10-00",
            "hash": hash,
            "tripKey": "TH01xL01xR004a00l028QSB9"
        }
        response = delete_request(url, json=payload)

        assert response.status_code == 200
        assert len(response.json()['hash']) == 0
