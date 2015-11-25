# coding: utf-8
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page_objects.catalog_page_object import CatalogPage


class AlphabeticalCatalogCheck(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        catalog_page = CatalogPage(self.driver)
        catalog_page.open()
        alphabetical_catalog = catalog_page.alphabetical_catalog
        self.letters = alphabetical_catalog.get_catalog_letter_elements()

    def tearDown(self):
        self.driver.quit()

    def test_visibility_of_tooltips_at_hover(self):
        for letter in self.letters:
            letter.hover()
            self.assertEquals(letter.get_visibility_of_tooltip(), u'visible')

    def test_positions_count(self):
        for letter in self.letters:
            self.assertGreater(letter.get_cars_count(), 0)
