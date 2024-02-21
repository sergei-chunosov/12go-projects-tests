import pytest

from pages.API.auth import auth
import allure

@pytest.mark.api
def test_wrong_auth():
    with allure.step('Проверяем аутентификацию с невалидными данными через API'):
        cookies = auth.get_cookie(user_name='ncrs@test.test', password='123456')
        assert cookies == None
