from selene import browser, have
from asia_12go_project.pages.api.auth import auth
from asia_12go_project.utils.add_cookie_to_browser import add_cookies_to_browser


class PreviousOrder:

    def open_previous_order(self):
        browser.open('en')
        cookies = auth.get_cookie()
        add_cookies_to_browser(cookies)
        browser.open('en')
        browser.all('.link').element_by(have.exact_text('Profile')).click()
        browser.all('.vue-dropdown li').first.click()

    def assert_previous_order(self):
        browser.element('[data-qa="card"]').element('a') \
            .should(have.exact_text('Koh Samui Transfer → Patong Kata Karon Transfer'))


previouse_order = PreviousOrder()
