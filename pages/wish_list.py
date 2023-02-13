import logging

from selenium.webdriver.common.by import By

from constants.wish_list import WishListConstants
from pages.base import BasePage
from pages.header import Header
from pages.utils import log_wrapper, wait_until_ok


class WishList(BasePage):
    """Stores methods describes Wish List page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = WishListConstants
        self.header = Header(self.driver)
        self.log = logging.getLogger("[WishListPage]")

    @wait_until_ok(timeout=3, period=0.25)
    @log_wrapper
    def verify_products_in_wish_list(self, quantity_of_products):
        """Verify if the Wish List has the same number of products as it was selected """
        # Open wish list page
        self.wait_until_displayed(by=By.XPATH, xpath=self.header.const.WISH_LIST_XPATH).click()
        # Checking if the Wish List has previous added products. If yes this number will be
        # added to Verify step to prevent mismatch between quantity of recently added product and total number
        prev_quantity = self.wait_until_displayed(by=By.XPATH, xpath=self.const.WISH_LIST_XPATH).text
        if int(prev_quantity) != 0:
            quantity_of_products = int(prev_quantity)
        # Check if the Wish List has the same number of products as it was selected
        assert self.compare_element_text(text=str(quantity_of_products),
                                         xpath=self.const.WISH_LIST_XPATH)
        # Clear the Wish List
        self.wait_until_displayed(by=By.XPATH, xpath=self.const.WISH_LIST_CLEAR_LIST_BUTTON_XPATH).click()
        self.switch_to_alert()
