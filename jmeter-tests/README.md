# JMeter Test Plans

This directory contains JMeter test plans for load testing REST APIs.

## Test Plans

1. `api_load_test.jmx` - Tests the main API endpoints with different user loads (100, 500, 1000 concurrent users)
2. `performance_test.jmx` - Measures response time and throughput for critical endpoints
3. `stress_test.jmx` - Stress testing with gradually increasing load

## How to Run

1. Install Apache JMeter
2. Open the .jmx file with JMeter GUI
3. Configure any necessary parameters
4. Run the test or use command line:

```bash
jmeter -n -t api_load_test.jmx -l results.jtl -e -o report_folder
```

## Automated Execution

The test plans can be executed automatically as part of the CI/CD pipeline. See the `/ci-cd` directory for the configuration.
