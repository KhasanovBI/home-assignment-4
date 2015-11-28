# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page_objects.review_page_object import *


class StarsCalculationTest(unittest.TestCase):
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

    def test_none_of_stars(self):
        self.assertTrue(self.page.average_stars.get_value(), '0')

    def test_min_of_stars(self):
        self.page.rate_stars(0, 1)
        self.page.rate_stars(1, 1)
        self.page.rate_stars(2, 1)
        self.page.rate_stars(3, 1)
        self.page.rate_stars(4, 1)
        self.page.rate_stars(5, 1)
        self.page.wait_for_average(1, 1)
        self.assertTrue(self.page.average_stars.get_value(), '1')

    def test_max_of_stars(self):
        self.page.rate_stars(0, 5)
        self.page.rate_stars(1, 5)
        self.page.rate_stars(2, 5)
        self.page.rate_stars(3, 5)
        self.page.rate_stars(4, 5)
        self.page.rate_stars(5, 5)
        self.page.wait_for_average(5, 1)
        self.assertTrue(self.page.average_stars.get_value() == '5')

    def test_float_average_of_stars(self):
        self.page.rate_stars(0, 4)
        self.page.rate_stars(1, 4)
        self.page.rate_stars(2, 4)
        self.page.rate_stars(3, 5)
        self.page.rate_stars(4, 5)
        self.page.rate_stars(5, 5)
        self.page.wait_for_average(4.5, 1)
        self.assertTrue(self.page.average_stars.get_value() == '4.5')

    def test_round_float_average_of_stars(self):
        self.page.rate_stars(0, 3)
        self.page.rate_stars(1, 4)
        self.page.rate_stars(2, 5)
        self.page.rate_stars(3, 1)
        self.page.rate_stars(4, 4)
        self.page.rate_stars(5, 5)
        self.page.wait_for_average(3.7, 1)
        self.assertTrue(self.page.average_stars.get_value() == '3.7')

    def test_not_full_stars_average(self):
        self.page.rate_stars(2, 5)
        self.page.rate_stars(4, 4)
        self.page.wait_for_average(4.5, 1)
        self.assertTrue(self.page.average_stars.get_value() == '4.5')


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

    def test_min_total_symbols_count_in_text_area_fields(self):
        self.page.login()
        pass
