from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class RegistrationPage(BasePage):
    """Page object for the registration page"""
    
    # Personal Information Locators
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    DOB_DAY = (By.ID, "days")
    DOB_MONTH = (By.ID, "months")
    DOB_YEAR = (By.ID, "years")
    
    # Address Locators
    ADDRESS_FIRST_NAME = (By.ID, "firstname")
    ADDRESS_LAST_NAME = (By.ID, "lastname")
    COMPANY = (By.ID, "company")
    ADDRESS_LINE1 = (By.ID, "address1")
    ADDRESS_LINE2 = (By.ID, "address2")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    POSTCODE = (By.ID, "postcode")
    COUNTRY = (By.ID, "id_country")
    ADDITIONAL_INFO = (By.ID, "other")
    HOME_PHONE = (By.ID, "phone")
    MOBILE_PHONE = (By.ID, "phone_mobile")
    ADDRESS_ALIAS = (By.ID, "alias")
    
    # Submit Button
    REGISTER_BUTTON = (By.ID, "submitAccount")
    
    # Error Messages
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_personal_information(self, gender, first_name, last_name, password, dob_day, dob_month, dob_year):
        """Fill in the personal information section"""
        if gender.lower() == "male":
            self.click_element(self.GENDER_MALE)
        else:
            self.click_element(self.GENDER_FEMALE)
        
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        # Email is usually pre-filled from the previous page
        self.input_text(self.PASSWORD, password)
        
        # Handle dropdowns for date of birth
        Select(self.find_element(self.DOB_DAY)).select_by_value(str(dob_day))
        Select(self.find_element(self.DOB_MONTH)).select_by_value(str(dob_month))
        Select(self.find_element(self.DOB_YEAR)).select_by_value(str(dob_year))
        
        return self
    
    def fill_address(self, address1, city, state, postcode, country, mobile_phone, alias):
        """Fill in the address section"""
        # First name and last name are usually pre-filled from personal information
        self.input_text(self.ADDRESS_LINE1, address1)
        self.input_text(self.CITY, city)
        
        # Handle dropdowns for state and country
        Select(self.find_element(self.STATE)).select_by_visible_text(state)
        Select(self.find_element(self.COUNTRY)).select_by_visible_text(country)
        
        self.input_text(self.POSTCODE, postcode)
        self.input_text(self.MOBILE_PHONE, mobile_phone)
        self.input_text(self.ADDRESS_ALIAS, alias)
        
        return self
    
    def submit_registration(self):
        """Submit the registration form"""
        self.click_element(self.REGISTER_BUTTON)
        
        # If registration is successful, we should be redirected to the account page
        from .my_account_page import MyAccountPage
        return MyAccountPage(self.driver)
    
    def get_error_message(self):
        """Get error message if registration fails"""
        return self.get_text(self.ERROR_MESSAGE)
