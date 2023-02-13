import asyncio
import datetime
import logging
import random
import string
from functools import wraps

import pytest
from selenium import webdriver
from constants.base import BaseConstants
from constants.catalog import CatalogConstants


def random_num():
    """Generates random number"""
    return str(random.randint(1111111, 9999999))


def random_str(length=3):
    """Generates random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.25):
    """Retries function until ok (or 5 seconds)"""
    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catching : {err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    asyncio.sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """Add logs for method based on the docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        # log.info(f"{func.__doc__}; Args: {args};")
        log.info(func.__doc__)
        return result

    return wrapper


def skip_on(exception, reason="Default reason"):
    # Func below is the real decorator and will receive the test function as param
    def decorator_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                # Try to run the test
                return f(*args, **kwargs)
            except exception:
                # If exception of given type happens
                # just swallow it and raise pytest.Skip with given reason
                pytest.skip(reason)

        return wrapper

    return decorator_func


def create_driver(browser):
    """Create driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH_CHROME)
    elif browser == BaseConstants.FIREFOX:
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unknown browser name : {browser}")
    driver.implicitly_wait(1)
    driver.get(BaseConstants.URL)
    return driver


def random_category():
    list_of_category = ["Електросамокати", "Гіроборди", "Гіроскутери", "Запчастини"]
    return str(random.choice(list_of_category))


def random_brand(category):
    if category == "Електросамокати":
        list_of_brands = ["CROSSER", "SEGWAY", "CITY_RIDER", "KUGO", "SMALL_CHILD"]
        return str(random.choice(list_of_brands))
    elif category == "Гіроборди":
        list_of_brands = ["65_INCH", "8_INCH"]
        return str(random.choice(list_of_brands))
    else:
        return ''


def catalog_product_categories(category):
    """Stores Catalog menu category"""
    if category == "Електросамокати":
        return CatalogConstants.PRODUCT_MENU_ELECTRIC_SCOOTERS_XPATH
    elif category == "Гіроборди":
        return CatalogConstants.PRODUCT_MENU_GIROBORDS_XPATH
    elif category == "Гіроскутери":
        return CatalogConstants.PRODUCT_MENU_GIROSCUTERS_XPATH
    elif category == "Запчастини":
        return CatalogConstants.PRODUCT_MENU_SPAREPARTS_XPATH
    elif category == "Акції":
        return CatalogConstants.PRODUCT_MENU_SPECIALS_XPATH


def catalog_product_brands(brand):
    """Stores Catalog menu category"""
    if brand == "CROSSER":
        return CatalogConstants.ELECTRIC_SCOOTER_BRAND_CROSSER_XPATH
    elif brand == "SEGWAY":
        return CatalogConstants.ELECTRIC_SCOOTER_BRAND_SEGWAY_XPATH
    elif brand == "CITY_RIDER":
        return CatalogConstants.ELECTRIC_SCOOTER_BRAND_CITY_RIDER_XPATH
    elif brand == "KUGO":
        return CatalogConstants.ELECTRIC_SCOOTER_BRAND_KUGO_XPATH
    elif brand == "SMALL_CHILD":
        return CatalogConstants.ELECTRIC_SCOOTER_BRAND_SMALL_CHILD_XPATH
    elif brand == "65_INCH":
        return CatalogConstants.GIROBORDS_TYPES_65_INCH_XPATH
    elif brand == "8_INCH":
        return CatalogConstants.GIROBORDS_TYPES_8_INCH_XPATH
