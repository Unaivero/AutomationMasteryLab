from faker import Faker
import random
import string
import os
from datetime import datetime, timedelta

fake = Faker()


class TestData:
    """Utility class for generating test data"""
    
    @staticmethod
    def random_email():
        """Generate a random email address"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"test.user.{timestamp}@example.com"
    
    @staticmethod
    def random_password(length=10):
        """Generate a random password"""
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def random_name():
        """Generate a random first and last name"""
        return fake.first_name(), fake.last_name()
    
    @staticmethod
    def random_address():
        """Generate a random address"""
        return {
            'address1': fake.street_address(),
            'city': fake.city(),
            'state': 'Alabama',  # Using a fixed state for simplicity
            'postcode': fake.zipcode(),
            'country': 'United States',
            'mobile_phone': fake.phone_number(),
            'alias': 'My Address'
        }
    
    @staticmethod
    def random_date_of_birth():
        """Generate a random date of birth for an adult"""
        # Generate a date between 18 and 70 years ago
        date = fake.date_of_birth(minimum_age=18, maximum_age=70)
        return {
            'day': date.day,
            'month': date.month,
            'year': date.year
        }
    
    @staticmethod
    def random_product_search_terms():
        """Generate a list of product search terms"""
        return [
            "dress",
            "t-shirt",
            "blouse",
            "jeans",
            "shoes",
            "summer",
            "printed"
        ]
    
    @staticmethod
    def random_product_search_term():
        """Generate a random product search term"""
        return random.choice(TestData.random_product_search_terms())
    
    @staticmethod
    def invalid_credentials():
        """Generate a list of invalid credentials for negative testing"""
        return [
            {"email": "invalid@example.com", "password": "wrongpassword"},
            {"email": "notregistered@example.com", "password": "password123"},
            {"email": "invalid-email-format", "password": "password123"},
            {"email": "", "password": "password123"},
            {"email": "valid@example.com", "password": ""}
        ]
