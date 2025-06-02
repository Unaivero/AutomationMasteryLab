# 🚀 Automation Mastery Lab

A comprehensive, multi-layered test automation framework showcasing modern testing practices across UI, API, and Performance testing domains. Built with Python, Selenium WebDriver, Postman/Newman, JMeter, and enterprise CI/CD integration.

## 🎯 Overview

AutomationMasteryLab is a production-ready testing framework that demonstrates best practices in test automation across multiple testing layers. It serves as both a learning platform and a robust foundation for enterprise-scale automation projects.

## ✨ Features

### **🌐 UI Test Automation**
- **Selenium WebDriver 4.10** with modern browser management
- **Page Object Model (POM)** architecture for maintainable code
- **Cross-browser testing** support (Chrome, Firefox, Edge, Safari)
- **Responsive and mobile testing** capabilities
- **Screenshot capture** on test failures
- **Data-driven testing** with external test data sources

### **🔌 API Test Automation**
- **Postman Collections** with comprehensive API test scenarios
- **Newman CLI integration** for automated API testing
- **Environment management** for multiple test environments
- **Request/Response validation** and schema testing
- **Authentication handling** and token management
- **Performance assertions** for API response times

### **⚡ Performance Testing**
- **JMeter test plans** for load, stress, and performance testing
- **Scalable load testing** scenarios with configurable parameters
- **Performance metrics collection** and analysis
- **Automated performance reporting** with thresholds
- **CI/CD integration** for continuous performance monitoring

### **🛠️ DevOps & CI/CD**
- **Docker containerization** for consistent test environments
- **Jenkins pipeline** with declarative configuration
- **GitLab CI/CD** integration for GitLab environments
- **Allure reporting** with rich HTML test reports
- **Multi-stage testing** pipeline with parallel execution
- **Automated test result notifications**

## 📁 Project Structure

```
AutomationMasteryLab/
├── selenium-tests/                    # UI automation tests
│   ├── pages/                         # Page Object Model classes
│   ├── tests/                         # Test scenarios
│   │   ├── test_login.py              # Authentication tests
│   │   ├── test_registration.py       # User registration tests
│   │   ├── test_product.py            # Product workflow tests
│   │   └── test_search.py             # Search functionality tests
│   ├── utils/                         # Utility functions and helpers
│   ├── test_data/                     # Test data files (JSON/CSV)
│   ├── conftest.py                    # Pytest configuration and fixtures
│   └── .env                           # Environment configuration
├── postman-tests/                     # API automation tests
│   ├── api_test_collection.json       # Postman test collection
│   ├── api_environment.json           # Environment variables
│   ├── postman_test_guide.md          # API testing documentation
│   └── run_tests.sh                   # API test runner script
├── jmeter-tests/                      # Performance tests
│   ├── api_load_test.jmx              # API load testing scenarios
│   ├── performance_test.jmx           # Performance benchmark tests
│   ├── stress_test.jmx                # Stress testing scenarios
│   ├── jmeter_test_guide.md           # Performance testing guide
│   └── README.md                      # JMeter setup instructions
├── ci-cd/                             # CI/CD pipeline configurations
│   ├── Jenkinsfile                    # Jenkins declarative pipeline
│   └── .gitlab-ci.yml                 # GitLab CI/CD configuration
├── reports/                           # Test execution reports
│   ├── allure-results/                # Allure test results
│   ├── postman-reports/               # API test reports
│   ├── jmeter-results/                # Performance test results
│   └── screenshots/                   # UI test screenshots
├── docs/                              # Project documentation
├── Dockerfile                         # Container configuration
├── docker-compose.yml                 # Multi-container setup
├── requirements.txt                   # Python dependencies
├── pytest.ini                        # Pytest configuration
└── run_all_tests.sh                   # Master test execution script
```

## 🛠️ Technology Stack

### **Core Technologies**
| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Language** | Python | 3.8+ | Main automation language |
| **UI Testing** | Selenium WebDriver | 4.10.0 | Browser automation |
| **Test Framework** | Pytest | 7.3.1 | Test execution and fixtures |
| **API Testing** | Postman/Newman | Latest | API validation and testing |
| **Performance** | Apache JMeter | 5.5+ | Load and performance testing |
| **Reporting** | Allure | 2.13.2 | Rich HTML test reports |
| **Containerization** | Docker | Latest | Environment consistency |

