from time import sleep

from selene import browser, have, command
from datetime import date, timedelta
from asia_12go_project.data.ui.user_data import Flight


class AddTicketToCart:

    def open(self):
        browser.open('en')

    def search_flight(self):
        browser.all('[data-qa=select-button]').first.type('Bangkok')
        browser.element('[data-qa=select-list]').all('li').first.click()

        browser.element('input').type('Koh Samui')
        browser.element('[data-qa=select-list]').all('li').first.click()

        browser.element('[data-qa=datepicker-button]').click()
        tomorrow = date.today() + timedelta(days=5)
        browser.element(f'[data-qa="day({tomorrow})"]').click()
        browser.element('[data-qa=datepicker-done-button]').click()

        browser.element('[data-qa=people-button]').click()
        browser.all('.field-people-counter-decrease').first.click()
        browser.element('[type=submit]').click()

        browser.element('[data-qa=search-form-submit-button]').click()

        browser.all('[data-qa=other-trips-show-options]').first.click() \
            .perform(command.js.scroll_into_view).with_(timeout=10)

    def add_ticket_to_cart(self):
        browser.all('[data-qa="trip-time dep"]').with_(timeout=10).element_by(have.text('06:10')).click()
        browser.element('[data-qa="trip-buy-button"]').click()
        browser.element('[data-qa=backBtn]').with_(timeout=10).click()

        browser.element('.vue-badge').click()

    def assert_ticket(self, flight: Flight):
        browser.all('.trip-points-line-desc').all('span').should(have.exact_texts(
            flight.departure_airport,
            flight.flight,
            flight.arrival_airport
        ))

        browser.all('.time-label').should(have.exact_texts(
            flight.departure_time,
            flight.arrival_time
        ))


add_ticket_to_cart = AddTicketToCart()
