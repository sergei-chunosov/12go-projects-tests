import pytest
from asia_12go_project.utils.auth import auth
import allure


@pytest.mark.api
def test_wrong_auth():
    with allure.step('Проверяем аутентификацию с невалидными данными через api'):
        cookies = auth.get_cookie('/api/nuxt/en/user/auth', user_name='ncrs@test.test', password='123456')
        assert 'autht4' not in cookies
