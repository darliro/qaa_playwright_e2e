import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    # Set Chrome options for running the browser
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Determine the environment: local or Docker
    env = os.getenv("ENV", "local")

    if env == "local":  # Local environment on Mac
        chrome_driver_path = (
            "/opt/homebrew/bin/chromedriver"  # Path to local chromedriver
        )
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

    else:  # Docker environment
        options.add_argument("--headless")  # Enable headless mode for Docker
        chrome_driver_path = "/usr/bin/chromedriver"  # Path to chromedriver in Docker
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

    # Assign the driver instance to the class for tests
    request.cls.driver = driver
    yield driver
    driver.quit()  # Quit the driver after the test class execution is complete
