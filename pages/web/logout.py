from time import sleep

from selene import browser, have, be
from pages.API.auth import auth


class LogOut:

    def open_profile(self):
        browser.open('en')
        cookies = auth.get_cookie()
        browser.driver.add_cookie({'name': 'autht4', 'value': cookies})
        browser.open('en')
        browser.all('.link').element_by(have.exact_text('Profile')).click()
        browser.all('.vue-dropdown li')[2].click()

    def assert_empty_profile(self):
        browser.all('.link').element_by(have.exact_text('Profile')).should(be.hidden)


logout = LogOut()
