import pytest
import allure
from ..pages.login_page import LoginPage
from ..utils.test_data import TestData
from .base_test import BaseTest


@allure.feature("Registration")
class TestRegistration(BaseTest):
    """Test cases for the registration functionality"""
    
    @allure.story("Successful Registration")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(self):
        """Test successful registration with valid data"""
        # Generate random test data
        email = TestData.random_email()
        password = TestData.random_password()
        first_name, last_name = TestData.random_name()
        dob = TestData.random_date_of_birth()
        address = TestData.random_address()
        
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Start account creation
        registration_page = login_page.start_create_account(email)
        
        # Fill personal information
        registration_page.fill_personal_information(
            gender="male",
            first_name=first_name,
            last_name=last_name,
            password=password,
            dob_day=dob['day'],
            dob_month=dob['month'],
            dob_year=dob['year']
        )
        
        # Fill address information
        registration_page.fill_address(
            address1=address['address1'],
            city=address['city'],
            state=address['state'],
            postcode=address['postcode'],
            country=address['country'],
            mobile_phone=address['mobile_phone'],
            alias=address['alias']
        )
        
        # Submit registration
        my_account_page = registration_page.submit_registration()
        
        # Verify successful registration
        assert my_account_page.is_user_logged_in(), "Registration failed"
        
        # Verify account name contains the expected text
        account_name = my_account_page.get_account_name()
        assert f"{first_name} {last_name}" in account_name, f"Account name '{account_name}' does not contain expected text"
    
    @allure.story("Registration Validation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registration_validation_empty_fields(self):
        """Test registration validation with empty required fields"""
        email = TestData.random_email()
        
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Start account creation
        registration_page = login_page.start_create_account(email)
        
        # Submit registration without filling any fields
        registration_page.click_element(registration_page.REGISTER_BUTTON)
        
        # Verify error message is displayed
        assert registration_page.is_element_visible(registration_page.ERROR_MESSAGE), "Error message not displayed"
        
        # Get error message text
        error_message = registration_page.get_error_message()
        assert "error" in error_message.lower(), f"Error message '{error_message}' does not contain expected text"
    
    @allure.story("Registration Validation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registration_validation_invalid_email(self):
        """Test registration with invalid email format"""
        invalid_email = "invalid-email"
        
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Try to start account creation with invalid email
        login_page.input_text(login_page.CREATE_ACCOUNT_EMAIL, invalid_email)
        login_page.click_element(login_page.CREATE_ACCOUNT_BUTTON)
        
        # Wait for error message
        assert login_page.is_element_visible(login_page.ERROR_MESSAGE), "Error message not displayed"
        
        # Get error message text
        error_message = login_page.get_error_message()
        assert "invalid" in error_message.lower(), f"Error message '{error_message}' does not contain expected text"
