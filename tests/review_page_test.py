# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver import Firefox
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
        self.page.probeg_input.send_keys("-123a4#8")
        self.assertEquals(self.page.probeg_input.get_value(), "12 348")

    def test_invalid_text_fields(self):
        self.page.login()
        self.page.problems_input.send_keys("lalala")
        self.page.submit_btn.click()
        self.assertTrue(self.page.common_input.is_invalid())
        self.assertTrue(self.page.advant_input.is_invalid())
        self.assertFalse(self.page.problems_input.is_invalid())
        self.assertTrue(self.page.invalid_list.get_value().find(u'достоинства') != -1)
        self.assertTrue(self.page.invalid_list.get_value().find(u'общее впечатление') != -1)

    def test_min_total_symbols_count_in_text_area_fields(self):
        self.page.login()
        self.page.fill_car_fields()
        self.page.rate_all_stars(5)
        self.page.common_input.send_keys("q"*100)
        self.page.problems_input.send_keys("q"*50)
        self.page.advant_input.send_keys("q"*49)
        self.page.submit_btn.click()
        self.assertTrue(self.page.invalid_form_msg.get_value().find(u'не менее 200 знаков') != -1)
        self.page.advant_input.send_keys("q")
        self.page.submit_btn.click()
        self.assertTrue(self.page.success_msg.is_present())

    def test_mod_field_fills_rest(self):
        self.page.login()
        self.page.marka_box.click()
        self.page.BMW_list_item.click()
        self.page.model_box.click()
        self.page.BMW_model_list_item.click()
        self.page.year_box.click()
        self.page.BMW_year_list_item.click()
        self.page.submit_btn.click()
        invalid_msg = self.page.invalid_list.get_value()
        self.assertTrue(invalid_msg.find(u'кузов') != -1)
        self.assertTrue(invalid_msg.find(u'объем двигателя') != -1)
        self.assertTrue(invalid_msg.find(u'кпп') != -1)
        self.assertTrue(invalid_msg.find(u'привод') != -1)
        self.page.mod_box.click()
        self.page.BMW_mod_list_item.click()
        self.page.submit_btn.click()
        invalid_msg = self.page.invalid_list.get_value()
        self.assertTrue(invalid_msg.find(u'кузов') == -1)
        self.assertTrue(invalid_msg.find(u'объем двигателя') == -1)
        self.assertTrue(invalid_msg.find(u'кпп') == -1)
        self.assertTrue(invalid_msg.find(u'привод') == -1)

