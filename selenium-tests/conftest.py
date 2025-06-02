"""
Global pytest fixtures for Selenium tests
"""
import os
import pytest
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.config import Config


def pytest_addoption(parser):
    """Add command-line options for pytest"""
    parser.addoption(
        "--browser", action="store", default=Config.BROWSER, help="Browser to run tests with"
    )
    parser.addoption(
        "--headless", action="store_true", default=Config.HEADLESS, help="Run browser in headless mode"
    )
    parser.addoption(
        "--base-url", action="store", default=Config.BASE_URL, help="Base URL for the application"
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Get base URL from command line or config"""
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function")
def driver(request):
    """
    Create and configure WebDriver instance
    Returns the WebDriver instance
    Quits the WebDriver instance after the test
    """
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    
    # Setup WebDriver based on browser choice
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    # Set implicit wait time
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    # Return the driver instance
    yield driver
    
    # Quit the driver after test
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook for test result processing
    Capture screenshot on test failure
    """
    outcome = yield
    report = outcome.get_result()
    
    # Only capture screenshot for selenium tests that have the driver fixture
    if "driver" not in item.funcargs:
        return
    
    # Only capture screenshot on test failure during call phase
    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]
        take_screenshot(driver, item.name)


def take_screenshot(driver, test_name):
    """Capture and attach screenshot to Allure report"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(Config.SCREENSHOT_DIR, screenshot_name)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    
    # Take screenshot
    driver.save_screenshot(screenshot_path)
    
    # Attach to Allure report
    allure.attach.file(
        screenshot_path,
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG
    )
