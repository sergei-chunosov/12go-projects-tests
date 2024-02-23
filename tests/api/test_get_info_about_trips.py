import allure
import pytest
from jsonschema import validate
from asia_12go_project.data.schemas import successful_search_result
from asia_12go_project.utils.api_requests import get_request
from asia_12go_project.utils.get_number_of_trip import get_number_of_trip


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
        trip_key = 'TH01xL01xR004a00l028QSB9'

        i = get_number_of_trip(response.json(), trip_key)

        trip_id = response.json()['trips'][i]['segments'][0]['trip_id']
        schema = response.json()['trips'][i]['segments'][0]

        validate(schema, successful_search_result.successful_search_result)
        assert response.status_code == 200
        assert trip_id == trip_key
