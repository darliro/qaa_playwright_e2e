import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """
    Base page initialization.
    """

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self) -> None:  # Annotated return type as None
        """
        Opens the page using the URL specified in PAGE_URL.
        """
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def verify_url(self) -> None:
        """
        Verifies that the current URL matches PAGE_URL.
        """
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name: str) -> None:
        """
        Takes a screenshot of the current page and attaches it to the Allure report.
        """
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG,
        )
