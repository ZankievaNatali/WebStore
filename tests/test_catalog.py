import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])  # also adapted for Firefox , BaseConstants.FIREFOX
class TestCatalog:
    """Stores tests for Catalog page"""

    def test_cart_as_registered_user(self, catalog_page, registered_user):
        """
                - Pre-condition:
                    -Open start page
                    -Click Catalog button
                -Steps:
                    -Choose one of Catalog Category
                    -Choose the item
                    -Click Buy button
                    -Click Checkout button
                    -Choose option Registered buyer at the top of Checkout window
                    -Fill in missed credentials
                    -Check if the Offer button is enabled
        """
        # Choosing a product to buy
        catalog_page.choose_product_to_buy()
        # Adding product to a shopping cart
        catalog_page.buy_via_order_form()
        # Filling in all required fields in Order Form as a registered user
        catalog_page.buy_as_registered_user(registered_user)
        # Verifying if order button is enabled
        catalog_page.verify_success_order()

    def test_cart_as_unregistered_user(self, catalog_page, random_user):
        """
                - Pre-condition:
                    -Open start page
                    -Click Catalog button
                -Steps:
                    -Choose one of Catalog Category
                    -Choose the item
                    -Click Buy button
                    -Click Checkout button
                    -Choose option New buyer at the top of Checkout window
                    -Fill in missed credentials
                    -Check if the Offer button is enabled
        """
        # Choosing a product to buy
        catalog_page.choose_product_to_buy()
        # Adding product to a shopping cart
        catalog_page.buy_via_order_form()
        # Filling in all required fields in Order Form as a new user
        catalog_page.buy_as_new_user(random_user)
        # Verifying if order button is enabled
        catalog_page.verify_success_order()

    def test_cart_quick_order_via_order_form(self, catalog_page, random_user):
        """
                - Pre-condition:
                    -Open start page
                    -Click Catalog button
                -Steps:
                    -Choose one of Catalog Category
                    -Choose the item
                    -Click Buy button
                    -Click Checkout button
                    -Choose option Quick Buy at the top of Checkout window
                    -Fill in missed credentials
                    -Check if the Offer button is enabled
        """
        # Choosing a product to buy
        catalog_page.choose_product_to_buy()
        # Adding product to a shopping cart
        catalog_page.buy_via_order_form()
        # Filling in all required fields in Order Form as a new user
        catalog_page.quick_buy_via_order_form(random_user)
        # Verifying if order button is enabled
        catalog_page.verify_success_quick_order()

    def test_cart_quick_order_via_button(self, catalog_page, random_user):
        """
                - Pre-condition:
                    -Open start page
                    -Click Catalog button
                -Steps:
                    -Choose one of Catalog Category
                    -Choose the item
                    -Click Quick Buy button
                    -Fill in missed credentials
                    -Check if the Offer button is enabled
        """
        # Choosing a product to buy
        catalog_page.choose_product_to_buy()
        # Filling in all required fields in Quick buy form
        catalog_page.quick_buy_via_button(random_user)
        # Verifying if order button is enabled
        catalog_page.verify_success_quick_order()

    def test_cart_remove_product(self, catalog_page):
        """
                - Pre-condition:
                    -Open start page
                    -Click Catalog button
                -Steps:
                    -Choose one of Catalog Category
                    -Choose the item
                    -Click Buy button
                    -Verify if cart has one unit of product
                    -Remove product from cart
                    -Verify if cart is empty
        """
        # Choosing a product to buy
        catalog_page.choose_product_to_buy()
        # Add and verify if the product is added to the cart
        catalog_page.add_product_to_cart()
        # Remove products from the cart
        catalog_page.remove_from_cart()
        # Verify if shopping cart is empty
        catalog_page.verify_success_cart_empty()

    def test_wish_list_products(self, catalog_page, registration_login_page, registered_user):
        """
                - Pre-condition:
                    -Open start page
                    -Log in as a registered user
                    -Click Catalog button
                -Steps:
                    -Choose one of Catalog Category
                    -Click heart icon to add any product/products to the wish list
                    -Open Wish List
                    -Check if the Wish List has all products that you added
        """
        # Log in as a registered user
        registration_login_page.login(registered_user)
        # Choose random category and brand
        catalog_page.choose_category_brand()
        # Add one or more products to your wish list
        quantity_of_wish_products = 2
        wish_list = catalog_page.add_product_to_wish_list(quantity_of_wish_products)
        # Verify if the Wish List has all products that you added
        wish_list.verify_products_in_wish_list(quantity_of_wish_products)
