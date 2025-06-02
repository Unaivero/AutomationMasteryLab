from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Base page class that all page objects inherit from"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator):
        """Find an element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find elements with explicit wait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        """Click on an element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element
    
    def input_text(self, locator, text):
        """Input text into an element with explicit wait"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return element
    
    def get_text(self, locator):
        """Get text from an element with explicit wait"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=10):
        """Check if element is present in the DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Wait for an element to disappear"""
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def get_page_title(self):
        """Get the title of the current page"""
        return self.driver.title
    
    def get_current_url(self):
        """Get the URL of the current page"""
        return self.driver.current_url
    
    def refresh_page(self):
        """Refresh the current page"""
        self.driver.refresh()
    
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)
