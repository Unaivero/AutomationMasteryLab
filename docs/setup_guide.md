# Automation Mastery Lab - Setup Guide

This guide provides detailed instructions for setting up and running the Automation Mastery Lab testing framework.

## Environment Setup

### 1. Python Environment

The Selenium tests are written in Python. Set up your Python environment as follows:

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. JMeter Setup

1. Download [Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi)
2. Extract the archive to a location of your choice
3. Add JMeter to your PATH:
   ```bash
   # On macOS/Linux
   export PATH=$PATH:/path/to/apache-jmeter/bin
   
   # On Windows (add to system environment variables)
   # C:\path\to\apache-jmeter\bin
   ```

### 3. Postman/Newman Setup

1. Install Node.js and npm
2. Install Newman and the HTML reporter:
   ```bash
   npm install -g newman newman-reporter-htmlextra
   ```

### 4. WebDrivers for Selenium

The framework uses WebDriver Manager to automatically download and manage browser drivers, but you can also set them up manually:

```bash
# Chrome WebDriver
webdriver-manager update --chrome
# Firefox WebDriver (GeckoDriver)
webdriver-manager update --gecko
```

### 5. Allure Reporting Tool

Install Allure command-line tool for generating test reports:

```bash
# Using npm
npm install -g allure-commandline

# On macOS using Homebrew
brew install allure
```

## Configuration

### Selenium Test Configuration

Edit the configuration file at `selenium-tests/utils/config.py` to customize:

- Browser settings
- Base URL
- Default credentials
- Timeouts

### JMeter Test Configuration

Edit the JMeter test plans (`.jmx` files) using JMeter GUI to customize:

- Number of threads (users)
- Ramp-up period
- Loop count
- Assertions

### Postman Test Configuration

Edit the environment file at `postman-tests/api_environment.json` to customize:

- Base URL
- API endpoints
- Timeout values
- Authentication tokens

## Running Tests

### Running All Tests

To run all tests in sequence, use the CI/CD pipeline configuration or create a shell script:

```bash
#!/bin/bash

# Run Selenium tests
cd selenium-tests
python -m pytest tests/ --alluredir=../reports/allure-results

# Run Postman tests
cd ../postman-tests
./run_tests.sh

# Run JMeter tests
cd ../jmeter-tests
jmeter -n -t api_load_test.jmx -l ../reports/jmeter-results/results.jtl -e -o ../reports/jmeter-results/dashboard

# Generate reports
cd ../reports
python generate_reports.py --open
```

### Running Individual Test Suites

#### Selenium UI Tests

```bash
# Run all Selenium tests
cd selenium-tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_login.py

# Run specific test
python -m pytest tests/test_login.py::TestLogin::test_successful_login

# Run with markers
python -m pytest -m "critical"
```

#### Postman API Tests

```bash
cd postman-tests
newman run api_test_collection.json --environment api_environment.json
```

#### JMeter Performance Tests

```bash
cd jmeter-tests
jmeter -n -t api_load_test.jmx -l results.jtl
```

## Generating Reports

After running tests, generate comprehensive reports:

```bash
cd reports
python generate_reports.py
```

This will create:
- Allure HTML reports for Selenium tests
- HTML reports for Postman API tests
- Dashboard reports for JMeter performance tests

To view the Allure report in a browser:

```bash
allure serve reports/allure-results
```

## Troubleshooting

### Common Issues

1. **WebDriver errors**:
   - Ensure you have the correct browser versions installed
   - Try updating WebDriver: `webdriver-manager update`

2. **JMeter connection errors**:
   - Check firewall settings
   - Verify the target server is accessible

3. **Newman/Postman failures**:
   - Verify API endpoints are correct
   - Check authentication tokens

4. **Report generation issues**:
   - Ensure Allure is correctly installed
   - Check file permissions in the reports directory

For more detailed troubleshooting, check the logs in the respective test directories.
