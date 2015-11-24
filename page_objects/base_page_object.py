import urlparse

from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://cars.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def get_current_url(self):
        return self.driver.current_url

    def wait_another_page_loading(self):
        old_page = self.driver.find_element_by_tag_name('html')
        WebDriverWait(self.driver, 5).until(staleness_of(old_page))


class Component(object):
    def __init__(self, driver):
        self.driver = driver
