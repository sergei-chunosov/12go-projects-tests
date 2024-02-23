import pytest
from asia_12go_project.utils.api_requests import get_cookie
import allure
from jsonschema import validate
from asia_12go_project.data.schemas import usuccessful_auth_response_result


@pytest.mark.api
def test_wrong_auth():
    with allure.step('Проверяем аутентификацию с невалидными данными через api'):
        cookies, response = get_cookie(user_name='ncrs@test.test', password='123456')
        validate(response.json(), usuccessful_auth_response_result.usuccessful_auth_response_result)
        assert 'autht4' not in cookies
        assert response.status_code == 401
