import pytest
from pages.api.auth import auth
import allure
from utils.marks import layer

pytestmark = [
    layer("api")
]

@pytest.mark.api
def test_wrong_auth():
    with allure.step('Проверяем аутентификацию с невалидными данными через api'):
        cookies = auth.get_cookie(user_name='ncrs@test.test', password='123456')
        assert cookies == None
