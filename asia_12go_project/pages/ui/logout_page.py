from selene import browser, have, be
from asia_12go_project.utils.api_requests import get_cookie
from asia_12go_project.utils.add_cookie_to_browser import add_cookies_to_browser


class LogOut:

    def open_profile(self):
        browser.open('en')
        cookies = get_cookie()
        add_cookies_to_browser(cookies)
        browser.open('en')
        browser.all('.link').element_by(have.exact_text('Profile')).click()
        browser.all('.vue-dropdown li')[2].click()

    def assert_empty_profile(self):
        browser.all('.link').element_by(have.exact_text('Profile')).should(be.hidden)


logout = LogOut()
