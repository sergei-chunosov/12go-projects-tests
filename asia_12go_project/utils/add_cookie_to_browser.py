from selene import browser


def add_cookies_to_browser(cookies):
    for name, cookie in cookies.items():
        browser.driver.add_cookie({'name': name, 'value': cookie})
