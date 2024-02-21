from time import sleep

from selene import browser, have, command
from datetime import date, timedelta
from data.ui.user_data import Flight


class SearchTickets:


    def open(self):
        browser.open('en')

    def search_flight(self):
        sleep(3)
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

        browser.all('[data-qa=other-trips-show-options]').first.click().perform(command.js.scroll_into_view)

    def add_ticket_to_cart(self):
        sleep(4)
        browser.all('[data-qa="trip-time dep"]').element_by(have.text('06:10')).click()
        sleep(4)
        browser.element('[data-qa="trip-buy-button"]').click()
        sleep(4)
        browser.element('[data-qa=backBtn]').click()

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

search_tickets = SearchTickets()