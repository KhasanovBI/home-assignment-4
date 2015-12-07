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


class DriverLocatorMany(DriverLocator):
    def locate(self, driver):
        return driver.find_elements(*self.locator)


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
    OFFER_CARDS = DriverLocatorMany((By.XPATH, '//div[contains(@class, "offer-card js-offer")]'))

    class OfferCardPriceLocator(BaseLocator):
        def __init__(self, card_locator):
            self.card_locator = card_locator

        def locate(self, driver):
            return self.card_locator.locate(driver).find_element_by_class_name('offer-card__price__value')

    class OfferCardLocator(BaseLocator):
        def __init__(self, id):
            self.id = id

        def locate(self, driver):
            return driver.find_element_by_xpath(
                "(//div[@class='offer-card offer-card_fst js-offer' or @class='offer-card js-offer'])[%d]" % (self.id + 1,))


class ReviewPageLocators:
    AVERAGE_STARS = DriverLocator((By.CLASS_NAME, 'js-average_score_val'))
    # BMW_LIST_ITEM = DriverLocator((By.XPATH, '//div[contains(@class, "js-select__options__item") and text()="BMW"]'))
    # BMW_MODEL_ITEM = DriverLocator((By.XPATH, '//div[contains(@class, "js-select__options__item") and text()="1"]'))
    # BMW_YEAR_ITEM = DriverLocator((By.XPATH, '//div[contains(@class, "js-select__options__item") and text()="2015"]'))
    # BMW_MOD_ITEM = DriverLocator((By.XPATH, '//div[contains(@class, "js-select__options__item") and text()="1.5D AT"]'))
    MARK_BOX = DriverLocator((By.XPATH, '//div[@data-title="Марка"]'))
    MODEL_BOX = DriverLocator((By.XPATH, '//div[@data-title="Модель"]'))
    YEAR_BOX = DriverLocator((By.XPATH, '//div[@data-title="Год производства"]'))
    MOD_BOX = DriverLocator((By.XPATH, '//div[@data-title="Модификация"]'))
    BODY_BOX = DriverLocator((By.XPATH, '//div[@data-title="Кузов"]'))
    GAS_VOLUME_BOX = DriverLocator((By.XPATH, '//div[@data-title="Объем двигателя"]'))
    KPP_BOX = DriverLocator((By.XPATH, '//div[@data-title="КПП"]'))
    PRIVOD_BOX = DriverLocator((By.XPATH, '//div[@data-title="Привод"]'))
    MILEAGE_INPUT = DriverLocator((By.XPATH, '//input[@placeholder="Пробег"][2]'))
    ADVANT_INPUT_WRAP = DriverLocator((By.XPATH, '//div[@data-title="Достоинства"]'))
    ADVANT_INPUT = DriverLocator((By.XPATH, '//textarea[@name="advantages_text"]'))
    PROBLEMS_INPUT_WRAP = DriverLocator((By.XPATH, '//div[@data-title="Недостатки"]'))
    PROBLEMS_INPUT = DriverLocator((By.XPATH, '//textarea[@name="problems_text"]'))
    COMMON_INPUT_WRAP = DriverLocator((By.XPATH, '//div[@data-title="Общее впечатление"]'))
    COMMON_INPUT = DriverLocator((By.XPATH, '//textarea[@name="common_text"]'))
    SUBMIT_BTN = DriverLocator((By.XPATH, '//div[@class="car__submit"]//button[@type="submit"]'))
    INVALID_LIST = DriverLocator((By.CLASS_NAME, 'car-add__error__validate'))
    INVALID_FORM_MSG = DriverLocator((By.CLASS_NAME, 'car-add__error__form'))
    SUCCESS_MSG = DriverLocator((By.CLASS_NAME, 'car-add__done'))


class StarLocator(BaseLocator):
    def __init__(self, line_id, star_id):
        self.line_id = line_id
        self.star_id = star_id

    def locate(self, driver):
        return driver.find_elements_by_class_name('rate__line__mark_%d' % self.star_id)[self.line_id]
