import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step("Opening page: {url}")
    def open_page(self, url: str = None) -> None:
        target_url: str = url or getattr(self, "PAGE_URL", None)
        if not target_url:
            raise ValueError("No URL provided for the page to open.")
        self.page.goto(target_url, wait_until="load")

    @allure.step("Verify URL is {expected_url}")
    def verify_url(self, expected_url: str) -> None:
        expect(self.page).to_have_url(expected_url)

    @allure.step("Taking screenshot: {screenshot_name}")
    def make_screenshot(self, screenshot_name: str = "screenshot") -> None:
        screenshot = self.page.screenshot()
        allure.attach(
            screenshot, name=screenshot_name, attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Filling field: {locator}")
    def fill_field(self, locator: str, value: str) -> None:
        element = self.page.locator(locator)
        element.click()
        element.fill("")
        element.fill(value)

    @allure.step("Waiting for element {locator} to reach state '{state}'")
    def wait_for_element(
        self, locator: str, state: str = "visible", timeout: int = 10000
    ) -> None:
        element = self.page.locator(locator)

        if state == "visible":
            expect(element).to_be_visible(timeout=timeout)
        elif state == "hidden":
            expect(element).to_be_hidden(timeout=timeout)
        else:
            raise ValueError(f"Unsupported state: {state}")
