from time import sleep

from selene import browser, have
from pages.API.auth import auth


class PreviousOrder:

    def open_previous_order(self):
        browser.open('en')
        cookies = auth.get_cookie()
        browser.driver.add_cookie({'name': 'autht4', 'value': cookies})
        browser.open('en')
        browser.all('.link').element_by(have.exact_text('Profile')).click()
        browser.all('.vue-dropdown li').first.click()

    def assert_previous_order(self):
        browser.element('[data-qa="card"]').element('a') \
            .should(have.exact_text('Koh Samui Transfer → Patong Kata Karon Transfer'))


previouseorder = PreviousOrder()