### **Supporting Libraries**
- **webdriver-manager**: Automated browser driver management
- **requests**: HTTP library for API testing
- **faker**: Dynamic test data generation
- **python-dotenv**: Environment variable management
- **pytest-html**: HTML test reporting

## 🚦 Quick Start

### **Prerequisites**
- Python 3.8 or higher
- Chrome browser (latest version)
- Docker (optional, for containerized execution)
- Node.js and npm (for Newman API testing)
- Java JDK 8+ (for JMeter performance testing)

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/Unaivero/AutomationMasteryLab.git
cd AutomationMasteryLab
```

2. **Set up Python environment**
```bash
# Create virtual environment
python -m venv automation_env

# Activate virtual environment
# On macOS/Linux:
source automation_env/bin/activate
# On Windows:
automation_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

3. **Install additional tools**
```bash
# Install Newman for API testing
npm install -g newman newman-reporter-html

# Install JMeter (download from https://jmeter.apache.org/)
# Or via package manager:
# macOS: brew install jmeter
# Ubuntu: sudo apt-get install jmeter
```

### **Environment Configuration**
```bash
# Copy environment template
cp selenium-tests/.env.example selenium-tests/.env

# Edit configuration
# Set BASE_URL, browser preferences, timeouts, etc.
```

## 🎮 Running Tests

### **UI Tests (Selenium)**
```bash
# Run all UI tests
cd selenium-tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_login.py -v

# Run with different browser
python -m pytest tests/ -v --browser=firefox

# Run with custom markers
python -m pytest tests/ -m smoke -v

# Generate Allure report
python -m pytest tests/ --alluredir=../reports/allure-results
allure serve ../reports/allure-results
```

### **API Tests (Postman/Newman)**
```bash
# Run API test collection
cd postman-tests
./run_tests.sh

# Run with specific environment
newman run api_test_collection.json -e api_environment.json

# Generate HTML report
newman run api_test_collection.json -e api_environment.json \
  -r html --reporter-html-export ../reports/postman-reports/api-report.html
```

### **Performance Tests (JMeter)**
```bash
# Run load test
cd jmeter-tests
jmeter -n -t api_load_test.jmx -l ../reports/jmeter-results/load-test.jtl

# Run with custom parameters
jmeter -n -t performance_test.jmx \
  -Jusers=50 -Jramp-up=300 -Jduration=600 \
  -l ../reports/jmeter-results/performance-test.jtl

# Generate HTML dashboard
jmeter -n -t stress_test.jmx \
  -l ../reports/jmeter-results/stress-test.jtl \
  -e -o ../reports/jmeter-results/stress-dashboard
```

### **Run All Tests**
```bash
# Execute complete test suite
./run_all_tests.sh

# This will run:
# 1. All Selenium UI tests
# 2. All Postman API tests  
# 3. Selected JMeter performance tests
# 4. Generate comprehensive reports
```

## 🐳 Docker Execution

### **Build and Run Container**
```bash
# Build Docker image
docker build -t automation-mastery-lab .

# Run tests in container
docker run --rm -v $(pwd)/reports:/app/reports automation-mastery-lab

# Run with Docker Compose
docker-compose up --build
```

### **Container Features**
- Pre-configured Python environment with all dependencies
- Headless browser execution for CI/CD environments
- Automated report generation and export
- Volume mounting for persistent test reports

## 📊 Test Reports & Analytics

### **Allure Reports**
Rich, interactive HTML reports with:
- Test execution timeline and trends
- Detailed step-by-step test execution
- Screenshots and logs for failed tests
- Historical test data comparison
- Flaky test detection and analysis

### **API Test Reports**
- Request/response validation results
- Performance metrics and response times
- Environment variable usage tracking
- Test data coverage analysis

### **Performance Reports**
- Load testing metrics and graphs
- Response time percentiles and throughput
- Error rate analysis and bottleneck identification
- Scalability and stress testing results

## 🔧 Configuration

### **Browser Configuration**
```python
# pytest.ini or conftest.py
[tool:pytest]
addopts = --browser=chrome --headless=false --window-size=1920,1080
markers = 
    smoke: Quick validation tests
    regression: Full regression test suite
    login: Authentication related tests
    api: API integration tests
```

