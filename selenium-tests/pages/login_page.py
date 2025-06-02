from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page"""
    
    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    LOGIN_BUTTON = (By.ID, "SubmitLogin")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot your password?")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://automationpractice.com/index.php?controller=authentication"
    
    def open(self):
        """Open the login page"""
        self.driver.get(self.url)
        return self
    
    def login(self, email, password):
        """Login with the provided credentials"""
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        # Return the next expected page
        from .my_account_page import MyAccountPage
        return MyAccountPage(self.driver)
    
    def attempt_login(self, email, password):
        """Attempt to login but stay on the login page (for negative testing)"""
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        return self
    
    def get_error_message(self):
        """Get the error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def click_forgot_password(self):
        """Click on the forgot password link"""
        self.click_element(self.FORGOT_PASSWORD_LINK)
        # Return the next expected page
        # This would be a ForgotPasswordPage class if implemented
        return self
    
    def start_create_account(self, email):
        """Start the account creation process"""
        self.input_text(self.CREATE_ACCOUNT_EMAIL, email)
        self.click_element(self.CREATE_ACCOUNT_BUTTON)
        # Return the next expected page
        from .registration_page import RegistrationPage
        return RegistrationPage(self.driver)
