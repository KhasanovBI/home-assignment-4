import urlparse
from contextlib import contextmanager

from selenium.webdriver.support.expected_conditions import staleness_of

from auth_settings import TEST_USER_LOGIN, TEST_USER_PASSWORD
from element import *
from locators import MainPageLocators


class Page(object):
    BASE_URL = 'https://cars.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver
        self.username_field = InputElement(MainPageLocators.USERNAME_FIELD, self)
        self.password_field = InputElement(MainPageLocators.PASSWORD_FIELD, self)
        self.login_button = ClickableElement(MainPageLocators.LOGIN_BUTTON, self)
        self.email_field = ClickableElement(MainPageLocators.USER_EMAIL_HREF, self)
        self.logout_button = ClickableElement(MainPageLocators.LOGOUT_BUTTON, self)

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def get_current_url(self):
        return self.driver.current_url

    def wait_another_page_loading(self):
        old_page = self.driver.find_element_by_tag_name('html')
        WebDriverWait(self.driver, 30).until(staleness_of(old_page))

    def login(self):
        self.login_button.click()
        self.username_field.set_value(TEST_USER_LOGIN)
        self.password_field.set_value(TEST_USER_PASSWORD)
        self.username_field.submit()


class Component(object):
    def __init__(self, driver):
        self.driver = driver
