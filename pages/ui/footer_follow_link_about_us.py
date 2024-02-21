from selene import browser, have, command


class Footer_about_us:

    def open(self):
        browser.open('en')

    def follow_link(self):
        browser.all('.grid').all('li').second.perform(
            command.js.scroll_into_view).element('a').click()

    def assert_follow_link(self):
        browser.element('.large-text').element('p').should(have.exact_text('We provide all'
                                                                           ' travel services on a single platform'
                                                                           ' for comparison and interline ticketing.'
                                                                           ' To provide the best results we connect'
                                                                           ' directly to supplier systems via api.'))


footer_link = Footer_about_us()
