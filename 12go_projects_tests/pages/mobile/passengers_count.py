from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class PassengersCount:

    def set_passengers_count(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.view.View'))[7].click()
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="__nuxt"]'
                                         '/android.view.View/android.view.View/'
                                         'android.view.View/android.view.View/'
                                         'android.view.View/android.view.View/'
                                         'android.view.View/android.view.View/'
                                         'android.view.View[1]/android.view.View[5]/'
                                         'android.view.View/android.view.View/'
                                         'android.view.View[2]/android.view.View/'
                                         'android.view.View/android.view.View[2]/android.view.View[1]')).click()

        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Done"]')).click()

    def assert_passengers_count(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.view.View'))[7].should(have.exact_text(' 1 Passenger'))


passengerscount = PassengersCount()
