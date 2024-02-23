import pytest
from asia_12go_project.utils.api_requests import get_cookie
import allure
from jsonschema import validate
from asia_12go_project.data.schemas import successful_auth_response_result


@pytest.mark.api
def test_auth():
    with allure.step('Проверяем успешную аутентификацию через api'):
        cookies, response = get_cookie()
        validate(response.json(), successful_auth_response_result.successful_auth_response_result)
        assert response.status_code == 200
        assert len(cookies) > 0, cookies
