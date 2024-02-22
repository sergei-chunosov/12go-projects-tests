import pytest
from asia_12go_project.utils.api_requests import get_cookie
import allure


@pytest.mark.api
def test_auth():
    with allure.step('Проверяем успешную аутентификацию через api'):
        cookies = get_cookie()
        assert len(cookies) > 0, cookies
