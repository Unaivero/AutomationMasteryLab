#!/usr/bin/env python3
"""
Script to generate test reports from test results
"""
import os
import sys
import subprocess
import argparse
from datetime import datetime

# Define report directories
REPORT_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS_DIR = os.path.join(REPORT_DIR, "allure-results")
ALLURE_REPORT_DIR = os.path.join(REPORT_DIR, "allure-report")
JMETER_RESULTS_DIR = os.path.join(REPORT_DIR, "jmeter-results")
POSTMAN_REPORTS_DIR = os.path.join(REPORT_DIR, "postman-reports")


def create_directories():
    """Create necessary directories if they don't exist"""
    for directory in [
        ALLURE_RESULTS_DIR,
        ALLURE_REPORT_DIR,
        JMETER_RESULTS_DIR,
        os.path.join(POSTMAN_REPORTS_DIR, "html"),
        os.path.join(POSTMAN_REPORTS_DIR, "junit"),
        os.path.join(REPORT_DIR, "screenshots")
    ]:
        os.makedirs(directory, exist_ok=True)


def generate_allure_report():
    """Generate Allure report from test results"""
    try:
        print("Generating Allure report...")
        subprocess.run(
            ["allure", "generate", ALLURE_RESULTS_DIR, "-o", ALLURE_REPORT_DIR, "--clean"],
            check=True
        )
        print(f"✅ Allure report generated successfully at {ALLURE_REPORT_DIR}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate Allure report: {e}")
        return False
    except FileNotFoundError:
        print("❌ Allure command not found. Please install Allure command line tool.")
        return False


def open_allure_report():
    """Open Allure report in browser"""
    try:
        print("Opening Allure report in browser...")
        subprocess.run(
            ["allure", "open", ALLURE_REPORT_DIR],
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to open Allure report: {e}")
        return False
    except FileNotFoundError:
        print("❌ Allure command not found. Please install Allure command line tool.")
        return False


def check_test_failures():
    """Check for test failures in the results"""
    failures = []
    
    # Check Allure results
    if os.path.exists(ALLURE_RESULTS_DIR):
        for file in os.listdir(ALLURE_RESULTS_DIR):
            if file.endswith("-result.json"):
                with open(os.path.join(ALLURE_RESULTS_DIR, file), 'r') as f:
                    content = f.read()
                    if '"status":"failed"' in content:
                        failures.append(f"Allure: {file}")
    
    # Check JMeter results
    jmeter_results_file = os.path.join(JMETER_RESULTS_DIR, "results.jtl")
    if os.path.exists(jmeter_results_file):
        with open(jmeter_results_file, 'r') as f:
            content = f.read()
            if 'success="false"' in content:
                failures.append("JMeter: Performance test failures")
    
    # Check Postman results
    postman_junit_file = os.path.join(POSTMAN_REPORTS_DIR, "junit", "report.xml")
    if os.path.exists(postman_junit_file):
        with open(postman_junit_file, 'r') as f:
            content = f.read()
            if 'failures="' in content and not 'failures="0"' in content:
                failures.append("Postman: API test failures")
    
    return failures


def main():
    """Main function to generate reports"""
    parser = argparse.ArgumentParser(description='Generate test reports')
    parser.add_argument('--open', action='store_true', help='Open Allure report after generation')
    args = parser.parse_args()
    
    create_directories()
    
    # Generate Allure report
    if not generate_allure_report():
        sys.exit(1)
    
    # Check for test failures
    failures = check_test_failures()
    if failures:
        print("\n❌ Test failures detected:")
        for failure in failures:
            print(f"  - {failure}")
        print("\nPlease check the detailed reports for more information.")
    else:
        print("\n✅ All tests passed successfully!")
    
    # Open Allure report if requested
    if args.open:
        open_allure_report()


if __name__ == "__main__":
    main()
