import pytest

from pages.API.auth import auth
import allure

@pytest.mark.api
def test_auth():
    with allure.step('Проверяем успешную аутентификацию через API'):
        cookies = auth.get_cookie()
        assert len(cookies) > 0
