from datetime import date, timedelta


def date_halper():
    day = (date.today() + timedelta(days=4)).day
    weekday = (date.today() + timedelta(days=4)).strftime('%a')
    mothday = (date.today() + timedelta(days=4)).strftime('%h')
    date_for_test = f'{weekday}, {mothday} {day}'
    if date.today().day < day:
        page = 1
    else:
        page = 2

    return day, page, date_for_test
