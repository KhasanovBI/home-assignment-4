# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote, Firefox, Chrome
from selenium.webdriver.chrome import webdriver

from page_objects.buy_page_object import BuyPage


class BuyPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.driver.get("https://cars.mail.ru/sale/msk/all/")

    def tearDown(self):
        self.driver.quit()

    def test_price_sort(self):
        page = BuyPage(self.driver)
        page.price_sort_btn.click()

        cards = page.read_cards()
        prices = [x.price for x in cards]
        for i in range(0, len(prices) - 1):
            self.assertTrue(prices[i] <= prices[i + 1])

    def test_region(self):
        page = BuyPage(self.driver)
        page.region_btn.click()
        page.region_input.send_keys(u'Казань')
        page.city_first_result.click()
        page.submit_region_btn.click()
        page.apply_filter_lnk.click()
        cards = page.read_cards()
        for x in cards:
            self.assertTrue(x.region == u'Казань')
