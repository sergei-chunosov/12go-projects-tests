from selene import browser, have
# from utils.auth import get_cookie


class ChangeCurrency:

    def open(self):
        browser.open('en')
        # cookies = get_cookie()
        # browser.driver.add_cookie({'name': 'autht4', 'value': cookies})
        # browser.open('en')

    def change_currency(self):
        browser.element('.link.curr-selector').click()
        browser.all('[data-qa=topCurrencyItem]')[2].click()

    def assert_currency(self):
        browser.element('.curr-selector span').should(have.text('THB'))


change_currency = ChangeCurrency()
