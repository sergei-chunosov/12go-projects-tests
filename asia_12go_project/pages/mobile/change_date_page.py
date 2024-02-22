from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from asia_12go_project.utils.set_date import date_halper


class ChangeDate:

    def __init__(self):
        self.day, self.page, self.date_for_test = date_halper()

    def set_date(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[3].click()
        browser.element((AppiumBy.XPATH, f'(//android.widget.TextView[@text="{self.day}"])["{self.page}"]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Done"]')).click()

    def assert_date(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[3].should(have.exact_text(f'{self.date_for_test}'))


change_date = ChangeDate()
