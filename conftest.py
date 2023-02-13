import pytest as pytest

from pages.catalog import Catalog
from pages.registration_login_form import RegistrationLoginForm
from pages.wish_list import WishList
from pages.utils import create_driver
from pages.value import User


@pytest.fixture()
def driver(browser):
    """Create selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def registration_login_page(driver):
    """Create registration page object"""
    return RegistrationLoginForm(driver)


@pytest.fixture()
def catalog_page(driver):
    """Create start page object"""
    return Catalog(driver)


@pytest.fixture()
def wish_list_page(driver):
    """Create start page object"""
    return WishList(driver)


@pytest.fixture()
def empty_user():
    """Create an empty user"""
    return User()


@pytest.fixture()
def registered_user():
    """Create an empty user"""
    registered_user = User()
    registered_user.username = "testuser testuser"
    registered_user.email = "testuser@test.com"
    registered_user.password = "12345678"
    registered_user.phone = "672322874"
    registered_user.town = "'Київ'"
    return registered_user


@pytest.fixture()
def random_user(empty_user):
    """Create random user"""
    empty_user.fill_data()
    return empty_user
