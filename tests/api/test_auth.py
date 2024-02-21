import pytest

from pages.api.auth import auth
import allure

@pytest.mark.api
def test_auth():
    with allure.step('Проверяем успешную аутентификацию через api'):
        cookies = auth.get_cookie()
        assert len(cookies) > 0, cookies
