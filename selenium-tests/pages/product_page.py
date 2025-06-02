from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class ProductPage(BasePage):
    """Page object for the product details page"""
    
    # Locators
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1[itemprop='name']")
    PRODUCT_PRICE = (By.ID, "our_price_display")
    QUANTITY_INPUT = (By.ID, "quantity_wanted")
    SIZE_DROPDOWN = (By.ID, "group_1")
    COLOR_OPTIONS = (By.CSS_SELECTOR, ".attribute_list #color_to_pick_list a")
    ADD_TO_CART_BUTTON = (By.ID, "add_to_cart")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".button-medium[title='Proceed to checkout']")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, ".continue.btn")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".layer_cart_product h2")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_product_name(self):
        """Get the product name"""
        return self.get_text(self.PRODUCT_NAME)
    
    def get_product_price(self):
        """Get the product price"""
        return self.get_text(self.PRODUCT_PRICE)
    
    def set_quantity(self, quantity):
        """Set the product quantity"""
        self.input_text(self.QUANTITY_INPUT, str(quantity))
        return self
    
    def select_size(self, size_text):
        """Select a size from the dropdown"""
        size_select = Select(self.find_element(self.SIZE_DROPDOWN))
        size_select.select_by_visible_text(size_text)
        return self
    
    def select_color(self, color_index=0):
        """Select a color by index"""
        colors = self.find_elements(self.COLOR_OPTIONS)
        if 0 <= color_index < len(colors):
            colors[color_index].click()
        else:
            raise IndexError(f"Color index {color_index} out of range. Only {len(colors)} colors available.")
        return self
    
    def add_to_cart(self):
        """Add the product to cart"""
        self.click_element(self.ADD_TO_CART_BUTTON)
        # Wait for the success message to appear
        self.wait.until(lambda d: self.is_element_visible(self.SUCCESS_MESSAGE))
        return self
    
    def proceed_to_checkout(self):
        """Proceed to checkout after adding to cart"""
        self.click_element(self.PROCEED_TO_CHECKOUT)
        # Return the next expected page
        from .shopping_cart_page import ShoppingCartPage
        return ShoppingCartPage(self.driver)
    
    def continue_shopping(self):
        """Continue shopping after adding to cart"""
        self.click_element(self.CONTINUE_SHOPPING)
        return self
    
    def get_success_message(self):
        """Get the success message after adding to cart"""
        return self.get_text(self.SUCCESS_MESSAGE)
