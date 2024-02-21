from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from time import sleep
from datetime import date, timedelta



def test_button_more():
    ## language change
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="tab-button-more"]')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.click()
    browser.element((AppiumBy.XPATH, '//android.view.View[@text="English"]')).click()
    browser.all((AppiumBy.CSS_SELECTOR, 'android.widget.Button')).first\
        .should(have.exact_text('Language English'))

    browser.element((AppiumBy.XPATH, '//android.view.View[@text="Search"]')).click()

    sleep(2)
    ## currency change
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="tab-button-more"]')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).second.click()
    browser.element((AppiumBy.XPATH, '//android.view.View[normalize-space(@text)="THBThai baht"]')).click()


    browser.all((AppiumBy.CSS_SELECTOR, 'android.widget.Button')).second \
        .should(have.exact_text('THB Currency Thai baht'))

    browser.element((AppiumBy.XPATH, '//android.view.View[@text="Search"]')).click()


    ## check direction
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.click()

    browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Samui')
    browser.element((AppiumBy.XPATH, '//android.view.View[normalize-space(@text)="Koh Samui,Thailand"]')).click()

    browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Bangkok')
    browser.element((AppiumBy.XPATH, '//android.view.View[normalize-space(@text)="Bangkok,Thailand"]')).click()

    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.should(have.exact_text("Koh Samui"))
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[2].should(have.exact_text("Bangkok"))

    ##check mirroring direction

    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).second.click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).first.should(have.exact_text("Bangkok"))
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[2].should(have.exact_text("Koh Samui"))

    ## test date changes

    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[3].click()
    # tomorrow = (date.today() + timedelta(days=4)).day
    # day = date(day=tomorrow)
    day = (date.today() + timedelta(days=4)).day
    weekday = (date.today() + timedelta(days=4)).strftime('%a')
    mothday = (date.today() + timedelta(days=4)).strftime('%h')
    date_for_test = f'{weekday}, {mothday} {day}'
    if date.today().day < day:
         page = 1
    else:
         page = 2

    browser.element((AppiumBy.XPATH, f'(//android.widget.TextView[@text="{day}"])["{page}"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Done"]')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[3].should(have.exact_text(f'{date_for_test}'))


    ### test passengers count

    browser.all((AppiumBy.CLASS_NAME, 'android.view.View'))[7].click()
    sleep(5)
    browser.all((AppiumBy.CLASS_NAME, 'android.view.View'))[9].click()
    sleep(5)
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Done"]')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.view.View'))[7].should(have.exact_text(' 1 Passenger'))




    # pass
    # browser.open('en')
    # sleep(10)
    # browser.element((AppiumBy.ID, "00000000-0000-00ce-0000-14cc000000d9")).click()
    # browser.element((AppiumBy.CSS_SELECTOR, '[class="menu mobile"]')).click()
    # browser.all((AppiumBy.CSS_SELECTOR, '.vue-modal-content-body li')).first.should(have.exact_text('Support'))
    #
    # browser.element((AppiumBy.CSS_SELECTOR, '.vue-modal-content-body .curr-selector')).click()
    # browser.all((AppiumBy.CSS_SELECTOR, '[data-qa="topCurrencyItem"]'))[2].click()
    # browser.element((AppiumBy.CSS_SELECTOR, '.vue-modal-content-body .curr-selector')).should(have.text('Thai baht'))





# Sat, Feb 24
# print(date_for_test)
