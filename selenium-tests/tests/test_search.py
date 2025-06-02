import pytest
import allure
from ..pages.search_page import SearchPage
from ..utils.test_data import TestData
from .base_test import BaseTest


@allure.feature("Product Search")
class TestSearch(BaseTest):
    """Test cases for the search functionality"""
    
    @allure.story("Search Results")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_with_results(self):
        """Test search with results"""
        # Use a search term that should return results
        search_term = "dress"
        
        # Navigate to the base URL
        self.driver.get("http://automationpractice.com/index.php")
        
        # Create search page object
        search_page = SearchPage(self.driver)
        
        # Perform search
        search_page.search_for_product(search_term)
        
        # Verify search results
        results_count = search_page.get_search_results_count()
        assert results_count > 0, f"No search results found for '{search_term}'"
        
        # Verify product names contain the search term
        product_names = search_page.get_product_names()
        for name in product_names:
            assert search_term.lower() in name.lower(), f"Product name '{name}' does not contain search term '{search_term}'"
    
    @allure.story("No Search Results")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_no_results(self):
        """Test search with no results"""
        # Use a search term that should not return results
        search_term = "xyznonexistentproduct123"
        
        # Navigate to the base URL
        self.driver.get("http://automationpractice.com/index.php")
        
        # Create search page object
        search_page = SearchPage(self.driver)
        
        # Perform search
        search_page.search_for_product(search_term)
        
        # Verify no results message
        assert search_page.has_no_results(), "No results message not displayed"
        
        # Verify no results message contains expected text
        no_results_message = search_page.get_no_results_message()
        assert "no results" in no_results_message.lower(), f"No results message '{no_results_message}' does not contain expected text"
    
    @allure.story("Search with Enter Key")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_with_enter_key(self):
        """Test search using Enter key instead of clicking the search button"""
        # Use a search term that should return results
        search_term = "blouse"
        
        # Navigate to the base URL
        self.driver.get("http://automationpractice.com/index.php")
        
        # Create search page object
        search_page = SearchPage(self.driver)
        
        # Perform search using Enter key
        search_page.search_with_enter_key(search_term)
        
        # Verify search results
        results_count = search_page.get_search_results_count()
        assert results_count > 0, f"No search results found for '{search_term}'"
    
    @allure.story("Product Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_product_from_search(self):
        """Test navigating to a product from search results"""
        # Use a search term that should return results
        search_term = "shirt"
        
        # Navigate to the base URL
        self.driver.get("http://automationpractice.com/index.php")
        
        # Create search page object
        search_page = SearchPage(self.driver)
        
        # Perform search
        search_page.search_for_product(search_term)
        
        # Verify search results
        results_count = search_page.get_search_results_count()
        assert results_count > 0, f"No search results found for '{search_term}'"
        
        # Click on the first product
        product_page = search_page.click_on_product(0)
        
        # Verify we're on the product page
        product_name = product_page.get_product_name()
        assert product_name, "Product name not found on product page"
