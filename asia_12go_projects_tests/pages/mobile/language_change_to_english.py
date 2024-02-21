from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class LanguageChange:

    def language_change(self):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="tab-button-more"]')).click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.click()
        browser.element((AppiumBy.XPATH, '//android.view.View[@text="English"]')).click()

    def assert_language_change(self):
        browser.all((AppiumBy.CSS_SELECTOR, 'android.widget.Button')).first \
            .should(have.exact_text('Language English'))


language_change = LanguageChange()
