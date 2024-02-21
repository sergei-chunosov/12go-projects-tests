from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SetDirections:

    def set_directions(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.click()

        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Samui')
        browser.element((AppiumBy.XPATH, '//android.view.View[normalize-space(@text)="Koh Samui,Thailand"]')).click()

        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Bangkok')
        browser.element((AppiumBy.XPATH, '//android.view.View[normalize-space(@text)="Bangkok,Thailand"]')).click()

    def assert_directions(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.should(have.exact_text("Koh Samui"))
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[2].should(have.exact_text("Bangkok"))


set_directions = SetDirections()
