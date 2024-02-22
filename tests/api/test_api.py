import allure
import pytest
from jsonschema import validate
from asia_12go_project.data.schemas import successful_search_result
from asia_12go_project.utils.api_requests import post_request, delete_request, get_request


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


@pytest.mark.api
def test_get_info_about_trips():
    with allure.step('Проверяем поиск рейса через API'):
        url = '/api/nuxt/en/trips/' \
              'search' \
              '?fromId=1p' \
              '&toId=79p' \
              '&fromSlug=bangkok' \
              '&toSlug=koh-samui' \
              '&people=1' \
              '&date=2024-02-27' \
              '&csrf=sIht2g' \
              '&direction=forward'
        response = get_request(url)
        i = 0
        trip_key = 'TH01xL01xR004a00l028QSB9'
        while True:
            if response.json()['trips'][i]['segments'][0]['trip_id'] == trip_key:
                trip_id = response.json()['trips'][i]['segments'][0]['trip_id']
                schema = response.json()['trips'][i]['segments'][0]
                break
            i += 1

        validate(schema, successful_search_result.successful_search_result)
        assert response.status_code == 200
        assert trip_id == trip_key
