import pytest
from asia_12go_project.utils.auth import auth
import allure


@pytest.mark.api
def test_auth():
    with allure.step('Проверяем успешную аутентификацию через api'):
        cookies = auth.get_cookie('/api/nuxt/en/user/auth')
        assert len(cookies) > 0, cookies
