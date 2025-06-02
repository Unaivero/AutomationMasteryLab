import pytest
import allure
from ..pages.product_page import ProductPage
from .base_test import BaseTest


@allure.feature("Product Functionality")
class TestProduct(BaseTest):
    """Test cases for the product functionality"""
    
    @allure.story("Add to Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self):
        """Test adding a product to cart"""
        # Navigate directly to a product page
        self.driver.get("http://automationpractice.com/index.php?id_product=1&controller=product")
        
        # Create product page object
        product_page = ProductPage(self.driver)
        
        # Get product name and price for later verification
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        
        # Set quantity, size, and color
        product_page.set_quantity(2)
        product_page.select_size("M")
        product_page.select_color(1)  # Select the second color option
        
        # Add to cart
        product_page.add_to_cart()
        
        # Verify success message
        success_message = product_page.get_success_message()
        assert "added to your cart" in success_message.lower(), f"Success message '{success_message}' does not contain expected text"
        
        # Proceed to checkout
        cart_page = product_page.proceed_to_checkout()
        
        # Verify cart contains the product
        product_names = cart_page.get_product_names()
        assert product_name in product_names, f"Product '{product_name}' not found in cart"
        
        # Verify quantity is correct
        assert cart_page.get_cart_items_count() > 0, "Cart is empty"
    
    @allure.story("Product Details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_details_displayed(self):
        """Test that product details are correctly displayed"""
        # Navigate directly to a product page
        self.driver.get("http://automationpractice.com/index.php?id_product=2&controller=product")
        
        # Create product page object
        product_page = ProductPage(self.driver)
        
        # Verify product name is displayed
        product_name = product_page.get_product_name()
        assert product_name, "Product name not displayed"
        
        # Verify product price is displayed
        product_price = product_page.get_product_price()
        assert product_price, "Product price not displayed"
        
        # Verify size dropdown is displayed
        assert product_page.is_element_visible(product_page.SIZE_DROPDOWN), "Size dropdown not displayed"
        
        # Verify color options are displayed
        assert product_page.is_element_visible(product_page.COLOR_OPTIONS), "Color options not displayed"
        
        # Verify add to cart button is displayed
        assert product_page.is_element_visible(product_page.ADD_TO_CART_BUTTON), "Add to cart button not displayed"
    
    @allure.story("Continue Shopping")
    @allure.severity(allure.severity_level.NORMAL)
    def test_continue_shopping(self):
        """Test continue shopping functionality after adding to cart"""
        # Navigate directly to a product page
        self.driver.get("http://automationpractice.com/index.php?id_product=3&controller=product")
        
        # Create product page object
        product_page = ProductPage(self.driver)
        
        # Add to cart
        product_page.add_to_cart()
        
        # Continue shopping
        product_page.continue_shopping()
        
        # Verify we're still on the product page
        assert "controller=product" in product_page.get_current_url(), "Not on product page after continuing shopping"