### **Environment Variables**
```bash
# selenium-tests/.env
BASE_URL=https://example.com
BROWSER=chrome
HEADLESS=false
TIMEOUT=10
SCREENSHOT_ON_FAILURE=true
TEST_DATA_PATH=test_data/
```

### **CI/CD Configuration**
```yaml
# ci-cd/.gitlab-ci.yml
stages:
  - test-ui
  - test-api  
  - test-performance
  - report
  - notify
```

## 🏗️ Framework Architecture

### **Design Patterns**
- **Page Object Model (POM)**: Maintainable UI test structure
- **Factory Pattern**: Browser and driver initialization
- **Singleton Pattern**: Configuration management
- **Builder Pattern**: Test data creation
- **Strategy Pattern**: Multiple browser support

### **Key Principles**
- **DRY (Don't Repeat Yourself)**: Reusable components and utilities
- **SOLID Principles**: Clean, maintainable code architecture
- **Separation of Concerns**: Clear distinction between tests, data, and configuration
- **Scalability**: Framework designed for large-scale test suites

## 📈 Advanced Features

### **Parallel Execution**
```bash
# Run tests in parallel
python -m pytest tests/ -n auto  # Auto-detect CPU cores
python -m pytest tests/ -n 4     # Use 4 parallel workers
```

### **Test Data Management**
- **Dynamic data generation** with Faker library
- **Environment-specific test data** configuration
- **CSV/JSON data source** integration
- **Database connectivity** for data validation

### **Custom Reporting**
- **Slack/Teams notifications** for test results
- **Email reports** with executive summaries
- **Grafana dashboards** for test metrics visualization
- **JIRA integration** for defect management

## 🔍 Best Practices Demonstrated

### **Code Quality**
- **PEP 8 compliance** and consistent code formatting
- **Type hints** for better code documentation
- **Comprehensive logging** throughout the framework
- **Error handling** and graceful test failures

### **Test Design**
- **Independent test cases** that can run in any order
- **Data-driven testing** for comprehensive coverage
- **Clear test documentation** and meaningful assertions
- **Proper test categorization** with markers and tags

### **Maintenance**
- **Version pinning** for stable dependency management
- **Configuration externalization** for environment flexibility
- **Modular design** for easy extension and modification
- **Regular dependency updates** and security patches

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Follow coding standards** and add appropriate tests
4. **Run the full test suite** to ensure no regressions
5. **Update documentation** for new features
6. **Commit your changes** (`git commit -m 'Add amazing feature'`)
7. **Push to the branch** (`git push origin feature/amazing-feature`)
8. **Open a Pull Request** with detailed description

### **Development Guidelines**
- Write tests for new functionality
- Follow existing code structure and naming conventions
- Add appropriate documentation and comments
- Ensure cross-platform compatibility
- Update requirements.txt for new dependencies

## 📚 Learning Resources

### **Documentation**
- **Selenium WebDriver**: [Official Documentation](https://selenium-python.readthedocs.io/)
- **Pytest Framework**: [Testing Guide](https://docs.pytest.org/)
- **Postman API Testing**: [Learning Center](https://learning.postman.com/)
- **JMeter Performance Testing**: [User Manual](https://jmeter.apache.org/usermanual/)

### **Best Practices**
- **Test Automation Pyramid**: UI, API, Unit test distribution
- **Continuous Testing**: Integration with CI/CD pipelines
- **Test Data Management**: Strategies for maintainable test data
- **Reporting and Analytics**: Meaningful test metrics and KPIs

## 📞 Support & Feedback

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: GitHub Discussions for questions and community support
- **Documentation**: Check the `/docs` directory for detailed guides
- **Examples**: Review test files for implementation patterns

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Key Achievements

- ✅ **Multi-layer test automation** (UI, API, Performance)
- ✅ **Production-ready CI/CD integration** (Jenkins, GitLab)
- ✅ **Docker containerization** for consistent environments
- ✅ **Comprehensive reporting** with Allure and custom dashboards
- ✅ **Cross-browser and cross-platform support**
- ✅ **Scalable architecture** with parallel execution
- ✅ **Enterprise-grade practices** and design patterns
- ✅ **Extensive documentation** and learning resources

---

🎯 **Master modern test automation practices with this comprehensive, production-ready framework that covers all essential testing layers and DevOps integration.**

