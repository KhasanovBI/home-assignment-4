# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page_objects.review_page_object import *


class ReviewPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = ReviewPage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.quit()

    def test_average_of_stars(self):
        self.page.rate_stars(1, 1)
        self.page.rate_stars(2, 2)
        self.page.rate_stars(3, 3)
        self.page.rate_stars(4, 4)
        self.page.rate_stars(5, 5)
        self.page.wait_for_average(3, 1)
        self.assertTrue(self.page.average_stars.get_value(), '3')

    def test_mileage_input(self):
        self.page.probeg_input.set_value("-123a4#8")
        self.assertEquals(self.page.probeg_input.get_value(), "12 348")

    def test_invalid_text_fields(self):
        self.page.login()
        self.page.problems_input.set_value("lalala")
        self.page.submit_btn.click()
        self.assertTrue(self.page.common_input.is_invalid())
        self.assertTrue(self.page.advant_input.is_invalid())
        self.assertFalse(self.page.problems_input.is_invalid())
        self.assertTrue(self.page.invalid_list.get_value().find(u'достоинства') != -1)
        self.assertTrue(self.page.invalid_list.get_value().find(u'общее впечатление') != -1)
