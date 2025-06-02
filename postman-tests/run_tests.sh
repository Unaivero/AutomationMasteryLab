#!/bin/bash

# Run Newman tests with HTML reporter
newman run api_test_collection.json \
  --environment api_environment.json \
  --reporters cli,htmlextra,junit \
  --reporter-htmlextra-export ../reports/postman-reports/html/report.html \
  --reporter-junit-export ../reports/postman-reports/junit/report.xml

# Check if tests passed
if [ $? -eq 0 ]; then
  echo "✅ API tests passed successfully!"
else
  echo "❌ API tests failed!"
  exit 1
fi
