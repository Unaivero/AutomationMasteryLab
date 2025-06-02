import pytest
import allure
from ..pages.login_page import LoginPage
from ..utils.test_data import TestData
from .base_test import BaseTest


@allure.feature("Authentication")
class TestLogin(BaseTest):
    """Test cases for the login functionality"""
    
    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        """Test successful login with valid credentials"""
        # Use your test account credentials here
        email = "test.user@example.com"  # Replace with a valid email
        password = "Password123"  # Replace with a valid password
        
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Perform login
        my_account_page = login_page.login(email, password)
        
        # Verify successful login
        assert my_account_page.is_user_logged_in(), "Login failed"
        
        # Verify account name contains the expected text
        account_name = my_account_page.get_account_name()
        assert "Test User" in account_name, f"Account name '{account_name}' does not contain expected text"
    
    @allure.story("Failed Login")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("credentials", TestData.invalid_credentials())
    def test_failed_login(self, credentials):
        """Test failed login with invalid credentials"""
        email = credentials["email"]
        password = credentials["password"]
        
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Attempt login with invalid credentials
        login_page.attempt_login(email, password)
        
        # Verify error message is displayed
        assert login_page.is_element_visible(login_page.ERROR_MESSAGE), "Error message not displayed"
        
        # Verify we're still on the login page
        assert "authentication" in login_page.get_current_url(), "Not on login page after failed login"
    
    @allure.story("Logout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout(self):
        """Test logout functionality"""
        # Use your test account credentials here
        email = "test.user@example.com"  # Replace with a valid email
        password = "Password123"  # Replace with a valid password
        
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Perform login
        my_account_page = login_page.login(email, password)
        
        # Verify successful login
        assert my_account_page.is_user_logged_in(), "Login failed"
        
        # Perform logout
        login_page = my_account_page.sign_out()
        
        # Verify we're back on the login page
        assert "authentication" in login_page.get_current_url(), "Not redirected to login page after logout"
