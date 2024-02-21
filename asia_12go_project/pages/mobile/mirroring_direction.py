from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class MirroringDirection:

    def mirroring_directions(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).second.click()

    def assert_mirroring_directions(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.should(have.exact_text("Bangkok"))
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[2].should(have.exact_text("Koh Samui"))


mirroringdirection = MirroringDirection()
