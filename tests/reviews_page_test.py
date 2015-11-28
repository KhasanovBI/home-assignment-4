# coding: utf-8
import unittest
from urlparse import urlparse

from selenium.webdriver import DesiredCapabilities, Remote

from auth_settings import *
from page_objects.reviews_page_object import ReviewsPage


class AddReviewButtonCheck(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.reviews_page = ReviewsPage(self.driver)
        self.reviews_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_not_logged_add_review_button_click(self):
        add_review_button = self.reviews_page.add_review_button
        add_review_button.click()
        self.reviews_page.username_field.set_value(TEST_USER_LOGIN)
        self.reviews_page.password_field.set_value(TEST_USER_PASSWORD)
        self.reviews_page.username_field.submit()
        self.reviews_page.wait_another_page_loading()
        self.assertEquals(urlparse(self.reviews_page.get_current_url()).netloc, 'e.mail.ru')
