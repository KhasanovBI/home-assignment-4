# coding=utf-8
from selenium.webdriver.common.by import By


class BaseLocator:
    def locate(self, driver):
        pass


class DriverLocator(BaseLocator):
    def __init__(self, locator):
        self.locator = locator

    def locate(self, driver):
        return driver.find_element(*self.locator)


class MainPageLocators:
    USERNAME_FIELD = DriverLocator((By.ID, 'ph_login'))
    PASSWORD_FIELD = DriverLocator((By.ID, 'ph_password'))
    LOGIN_BUTTON = DriverLocator((By.ID, 'PH_authLink'))
    USER_EMAIL_HREF = DriverLocator((By.ID, "PH_user-email"))
    LOGOUT_BUTTON = DriverLocator((By.ID, "PH_logoutLink"))


class BuyPageLocators:
    PRICE_SORT_BTN = DriverLocator((By.XPATH, "//span[contains(@class, 'sort__pin__name') and text() = 'цене']"))
    REGION_SELECT_BTN = DriverLocator((By.CLASS_NAME, "js-geo_name"))
    REGION_INPUT = DriverLocator((By.XPATH, "//input[contains(@placeholder, 'Введите название города или региона')]"))
    CITY_ITEM = DriverLocator(
        (By.XPATH, '//div[contains(@class, "input__data__value") and contains(@class, "js-field_item")]'))
    APPLY_FILTER = DriverLocator((By.CLASS_NAME, 'tooltip__go__link'))
    SUBMIT_REGION = DriverLocator((By.CLASS_NAME, 'js-control_submit'))


class ReviewPageLocators:
    AVERAGE_STARS = DriverLocator((By.CLASS_NAME, 'js-average_score_val'))
    BMW_LIST_ITEM = DriverLocator((By.XPATH, '//div[contains(@class, "js-select__options__item") and text()="BMW"]'))
    MARKA_BOX = DriverLocator((By.XPATH, '//div[@data-title="Марка"]'))
    PROBEG_INPUT = DriverLocator((By.XPATH, '//input[@placeholder="Пробег"][2]'))
    ADVANT_INPUT_WRAP = DriverLocator((By.XPATH, '//div[@data-title="Достоинства"]'))
    ADVANT_INPUT = DriverLocator((By.XPATH, '//textarea[@name="advantages_text"]'))
    PROBLEMS_INPUT_WRAP = DriverLocator((By.XPATH, '//div[@data-title="Недостатки"]'))
    PROBLEMS_INPUT = DriverLocator((By.XPATH, '//textarea[@name="problems_text"]'))
    COMMON_INPUT_WRAP = DriverLocator((By.XPATH, '//div[@data-title="Общее впечатление"]'))
    COMMON_INPUT = DriverLocator((By.XPATH, '//textarea[@name="common_text"]'))
    SUBMIT_BTN = DriverLocator((By.XPATH, '//div[@class="car__submit"]//button[@type="submit"]'))
    INVALID_LIST = DriverLocator((By.CLASS_NAME, 'car-add__error__validate'))


class StarLocator(BaseLocator):
    def __init__(self, line_id, star_id):
        self.line_id = line_id
        self.star_id = star_id

    def locate(self, driver):
        return driver.find_elements_by_class_name('rate__line__mark_' + str(self.star_id))[self.line_id]
