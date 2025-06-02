#!/bin/bash

# Automation Mastery Lab - Main Test Runner
# This script runs all tests (Selenium, Postman, JMeter) and generates reports

# Set colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Create necessary directories
echo -e "${YELLOW}Creating report directories...${NC}"
mkdir -p reports/allure-results
mkdir -p reports/postman-reports/html
mkdir -p reports/postman-reports/junit
mkdir -p reports/jmeter-results
mkdir -p reports/screenshots

# Function to run tests with error handling
run_test() {
    echo -e "${YELLOW}Running $1 tests...${NC}"
    eval $2
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $1 tests completed successfully!${NC}"
        return 0
    else
        echo -e "${RED}❌ $1 tests failed!${NC}"
        return 1
    fi
}

# Track overall status
OVERALL_STATUS=0

# Run Selenium tests
run_test "Selenium UI" "cd selenium-tests && python -m pytest tests/ -v --alluredir=../reports/allure-results"
SELENIUM_STATUS=$?
OVERALL_STATUS=$((OVERALL_STATUS + SELENIUM_STATUS))

# Run Postman API tests
run_test "Postman API" "cd postman-tests && ./run_tests.sh"
POSTMAN_STATUS=$?
OVERALL_STATUS=$((OVERALL_STATUS + POSTMAN_STATUS))

# Run JMeter tests (commented out as JMeter may not be installed)
# Uncomment this section if JMeter is installed
# run_test "JMeter Performance" "cd jmeter-tests && jmeter -n -t api_load_test.jmx -l ../reports/jmeter-results/results.jtl -e -o ../reports/jmeter-results/dashboard"
# JMETER_STATUS=$?
# OVERALL_STATUS=$((OVERALL_STATUS + JMETER_STATUS))

# Generate reports
echo -e "${YELLOW}Generating test reports...${NC}"
cd reports && python generate_reports.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Reports generated successfully!${NC}"
else
    echo -e "${RED}❌ Failed to generate reports!${NC}"
    OVERALL_STATUS=$((OVERALL_STATUS + 1))
fi

# Print summary
echo -e "\n${YELLOW}=== Test Execution Summary ===${NC}"
echo -e "Selenium UI Tests: $([ $SELENIUM_STATUS -eq 0 ] && echo -e "${GREEN}PASSED${NC}" || echo -e "${RED}FAILED${NC}")"
echo -e "Postman API Tests: $([ $POSTMAN_STATUS -eq 0 ] && echo -e "${GREEN}PASSED${NC}" || echo -e "${RED}FAILED${NC}")"
# echo -e "JMeter Performance Tests: $([ $JMETER_STATUS -eq 0 ] && echo -e "${GREEN}PASSED${NC}" || echo -e "${RED}FAILED${NC}")"

# Exit with status
if [ $OVERALL_STATUS -eq 0 ]; then
    echo -e "\n${GREEN}🎉 All tests completed successfully!${NC}"
    exit 0
else
    echo -e "\n${RED}❌ Some tests failed. Check the reports for details.${NC}"
    exit 1
fi
