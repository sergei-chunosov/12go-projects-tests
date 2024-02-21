from selene import browser, have


class ChangeCurrency:

    def open(self):
        browser.open('en')

    def change_currency(self):
        browser.element('.link.curr-selector').click()
        browser.all('[data-qa=topCurrencyItem]')[2].click()

    def assert_currency(self):
        browser.element('.curr-selector span').should(have.text('THB'))


change_currency = ChangeCurrency()
