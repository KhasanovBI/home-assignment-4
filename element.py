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


class ClickableElement(BaseElement):
    def click(self):
        self._get_element().click()
