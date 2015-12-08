from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    def __init__(self, locator, page):
        self.locator = locator
        self.driver = page.driver

    def get_value(self):
        return self._get_element().text

    def wait_displayed(self, d):
        try:
            return self.locator.locate(d).is_displayed()
        except StaleElementReferenceException:
            return False


    def _get_element(self):
        WebDriverWait(self.driver, 10).until(lambda d: self.locator.locate(d))
        WebDriverWait(self.driver, 10).until(lambda d: self.wait_displayed(d))
        return self.locator.locate(self.driver)

    def is_present(self):
        try:
            self._get_element()
            return True
        except TimeoutException:
            return False


class InputElement(BaseElement):
    def send_keys(self, value):
        self._get_element().send_keys(value)

    def set_value(self, value):
        self._get_element().clear()
        self._get_element().send_keys(value)

    def submit(self):
        self._get_element().submit()

import selenium.webdriver.support.expected_conditions as EC

class ClickableElement(BaseElement):
    def _wait_clickable(self, d):
        try:
            return self.locator.locate(d).is_enabled()
        except StaleElementReferenceException:
            return False

    def click(self):
        WebDriverWait(self.driver, 5).until(lambda d: self._wait_clickable(d))
        self._get_element().click()
