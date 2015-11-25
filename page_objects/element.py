from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    def __init__(self, locator, page):
        self.locator = locator
        self.driver = page.driver

    def get_value(self):
        return self._get_element().get_attribute('innerHTML')

    def _get_element(self):
        return WebDriverWait(self.driver, 100).until(lambda d: self.locator.locate(d))


class InputElement(BaseElement):
    def set_value(self, value):
        self._get_element().send_keys(value)

    def submit(self):
        self._get_element().submit()


class ClickableElement(BaseElement):
    def click(self):
        self._get_element().click()
