from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def wait_until_displayed(self, by, xpath):
        """Waits until element displayed and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.visibility_of_element_located(
                (by, xpath)
            )
        )

    def wait_until_clickable(self, by, xpath):
        """Waits until element clickable and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.element_to_be_clickable((by, xpath)))

    def is_element_exist(self, xpath):
        """Waits until element exist, else raise an exception"""
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def is_element_visible(self, xpath):
        """Waits until element exist, else raise an exception"""
        try:
            self.wait_until_displayed(by=By.XPATH, xpath=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def fill_field(self, xpath, value):
        """Fill field using provided value"""
        element = self.wait_until_clickable(by=By.XPATH, xpath=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, by, xpath):
        """Find and click on the element by providing xpath"""
        # self.wait_until_displayed(by=by, xpath=xpath).click()
        self.driver.find_element(by=by, value=xpath).click()

    def move_mouse_on_element(self, element):
        """Moves mouse on provided element"""
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def switch_to_alert(self):
        """Moves focus to Alert window"""
        self.waiter.until(
            method=expected_conditions.alert_is_present()
        )
        self.driver.switch_to.alert.accept()

    def get_element_value(self, xpath, value):
        """Get element attribute value"""
        if self.is_element_exist(xpath=xpath):
            element = self.driver.find_element(By.XPATH, xpath).get_attribute(value)
            return element

    def compare_element_text(self, text, xpath):
        """Compare element's text with provided text """
        element = self.wait_until_displayed(by=By.XPATH, xpath=xpath)
        return element.text == text
