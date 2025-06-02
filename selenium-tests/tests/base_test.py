import os
import pytest
import allure
from datetime import datetime
from ..utils.driver_factory import DriverFactory
from ..utils.config import Config


class BaseTest:
    """Base class for all test classes"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self, request):
        """Setup and teardown for each test"""
        # Create the driver
        self.driver = DriverFactory.get_driver(Config.BROWSER, Config.HEADLESS)
        self.driver.maximize_window()
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        # Make driver available to the test
        yield self.driver
        
        # Teardown
        if request.node.rep_call.failed:
            self.take_screenshot(request.node.name)
        
        self.driver.quit()
    
    def take_screenshot(self, test_name):
        """Take a screenshot on test failure"""
        # Create screenshots directory if it doesn't exist
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
        
        # Generate a unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(Config.SCREENSHOT_DIR, filename)
        
        # Take the screenshot
        self.driver.save_screenshot(filepath)
        
        # Attach the screenshot to the Allure report
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=test_name,
            attachment_type=allure.attachment_type.PNG
        )
        
        return filepath


# This plugin helps to detect test failures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
