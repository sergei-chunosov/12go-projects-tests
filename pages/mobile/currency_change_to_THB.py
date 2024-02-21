from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ChangeCurrency:

    def change_currency(self):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="tab-button-more"]')).click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).second.click()
        browser.element((AppiumBy.XPATH, '//android.view.View[normalize-space(@text)="THBThai baht"]')).click()

    def assert_currency(self):
        browser.all((AppiumBy.CSS_SELECTOR, 'android.widget.Button')).second \
            .should(have.exact_text('THB Currency Thai baht'))


change_currency = ChangeCurrency()
