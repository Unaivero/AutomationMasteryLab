from selenium.webdriver.common.by import By
from .base_page import BasePage


class MyAccountPage(BasePage):
    """Page object for the My Account page"""
    
    # Locators
    PAGE_HEADING = (By.CLASS_NAME, "page-heading")
    ACCOUNT_NAME = (By.CLASS_NAME, "account")
    SIGN_OUT_LINK = (By.CLASS_NAME, "logout")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@title='Orders']")
    MY_ADDRESSES_LINK = (By.XPATH, "//a[@title='Addresses']")
    PERSONAL_INFO_LINK = (By.XPATH, "//a[@title='Information']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_user_logged_in(self):
        """Check if user is logged in by verifying page elements"""
        return (self.is_element_visible(self.PAGE_HEADING) and 
                self.get_text(self.PAGE_HEADING) == "MY ACCOUNT" and
                self.is_element_visible(self.SIGN_OUT_LINK))
    
    def get_account_name(self):
        """Get the account name displayed on the page"""
        return self.get_text(self.ACCOUNT_NAME)
    
    def sign_out(self):
        """Sign out from the account"""
        self.click_element(self.SIGN_OUT_LINK)
        # Return to login page
        from .login_page import LoginPage
        return LoginPage(self.driver)
    
    def go_to_order_history(self):
        """Navigate to order history page"""
        self.click_element(self.ORDER_HISTORY_LINK)
        # Return the next expected page
        # This would be an OrderHistoryPage class if implemented
        return self
    
    def go_to_my_addresses(self):
        """Navigate to my addresses page"""
        self.click_element(self.MY_ADDRESSES_LINK)
        # Return the next expected page
        # This would be an AddressesPage class if implemented
        return self
    
    def go_to_personal_info(self):
        """Navigate to personal information page"""
        self.click_element(self.PERSONAL_INFO_LINK)
        # Return the next expected page
        # This would be a PersonalInfoPage class if implemented
        return self
