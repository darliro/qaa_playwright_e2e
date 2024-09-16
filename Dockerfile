FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon0 \
    libgbm1 \
    libasound2 \
    libgtk-3-0 \
    libdrm2 \
    libxshmfence1 \
    ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Allure
RUN apt-get update && apt-get install -y \
    openjdk-17-jre \
    allure \
    curl \
    && apt-get clean

WORKDIR /usr/workspace

# Copy the dependencies file to the working directory
COPY ./pyproject.toml ./pdm.lock /usr/workspace/

# Install Python dependencies with PDM
RUN pip install pdm && pdm install --prod --no-self --no-editable

# Install Playwright browsers
RUN pdm run playwright install --with-deps

# Default command to run the tests
CMD ["pdm", "run", "pytest", "-sv", "--alluredir=allure-results"]
