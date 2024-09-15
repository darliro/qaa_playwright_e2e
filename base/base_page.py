import allure
from playwright.sync_api import Page, expect
from datetime import datetime


class BasePage:
    def __init__(self, page: Page):
        self.page: Page = page

    @allure.step("Opening page: {url}")
    def open_page(self, url: str = None) -> None:
        target_url: str = url or getattr(self, "PAGE_URL", None)
        self.page.goto(target_url, wait_until="load")

    @allure.step("Verifying URL: {self.PAGE_URL}")
    def verify_url(self) -> None:
        expected_url: str = getattr(self, "PAGE_URL", None)
        expect(self.page).to_have_url(expected_url)

    @allure.step("Taking screenshot: {screenshot_name}")
    def make_screenshot(self, screenshot_name: str = "screenshot") -> None:
        timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path: str = f"{screenshot_name}_{timestamp}.png"
        self.page.screenshot(path=screenshot_path)
        allure.attach.file(
            screenshot_path,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG,
        )

    @allure.step("Clearing and filling element: {locator}")
    def clear_and_fill(self, locator: str, value: str) -> None:
        element = self.page.locator(locator)
        element.click()
        element.fill("")
        element.fill(value)

    @allure.step("Waiting for spinner to be hidden: {spinner_locator}")
    def wait_for_spinner(
            self, spinner_locator: str = ".oxd-loading-spinner", timeout: int = 10000
    ) -> None:
        spinner = self.page.locator(spinner_locator)
        expect(spinner).to_be_hidden(timeout=timeout)
