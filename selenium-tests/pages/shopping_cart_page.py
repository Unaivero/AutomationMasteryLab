from selenium.webdriver.common.by import By
from .base_page import BasePage


class ShoppingCartPage(BasePage):
    """Page object for the shopping cart page"""
    
    # Locators
    CART_TITLE = (By.CSS_SELECTOR, "#cart_title")
    PRODUCT_ROWS = (By.CSS_SELECTOR, "#cart_summary tbody tr")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity_input")
    PRODUCT_TOTAL = (By.CSS_SELECTOR, ".cart_total .price")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".cart_quantity_delete")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".cart_navigation .standard-checkout")
    TOTAL_PRICE = (By.CSS_SELECTOR, "#total_price")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-warning")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_cart_items_count(self):
        """Get the number of items in the cart"""
        items = self.find_elements(self.PRODUCT_ROWS)
        return len(items)
    
    def get_product_names(self):
        """Get a list of product names in the cart"""
        products = self.find_elements(self.PRODUCT_NAME)
        return [product.text for product in products]
    
    def get_product_prices(self):
        """Get a list of product prices in the cart"""
        prices = self.find_elements(self.PRODUCT_PRICE)
        # Skip the first element as it's the header
        return [price.text for price in prices[1:]]
    
    def get_total_price(self):
        """Get the total price of the cart"""
        return self.get_text(self.TOTAL_PRICE)
    
    def update_quantity(self, index, quantity):
        """Update the quantity of a product by index"""
        quantity_inputs = self.find_elements(self.PRODUCT_QUANTITY)
        if 0 <= index < len(quantity_inputs):
            self.input_text((By.CSS_SELECTOR, f"#cart_summary tbody tr:nth-child({index+1}) .cart_quantity_input"), str(quantity))
            # Wait for the page to update
            self.driver.execute_script("arguments[0].blur();", quantity_inputs[index])
            return self
        else:
            raise IndexError(f"Product index {index} out of range. Only {len(quantity_inputs)} products found.")
    
    def remove_product(self, index=0):
        """Remove a product from the cart by index"""
        delete_buttons = self.find_elements(self.DELETE_BUTTON)
        if 0 <= index < len(delete_buttons):
            delete_buttons[index].click()
            # Wait for the cart to update
            self.wait_for_element_to_disappear((By.CSS_SELECTOR, f"#cart_summary tbody tr:nth-child({index+1})"))
            return self
        else:
            raise IndexError(f"Product index {index} out of range. Only {len(delete_buttons)} products found.")
    
    def proceed_to_checkout(self):
        """Proceed to checkout"""
        self.click_element(self.PROCEED_TO_CHECKOUT)
        # Return the next expected page (this would be the authentication page if not logged in)
        # or the address page if already logged in
        return self
    
    def is_cart_empty(self):
        """Check if the cart is empty"""
        return self.is_element_visible(self.EMPTY_CART_MESSAGE)
    
    def get_empty_cart_message(self):
        """Get the empty cart message"""
        if self.is_cart_empty():
            return self.get_text(self.EMPTY_CART_MESSAGE)
        return None
