from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class SearchPage(BasePage):
    """Page object for the search functionality"""
    
    # Locators
    SEARCH_BOX = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".product_list .product-container")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price.product-price")
    NO_RESULTS_ALERT = (By.CSS_SELECTOR, ".alert.alert-warning")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def search_for_product(self, product_name):
        """Search for a product"""
        self.input_text(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BUTTON)
        return self
    
    def search_with_enter_key(self, product_name):
        """Search using the Enter key"""
        search_box = self.find_element(self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        return self
    
    def get_search_results_count(self):
        """Get the number of search results"""
        results = self.find_elements(self.SEARCH_RESULTS)
        return len(results)
    
    def get_product_names(self):
        """Get a list of product names from search results"""
        products = self.find_elements(self.PRODUCT_NAME)
        return [product.text for product in products]
    
    def get_product_prices(self):
        """Get a list of product prices from search results"""
        prices = self.find_elements(self.PRODUCT_PRICE)
        return [price.text for price in prices]
    
    def click_on_product(self, index=0):
        """Click on a product from search results by index"""
        products = self.find_elements(self.PRODUCT_NAME)
        if 0 <= index < len(products):
            products[index].click()
            # Return the next expected page
            from .product_page import ProductPage
            return ProductPage(self.driver)
        else:
            raise IndexError(f"Product index {index} out of range. Only {len(products)} products found.")
    
    def has_no_results(self):
        """Check if the search returned no results"""
        return self.is_element_visible(self.NO_RESULTS_ALERT)
    
    def get_no_results_message(self):
        """Get the no results message"""
        if self.has_no_results():
            return self.get_text(self.NO_RESULTS_ALERT)
        return None
