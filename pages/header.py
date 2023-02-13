from selenium.webdriver.common.by import By

from constants.header import HeaderConstants
from pages.base import BasePage
from pages.utils import log_wrapper, wait_until_ok


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConstants

    @log_wrapper
    def navigate_to_registration_login_form(self):
        """Navigate to LOG IN/REGISTRATION form """
        self.click(by=By.XPATH, xpath=self.const.SIGN_IN_BUTTON_XPATH)

        from pages.registration_login_form import RegistrationLoginForm
        return RegistrationLoginForm(self.driver)

    @wait_until_ok(timeout=3, period=0.5)
    @log_wrapper
    def navigate_to_catalog(self):
        """Navigate to Catalog form via Catalog button"""
        # Click on Profile button
        if self.is_element_visible(xpath=self.const.CATALOG_XPATH):
            self.click(by=By.XPATH, xpath=self.const.CATALOG_XPATH)

        from pages.catalog import Catalog
        return Catalog(self.driver)
