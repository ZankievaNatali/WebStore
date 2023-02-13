import logging

from constants.start_page import StartPageConstants
from pages.base import BasePage
from pages.header import Header
from pages.utils import log_wrapper, wait_until_ok


class StartPage(BasePage):
    """Stores methods describes Start page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConstants
        self.header = Header(self.driver)
        self.log = logging.getLogger("[StartPage]")

    @log_wrapper
    @wait_until_ok(timeout=3, period=0.5)
    def verify_success_sign_in(self, username):
        """Verify sign in username"""
        assert self.compare_element_text(xpath=self.const.USER_LOGIN_NAME_XPATH, text=username)
