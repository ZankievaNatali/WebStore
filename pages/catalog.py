import logging

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from constants.catalog import CatalogConstants
from pages.base import BasePage
from pages.header import Header
from pages.registration_login_form import RegistrationLoginFormConstants
from pages.utils import log_wrapper, wait_until_ok, random_category, random_brand, catalog_product_categories, \
    catalog_product_brands, skip_on


class Catalog(BasePage):
    """Stores methods describes Catalog page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CatalogConstants
        self.header = Header(self.driver)
        self.registration = RegistrationLoginFormConstants
        self.log = logging.getLogger("[CatalogPage]")

    @log_wrapper
    def check_cart_quantity(self, xpath, value='1'):
        """Check cart quantity items"""
        if self.is_element_exist(xpath=xpath):
            assert self.get_element_value(xpath, 'value') == value
        else:
            self.wait_until_displayed(by=By.XPATH, xpath=xpath)
            assert self.get_element_value(xpath, 'value') == value

    @log_wrapper
    def fill_in_town_from_dropdown_menu(self, value):
        """Fill in town from dropdown list in order menu Registration form"""
        self.click(by=By.XPATH, xpath=self.const.CATALOG_ORDER_FORM_USER_TOWN_FIELD_XPATH)
        self.click(by=By.XPATH, xpath=f"{self.const.CATALOG_ORDER_FORM_TOWN_LIST_XPATH}{value}]")

    @wait_until_ok(timeout=3, period=0.5)
    @log_wrapper
    def fill_delivery_form(self, user):
        """Fill in delivery address field"""
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_DELIVERY_ADDRESS_XPATH, value=user.delivery_address)

    @wait_until_ok(timeout=2, period=0.25)
    @log_wrapper
    def choose_category_brand(self):
        """Choosing category and brand (if brand is exists)"""
        # Open Catalog form
        self.header.navigate_to_catalog()
        # Choose catalog category/brand
        """
        category could be manually selected to any of next values:
         "Електросамокати", "Гіроборди", "Гіроскутери", "Запчастини" 

        brands could be manually selected to any of next values:
         Електросамокати - "CROSSER", "SEGWAY", "CITY_RIDER", "KUGO", "SMALL_CHILD"
         Гіроборди       - "65_INCH", "8_INCH"
        """
        category = random_category()
        brand = random_brand(category)
        self.click(by=By.XPATH, xpath=catalog_product_categories(category))
        if brand:
            self.wait_until_displayed(by=By.XPATH, xpath=catalog_product_brands(brand)).click()

    @log_wrapper
    def verify_success_order(self):
        """Verify Order button state"""
        assert self.is_element_exist(
            xpath=self.const.CATALOG_ORDER_FORM_ENABLED_ORDER_BUTTON_XPATH), "Order button is Active and available to order"

    @log_wrapper
    def add_product_to_wish_list(self, quantity_of_products):
        """Add products to the Wish List"""

        for i in range(1, quantity_of_products+1):
            elements = self.driver.find_element(By.XPATH, f"{self.const.CATALOG_FORM_WISH_LIST_ITEMS_XPATH}//child::li[{i}]")
            self.move_mouse_on_element(elements)
            element = elements.find_element(By.XPATH, self.const.CATALOG_FORM_WISH_BUTTON_XPATH)
            element.click()

        from pages.wish_list import WishList
        return WishList(self.driver)

    @log_wrapper
    def add_product_to_cart(self):
        """Add products to the cart and verify if it's successful"""
        # Click Buy button
        self.click(by=By.XPATH, xpath=self.const.CATALOG_BUY_BUTTON_XPATH)
        # Check if quantity of items in cart > 0
        self.check_cart_quantity(xpath=self.const.CATALOG_CART_ITEM_QUANTITY_XPATH)

    @log_wrapper
    def remove_from_cart(self):
        """Remove products from the cart and verify if it's successful"""
        self.click(by=By.CSS_SELECTOR, xpath=self.const.CATALOG_CART_REMOVE_CSS_PATH)
        self.switch_to_alert()

    @wait_until_ok(timeout=1, period=0.5)
    @log_wrapper
    def verify_success_cart_empty(self):
        """Verify if shopping cart is empty"""
        assert self.compare_element_text(text='0', xpath=self.const.CATALOG_CART_QUANTITY_XPATH)

    @log_wrapper
    def verify_success_quick_order(self):
        """Verify Quick Order button state"""
        assert self.is_element_exist(
            xpath=self.const.CATALOG_ORDER_FORM_QUICK_ORDER_BUTTON_XPATH), "Order button is Active and available to order"

    @skip_on(NoSuchElementException, reason="Brand has no available products")
    @log_wrapper
    def choose_product_to_buy(self):
        """Choose a product to buy"""
        self.choose_category_brand()
        # Pick first product from the list (all available products always at the top of the list)
        if not self.is_element_exist(xpath=self.const.ELEMENT_HAS_BLOCK_BUY_XPATH):
            self.click(by=By.XPATH, xpath=self.const.CATALOG_FIRST_ITEM_XPATH)

    @log_wrapper
    def buy_via_order_form(self):
        """Buy using Order Form"""
        # Click Buy button and verify if quantity > 0
        self.add_product_to_cart()
        # Click set order button
        self.click(by=By.XPATH, xpath=self.const.CATALOG_SET_ORDER_BUTTON_XPATH)

    @log_wrapper
    def quick_buy_via_button(self, user):
        """Fill in all required fields for a quick order"""
        # Click Quick Order in the Order form
        self.click(by=By.XPATH, xpath=self.const.CATALOG_ORDER_FORM_QUIK_ORDER_FORM_BUTTON_XPATH)
        # Fill in random user
        self.fill_field(xpath=self.const.CATALOG_QUICK_ORDER_FORM_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.const.CATALOG_QUICK_ORDER_FORM_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.const.CATALOG_QUICK_ORDER_FORM_PHONE_XPATH, value=user.phone)

    @log_wrapper
    def quick_buy_via_order_form(self, user):
        """Fill in all required fields for a quick order"""
        # Click Quick Order in the Order form
        self.click(by=By.XPATH, xpath=self.const.CATALOG_ORDER_FORM_QUIK_ORDER_XPATH)
        # Fill in random user
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_QUICK_USER_XPATH, value=user.username)
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_QUICK_USER_PHONE_XPATH, value=user.phone)
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_QUICK_USER_EMAIL_XPATH, value=user.email)

    @log_wrapper
    def buy_as_new_user(self, user):
        """Fill in all required fields to purchasing as new user"""
        # Click New User in the Order form
        self.click(by=By.XPATH, xpath=self.const.CATALOG_ORDER_FORM_SET_NEW_USER_XPATH)
        # Fill in random user
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_NEW_USER_XPATH, value=user.username)
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_USER_PHONE_XPATH, value=user.phone)
        self.fill_in_town_from_dropdown_menu(value=user.town)
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_NEW_USER_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_DELIVERY_ADDRESS_XPATH, value=user.delivery_address)

    @log_wrapper
    def buy_as_registered_user(self, user):
        """Fill in all required fields to purchasing as registered user"""

        # Click Registered User in the Order form
        self.click(by=By.XPATH, xpath=self.const.CATALOG_ORDER_FORM_SET_REGISTERED_USER_XPATH)
        # Fill in registered user
        self.fill_field(xpath=self.registration.LOGIN_EMAIL_INPUT_XPATH, value=user.email)
        self.fill_field(xpath=self.registration.LOGIN_PASSWORD_INPUT_XPATH, value=user.password)
        # Click on SignIn button
        self.click(by=By.XPATH, xpath=self.const.CATALOG_ORDER_FORM_LOGIN_XPATH_XPATH)
        # Check and fill in all registration fields
        self.fill_field(xpath=self.const.CATALOG_ORDER_FORM_USER_PHONE_XPATH, value=user.phone)
        self.fill_in_town_from_dropdown_menu(value=user.town)
        self.fill_delivery_form(user)
