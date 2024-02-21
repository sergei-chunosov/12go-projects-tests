import pytest
from asia_12go_projects_tests.pages.api.auth import auth
import allure
from asia_12go_projects_tests.utils.marks import layer

pytestmark = [
    layer("api")
]

@pytest.mark.api
def test_wrong_auth():
    with allure.step('Проверяем аутентификацию с невалидными данными через api'):
        cookies = auth.get_cookie(user_name='ncrs@test.test', password='123456')
        assert 'autht4' not in cookies
