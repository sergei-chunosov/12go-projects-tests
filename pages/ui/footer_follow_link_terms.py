from selene import browser, have, command


class Footer_terms:

    def open(self):
        browser.open('en')

    def follow_link(self):
        browser.all('.grid').all('li')[2].perform(
            command.js.scroll_into_view).element('a').click()

    def assert_follow_link(self):
        browser.element('.markdowned').element('h1').should(have.exact_text('Terms and conditions'))


footer_terms = Footer_terms()
