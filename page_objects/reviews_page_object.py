# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page_object import Page, Component


class ReviewsPage(Page):
    PATH = '/reviews/'

    @property
    def add_review_button(self):
        return AddReviewButton(self.driver)

    @property
    def login_form(self):
        return LoginForm(self.driver)


class AddReviewButton(Component):
    ADD_REVIEW_BUTTON = '//a[@href="/reviews/add_edit_review/"]'

    def __init__(self, driver):
        super(AddReviewButton, self).__init__(driver)
        self.element = self.driver.find_element_by_xpath(self.ADD_REVIEW_BUTTON)

    def click(self):
        self.element.click()

    def wait_visibility(self):
        WebDriverWait(self.driver, 5).until(
            lambda driver: EC.visibility_of_element_located(driver.find_element_by_xpath(self.element))
        )


class LoginForm(Component):
    USERNAME_FIELD = '//*[@id="ph_login"]'
    PASSWORD_FIELD = '//*[@id="ph_password"]'
    LOGIN_BUTTON = '//*[@class="x-ph__button__input"]'

    def wait_popup(self):
        WebDriverWait(self.driver, 5).until(
            lambda driver: EC.visibility_of_element_located(driver.find_element_by_xpath(self.LOGIN_BUTTON))
        )
        WebDriverWait(self.driver, 5).until(
            lambda driver: EC.visibility_of_element_located(driver.find_element_by_xpath(self.USERNAME_FIELD))
        )
        WebDriverWait(self.driver, 5).until(
            lambda driver: EC.visibility_of_element_located(driver.find_element_by_xpath(self.PASSWORD_FIELD))
        )

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.USERNAME_FIELD).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_FIELD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
