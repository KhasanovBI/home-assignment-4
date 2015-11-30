from element import *
from locators import ReviewPageLocators
from page_objects.base_page_object import Page


class ReviewPage(Page):
    PATH = '/reviews/add_edit_review/'

    def __init__(self, driver):
        super(ReviewPage, self).__init__(driver)
        self.average_stars = BaseElement(ReviewPageLocators.AVERAGE_STARS, self)
        self.BMW_list_item = ClickableElement(ReviewPageLocators.BMW_LIST_ITEM, self)
        self.marka_box = ClickableElement(ReviewPageLocators.MARK_BOX, self)
        self.probeg_input = ProbegInput(ReviewPageLocators.MILEAGE_INPUT, self)
        self.problems_input = ReviewPageTextarea(ReviewPageLocators.PROBLEMS_INPUT, ReviewPageLocators.PROBLEMS_INPUT_WRAP, self)
        self.submit_btn = ClickableElement(ReviewPageLocators.SUBMIT_BTN, self)
        self.advant_input = ReviewPageTextarea(ReviewPageLocators.ADVANT_INPUT, ReviewPageLocators.ADVANT_INPUT_WRAP, self)
        self.common_input = ReviewPageTextarea(ReviewPageLocators.COMMON_INPUT, ReviewPageLocators.COMMON_INPUT_WRAP, self)
        self.invalid_list = BaseElement(ReviewPageLocators.INVALID_LIST, self)
        self.model_box = ClickableElement(ReviewPageLocators.MODEL_BOX, self)
        self.year_box = ClickableElement(ReviewPageLocators.YEAR_BOX, self)
        self.mod_box = ClickableElement(ReviewPageLocators.MOD_BOX, self)
        self.BMW_model_list_item = ClickableElement(ReviewPageLocators.BMW_MODEL_ITEM, self)
        self.BMW_mod_list_item = ClickableElement(ReviewPageLocators.BMW_MOD_ITEM, self)
        self.BMW_year_list_item = ClickableElement(ReviewPageLocators.BMW_YEAR_ITEM, self)
        self.invalid_form_msg = BaseElement(ReviewPageLocators.INVALID_FORM_MSG, self)
        self.success_msg = BaseElement(ReviewPageLocators.SUCCESS_MSG, self)

    def wait_for_average(self, average, timeout):
        WebDriverWait(self.driver, timeout).until(lambda d: self.average_stars.get_value() == str(average))

    def rate_stars(self, row, x):
        self.driver.find_elements_by_class_name('rate__line__mark_' + str(x))[row].click()

    def fill_car_fields(self):
        self.marka_box.click()
        self.BMW_list_item.click()
        self.model_box.click()
        self.BMW_model_list_item.click()
        self.year_box.click()
        self.BMW_year_list_item.click()
        self.mod_box.click()
        self.BMW_mod_list_item.click()
        self.probeg_input.send_keys('111')

    def rate_all_stars(self, x):
        self.rate_stars(1, x)
        self.rate_stars(2, x)
        self.rate_stars(3, x)
        self.rate_stars(4, x)
        self.rate_stars(5, x)
        self.rate_stars(0, x)


class ReviewPageTextarea(InputElement):
    def __init__(self, locator, wrap_locator, page):
        super(ReviewPageTextarea, self).__init__(locator, page)
        self.wrap_locator = wrap_locator

    def is_invalid(self):
        classs = self.wrap_locator.locate(self.driver).get_attribute('class')
        return classs.find('invalid') != -1


class ProbegInput(InputElement):
    def get_value(self):
        return self._get_element().get_attribute('value')
