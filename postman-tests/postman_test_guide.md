# Postman API Testing Guide

This guide provides detailed instructions for using the Postman collections included in the Automation Mastery Lab.

## Collection Overview

The project includes a comprehensive Postman collection (`api_test_collection.json`) that tests various API endpoints with different scenarios:

1. **Get Users - 200 OK**: Tests successful retrieval of users list
2. **Get Single User - 200 OK**: Tests successful retrieval of a specific user
3. **Get Single User - 404 Not Found**: Tests error handling for non-existent users
4. **Create User - 201 Created**: Tests successful user creation
5. **Update User - 200 OK**: Tests successful user update

## Test Scenarios

Each request in the collection includes tests that validate:

- **Status codes**: Verifying the correct HTTP status code is returned
- **Response time**: Ensuring the API responds within acceptable time limits
- **Response structure**: Validating the JSON structure of the response
- **Data validation**: Checking that the response data matches expected values
- **Headers**: Verifying the correct headers are present

## Running the Tests

### Using Postman GUI

1. Import the collection:
   - Open Postman
   - Click "Import" > Select `api_test_collection.json`
   - Import the environment file `api_environment.json`

2. Select the environment from the dropdown in the top-right corner

3. Run the collection:
   - Click on the collection name
   - Click "Run" button
   - Configure run settings (iterations, delay, etc.)
   - Click "Run Collection"

### Using Newman (Command Line)

Run the entire collection using Newman:

```bash
cd postman-tests
newman run api_test_collection.json --environment api_environment.json
```

With HTML reports:

```bash
newman run api_test_collection.json \
  --environment api_environment.json \
  --reporters cli,htmlextra,junit \
  --reporter-htmlextra-export ../reports/postman-reports/html/report.html \
  --reporter-junit-export ../reports/postman-reports/junit/report.xml
```

Or use the provided script:

```bash
./run_tests.sh
```

## Customizing the Tests

### Environment Variables

Edit the `api_environment.json` file to customize:

- `baseUrl`: The base URL for all API requests
- `userId`: The user ID to use for single user requests
- `timeout`: The maximum acceptable response time
- `authToken`: Authentication token if needed

### Test Scripts

Each request contains test scripts written in JavaScript. You can modify these scripts to add or change test assertions:

1. Open a request in Postman
2. Go to the "Tests" tab
3. Edit the JavaScript test code

Example test script:

```javascript
// Verify status code is 200
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Verify response time is less than 1000ms
pm.test("Response time is less than 1000ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(1000);
});

// Verify response has the correct format
pm.test("Response has the correct format", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
    pm.expect(jsonData.data).to.be.an('array');
});
```

## Adding New Tests

To add a new test to the collection:

1. In Postman, click on the collection
2. Click the "..." menu > "Add Request"
3. Configure the request details (URL, method, headers, body)
4. Add test scripts in the "Tests" tab
5. Save the request

After adding new tests, export the updated collection:

1. Click on the collection
2. Click the "..." menu > "Export"
3. Save as Collection v2.1
4. Replace the existing `api_test_collection.json` file

## Analyzing Test Results

### HTML Reports

After running tests with Newman, open the HTML report:

```bash
open ../reports/postman-reports/html/report.html
```

The report includes:
- Overall pass/fail status
- Response times
- Test results for each request
- Request and response details

### JUnit Reports

The JUnit reports can be integrated with CI/CD systems:

```bash
cat ../reports/postman-reports/junit/report.xml
```

## Best Practices

1. **Use environment variables** for all configurable values
2. **Structure tests logically** from simple to complex scenarios
3. **Include both positive and negative tests** for each endpoint
4. **Validate all aspects** of the response (status, headers, body)
5. **Set reasonable timeouts** for performance assertions
6. **Use descriptive test names** that explain what's being tested
7. **Clean up test data** after test execution when possible

## Troubleshooting

Common issues and solutions:

1. **Connection errors**:
   - Check if the API server is running
   - Verify network connectivity
   - Check for correct base URL

2. **Authentication failures**:
   - Verify the authentication token is valid
   - Check if token needs to be refreshed

3. **Test script errors**:
   - Check the JavaScript syntax
   - Verify the response structure matches expectations
   - Use `console.log()` for debugging

4. **Newman execution issues**:
   - Ensure Newman is installed correctly
   - Check for correct file paths
   - Verify JSON syntax in collection and environment files
