from selene import browser, have


class LanguageChange:

    def open(self):
        browser.open('en')

    def language_change(self):
        browser.all('.link.lang-selector').first.click()
        browser.all('.dropdown').all('li').element_by(have.exact_text('Deutsch')).click()
        browser.all('.link.lang-selector').first.click()
        browser.all('.dropdown').all('li').element_by(have.exact_text('English')).click()

    def assert_language_change(self):
        browser.element('.link.lang-selector').should(have.exact_text('English'))


language_change = LanguageChange()
