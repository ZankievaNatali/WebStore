import logging

from selenium.webdriver.common.by import By

from constants.registration_login_form import RegistrationLoginFormConstants
from pages.base import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class RegistrationLoginForm(BasePage):
    """Stores methods describes registration and login form"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = RegistrationLoginFormConstants
        self.header = Header(self.driver)
        self.log = logging.getLogger("[RegistrationLoginForm]")

    @log_wrapper
    def registration(self, user):
        """Sign up using provided values"""

        # Open Registration/Login form
        self.header.navigate_to_registration_login_form()
        # Click "Реєстрація" button
        self.click(by=By.XPATH, xpath=self.header.const.REGISTRATION_TAB_XPATH)
        # Fill in fields
        self.fill_field(xpath=self.const.REGISTRATION_USERNAME_INPUT_XPATH, value=user.username)
        self.fill_field(xpath=self.const.REGISTRATION_EMAIL_INPUT_XPATH, value=user.email)
        self.fill_field(xpath=self.const.REGISTRATION_PASSWORD_INPUT_XPATH, value=user.password)
        # Click on "Зареєструватись" button
        self.click(by=By.XPATH, xpath=self.const.BUTTON_REGISTRATION_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_wrapper
    def login(self, user):
        """Sign in using provided values"""
        # Open Registration/Login form
        self.header.navigate_to_registration_login_form()
        # Click "Вхід" button
        self.click(by=By.XPATH, xpath=self.header.const.LOGIN_TAB_XPATH)
        # Fill in fields
        self.fill_field(xpath=self.const.LOGIN_EMAIL_INPUT_XPATH, value=user.email)
        self.fill_field(xpath=self.const.LOGIN_PASSWORD_INPUT_XPATH, value=user.password)
        # Click on SignIn button
        self.click(by=By.XPATH, xpath=self.const.BUTTON_LOGIN_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)
