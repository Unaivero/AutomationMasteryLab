# JMeter Performance Testing Guide

This guide provides detailed instructions for using the JMeter test plans included in the Automation Mastery Lab.

## Test Plans Overview

The project includes three main JMeter test plans:

1. **api_load_test.jmx**: Tests the main API endpoints with different user loads (100, 500, 1000 concurrent users)
2. **performance_test.jmx**: Measures response time and throughput for critical endpoints
3. **stress_test.jmx**: Stress testing with gradually increasing load

## Test Scenarios

### Load Testing (api_load_test.jmx)

This test plan simulates multiple users accessing the API endpoints simultaneously:

- **User Scenario 1**: 100 concurrent users
  - Ramp-up: 30 seconds
  - Loop count: 5
  - Endpoints tested: GET /users, GET /user/{id}, POST /users

- **User Scenario 2**: 500 concurrent users
  - Ramp-up: 60 seconds
  - Loop count: 3
  - Endpoints tested: Same as Scenario 1

- **User Scenario 3**: 1000 concurrent users
  - Ramp-up: 120 seconds
  - Loop count: 1
  - Endpoints tested: Same as Scenario 1

### Performance Testing (performance_test.jmx)

This test plan focuses on measuring performance metrics:

- Response time (average, median, 90th percentile, 95th percentile)
- Throughput (requests per second)
- Error rate

### Stress Testing (stress_test.jmx)

This test plan gradually increases the load until the system breaks:

- Starting with 10 users
- Incrementing by 10 users every 30 seconds
- Maximum users: 1000
- Continues until error rate exceeds 5%

## Running the Tests

### Using JMeter GUI

1. Open JMeter:
   ```bash
   jmeter
   ```

2. Open the test plan:
   - File > Open
   - Navigate to the .jmx file

3. Configure test parameters if needed
4. Run the test:
   - Click the green "Start" button (or Ctrl+R)

### Using Command Line (Non-GUI Mode)

For better performance, run tests in non-GUI mode:

```bash
# Basic execution
jmeter -n -t api_load_test.jmx -l results.jtl

# With additional options
jmeter -n -t api_load_test.jmx -l results.jtl -e -o report_folder
```

Options:
- `-n`: Non-GUI mode
- `-t`: Test plan file
- `-l`: Log file (results)
- `-e`: Generate report at end
- `-o`: Output folder for report

## Configuring the Tests

### Thread Groups

Modify thread groups to adjust the load:

1. Right-click on Thread Group > Edit
2. Change:
   - Number of Threads (users)
   - Ramp-up Period (seconds)
   - Loop Count

### HTTP Requests

Configure the HTTP requests:

1. Select an HTTP Request element
2. Set:
   - Protocol: http/https
   - Server Name or IP
   - Port Number
   - Path
   - Method (GET, POST, etc.)
   - Parameters/Body Data

### Assertions

Add assertions to validate responses:

1. Right-click on HTTP Request > Add > Assertions
2. Choose assertion type:
   - Response Assertion (text patterns)
   - Duration Assertion (response time)
   - Size Assertion (response size)
   - JSON Assertion (JSON structure)

## Analyzing Results

### Real-time Analysis

During test execution in GUI mode:
- View Results Tree
- Summary Report
- Aggregate Report
- Response Time Graph

### Post-test Analysis

After test execution:
1. Open results in JMeter:
   - File > Open > results.jtl

2. View HTML report (if generated):
   ```bash
   open report_folder/index.html
   ```

3. Key metrics to analyze:
   - Average Response Time: < 1000ms is generally good
   - Error Rate: Should be < 1%
   - Throughput: Higher is better
   - 90th/95th percentile: Shows worst-case performance

## Best Practices

1. **Always run load tests in non-GUI mode** for accurate results
2. **Start with a small number of threads** and gradually increase
3. **Use CSV files for test data** to make tests more realistic
4. **Include think time** between requests using Timers
5. **Monitor server resources** during test execution
6. **Clean up test data** after test execution

## Troubleshooting

Common issues and solutions:

1. **OutOfMemoryError**:
   - Increase JMeter memory: `JVM_ARGS="-Xms1g -Xmx2g" jmeter -n -t test.jmx`

2. **Connection refused**:
   - Check if the server is running
   - Verify firewall settings

3. **Slow ramp-up**:
   - Increase ramp-up time for large thread groups
   - Use multiple thread groups with staggered start times

4. **High CPU usage**:
   - Reduce listeners in non-GUI mode
   - Use Simple Data Writer instead of complex listeners
