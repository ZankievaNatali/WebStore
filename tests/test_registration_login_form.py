import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestRegistrationLoginForm:
    """Stores tests for registration and login form"""

    def test_valid_registration(self, registration_login_page, random_user):
        """
        - Pre-condition:
            -Open start page
            -Click "Вхід" button
        -Steps:
            -Fill username
            -Fill email address
            -Fill Password
            -Click on "Зареєструватись" button
            -Verify if start page header has the name of registered user instead of button "Вхід"
        """
        # Fill in username, email, password
        start_page = registration_login_page.registration(random_user)
        # Verify transfer to Hello page
        start_page.verify_success_sign_in(username=random_user.username)

    def test_valid_login(self, registration_login_page, registered_user):
        """
        - Pre-condition:
            -Open start page
            -Click "Вхід" button
        -Steps:
            -Fill email address
            -Fill Password
            -Click on "Вхід" button
            -Verify if start page header has the name of registered user instead of button "Вхід"
        """
        # Fill in email, password
        start_page = registration_login_page.login(registered_user)
        # Verify transfer to Start page
        start_page.verify_success_sign_in(username=registered_user.username)
