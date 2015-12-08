from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from element import *
from locators import ReviewPageLocators, DriverLocator, BaseLocator
from page_objects.base_page_object import Page


class ReviewPage(Page):
    PATH = '/reviews/add_edit_review/'

    def __init__(self, driver):
        super(ReviewPage, self).__init__(driver)
        self.average_stars = BaseElement(ReviewPageLocators.AVERAGE_STARS, self)

        self.probeg_input = MileageInput(ReviewPageLocators.MILEAGE_INPUT, self)
        self.problems_input = ReviewPageTextarea(ReviewPageLocators.PROBLEMS_INPUT, ReviewPageLocators.PROBLEMS_INPUT_WRAP, self)
        self.submit_btn = ClickableElement(ReviewPageLocators.SUBMIT_BTN, self)
        self.advant_input = ReviewPageTextarea(ReviewPageLocators.ADVANT_INPUT, ReviewPageLocators.ADVANT_INPUT_WRAP, self)
        self.common_input = ReviewPageTextarea(ReviewPageLocators.COMMON_INPUT, ReviewPageLocators.COMMON_INPUT_WRAP, self)
        self.invalid_list = BaseElement(ReviewPageLocators.INVALID_LIST, self)
        self.marka_box = ComboboxElement(ReviewPageLocators.MARK_BOX, self)
        self.model_box = ComboboxElement(ReviewPageLocators.MODEL_BOX, self)
        self.year_box = ComboboxElement(ReviewPageLocators.YEAR_BOX, self)
        self.mod_box = ComboboxElement(ReviewPageLocators.MOD_BOX, self)
        self.body_box = ComboboxElement(ReviewPageLocators.BODY_BOX, self)
        self.kpp_box = ComboboxElement(ReviewPageLocators.KPP_BOX, self)
        self.privod_box = ComboboxElement(ReviewPageLocators.PRIVOD_BOX, self)
        self.gas_volume_box = ComboboxElement(ReviewPageLocators.GAS_VOLUME_BOX, self)
        self.invalid_form_msg = BaseElement(ReviewPageLocators.INVALID_FORM_MSG, self)
        self.success_msg = BaseElement(ReviewPageLocators.SUCCESS_MSG, self)

    def wait_for_average(self, average, timeout):
        WebDriverWait(self.driver, timeout).until(lambda d: self.average_stars.get_value() == str(average))

    def rate_stars(self, row, x):
        self.driver.find_elements_by_class_name('rate__line__mark_' + str(x))[row].click()

    def fill_car_fields(self):
        self.marka_box.select_option()
        self.model_box.select_option()
        self.year_box.select_option()
        self.mod_box.select_option()
        self.probeg_input.send_keys('111')

    def rate_all_stars(self, x):
        self.rate_stars(1, x)
        self.rate_stars(2, x)
        self.rate_stars(3, x)
        self.rate_stars(4, x)
        self.rate_stars(5, x)
        self.rate_stars(0, x)


class ComboboxElement(ClickableElement):
    class OptionLocator(BaseLocator):
        def __init__(self, box):
            self.box = box

        def locate(self, driver):
            return self.box._get_element().find_element_by_xpath('.//*[@data-optidx="1"]')

    def __init__(self, locator, page):
        super(ComboboxElement, self).__init__(locator, page)
        self.option = ClickableElement(self.OptionLocator(self), page)

    def expand_list(self, d):
        self.click()
        return self.option.locator.locate(d)

    def select_option(self):

        WebDriverWait(self.driver, 5).until(lambda d: self.expand_list(d))
        self.option.click()

        # WebDriverWait(self.driver, 5).until(
        #     lambda d: EC.visibility_of(self._get_element().find_element_by_xpath('.//*[@data-optidx="1"]'))
        # )
        # self._get_element().find_element_by_xpath('.//*[@data-optidx="1"]').click()

    def enabled_is(self, expected):
        inner_div = self._get_element().find_element_by_xpath('.//*[contains(@class,"input__box_select")]')
        try:
            WebDriverWait(self.driver, 5).until(
                lambda d: (inner_div.get_attribute('class').find('input__box_disabled') == -1) == expected
            )
            return True
        except TimeoutException:
            return False


class ReviewPageTextarea(InputElement):
    def __init__(self, locator, wrap_locator, page):
        super(ReviewPageTextarea, self).__init__(locator, page)
        self.wrap_locator = wrap_locator

    def is_invalid(self):
        classs = self.wrap_locator.locate(self.driver).get_attribute('class')
        return classs.find('invalid') != -1


class MileageInput(InputElement):
    def get_value(self):
        return self._get_element().get_attribute('value')
