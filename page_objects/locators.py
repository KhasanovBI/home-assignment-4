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
