import pytest
from asia_12go_project.pages.api.auth import auth
import allure
from asia_12go_project.utils.marks import layer

pytestmark = [
    layer("api")
]

@pytest.mark.api
def test_auth():
    with allure.step('Проверяем успешную аутентификацию через api'):
        cookies = auth.get_cookie()
        assert len(cookies) > 0, cookies
