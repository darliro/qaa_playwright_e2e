FROM python:3.13-slim

# Install system dependencies and Allure
RUN apt-get update && apt-get install -y openjdk-17-jre curl && \
    apt-get clean && \
    curl -o allure-2.30.0.tgz -L https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz && \
    tar -zxvf allure-2.30.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure && \
    rm allure-2.30.0.tgz && \
    apt-get clean

# Set the working directory for the project
WORKDIR /usr/workspace

# Copy the dependencies into the working directory
COPY ./pyproject.toml ./pdm.lock /usr/workspace/

# Install Python dependencies with PDM
RUN pip install pdm && pdm install --prod --no-self --no-editable

# Install Playwright browsers using the virtual environment
RUN pdm run playwright install chromium --with-deps

# Default command to run the tests
CMD ["pdm", "run", "pytest", "-sv", "--alluredir=allure-results"]