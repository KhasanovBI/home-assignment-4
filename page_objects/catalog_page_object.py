# coding=utf-8
from selenium.webdriver import ActionChains

from page_objects.base_page_object import Page, Component


class CatalogPage(Page):
    PATH = '/catalog/'

    @property
    def alphabetical_catalog(self):
        return AlphabeticalCatalog(self.driver)


class AlphabeticalCatalog(Component):
    CATALOG = '//table[@class="catalog-abc__table js-catalog_letters"]/tbody/tr'
    LETTER_IN_CATALOG_CLASS = 'catalog-abc__td'

    def __init__(self, driver):
        super(AlphabeticalCatalog, self).__init__(driver)
        self.element = self.driver.find_element_by_xpath(self.CATALOG)

    def get_catalog_letter_elements(self):
        raw_letters = self.element.find_elements_by_class_name(self.LETTER_IN_CATALOG_CLASS)
        letters = []
        for raw_letter in raw_letters:
            letters.append(Letter(raw_letter, self.driver))
        return letters


class Letter(Component):
    CAR = 'catalog-abc__dropdown__item'
    TOOLTIP = 'tooltip'

    def __init__(self, element, driver):
        super(Letter, self).__init__(driver)
        self.element = element

    def hover(self):
        _hover = ActionChains(self.driver).move_to_element(self.element)
        _hover.perform()

    def get_visibility_of_tooltip(self):
        tooltip = self.element.find_element_by_class_name(self.TOOLTIP)
        return tooltip.value_of_css_property('visibility')

    def get_cars_count(self):
        cars = self.element.find_elements_by_class_name(self.CAR)
        return len(cars)
