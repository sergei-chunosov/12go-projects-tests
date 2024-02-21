from selene import browser, have
from pages.api.auth import auth
from utils.add_cookie_to_browser import add_cookies_to_browser


class ChangeProfileInfo:

    def auth(self):
        browser.open('en')
        cookies = auth.get_cookie()
        add_cookies_to_browser(cookies)
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