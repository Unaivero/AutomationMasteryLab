import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class Config:
    """Configuration utility for test framework"""
    
    # Browser configuration
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    
    # Application URLs
    BASE_URL = os.getenv("BASE_URL", "http://automationpractice.com")
    
    # Test data
    DEFAULT_USERNAME = os.getenv("DEFAULT_USERNAME", "test.user@example.com")
    DEFAULT_PASSWORD = os.getenv("DEFAULT_PASSWORD", "Password123")
    
    # Reporting
    SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "reports", "screenshots")
    
    @staticmethod
    def get_browser_options():
        """Get browser-specific options"""
        browser = Config.BROWSER.lower()
        options = {}
        
        if browser == "chrome":
            options["arguments"] = ["--disable-gpu", "--no-sandbox"]
            if Config.HEADLESS:
                options["arguments"].append("--headless")
        
        elif browser == "firefox":
            if Config.HEADLESS:
                options["arguments"] = ["-headless"]
        
        return options
