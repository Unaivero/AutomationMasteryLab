FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    curl \
    nodejs \
    npm \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome for Selenium tests
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install Newman for Postman tests
RUN npm install -g newman newman-reporter-htmlextra

# Install JMeter
RUN mkdir -p /opt/jmeter \
    && wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.5.tgz -O /tmp/apache-jmeter-5.5.tgz \
    && tar -xzf /tmp/apache-jmeter-5.5.tgz -C /opt/jmeter --strip-components=1 \
    && rm /tmp/apache-jmeter-5.5.tgz

# Add JMeter to PATH
ENV PATH="/opt/jmeter/bin:${PATH}"

# Install Allure
RUN curl -o allure-2.22.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.22.0/allure-commandline-2.22.0.tgz \
    && tar -zxf allure-2.22.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.22.0/bin/allure /usr/bin/allure \
    && rm allure-2.22.0.tgz

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make scripts executable
RUN chmod +x run_all_tests.sh postman-tests/run_tests.sh

# Command to run tests
CMD ["./run_all_tests.sh"]
