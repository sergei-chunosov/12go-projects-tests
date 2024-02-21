from selene import browser, have
from pages.api.auth import auth


class ChangeProfileInfo:

    def auth(self):
        browser.open('en')
        cookies = auth.get_cookie()
        for name, cookie in cookies.items():
            browser.driver.add_cookie({'name': name, 'value': cookie})
        browser.open('en')

    def change_name(self):
        browser.all('.link').element_by(have.exact_text('Profile')).click()
        browser.all('.vue-dropdown li').second.click()
        browser.element('[name="name"]').click().clear()
        browser.element('[name="name"]').click().type('Sergei Chunosov')

    def assert_change_name(self):
        name = browser.element('[name="name"]').locate().get_attribute('value')
        assert name == 'Sergei Chunosov'
        browser.element('[type="submit"]').click()


change_profile_info = ChangeProfileInfo()