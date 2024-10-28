import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step("Opening page: {url}")
    def open_page(self, url: str = None) -> None:
        target_url: str = url or getattr(self, "PAGE_URL", None)
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

    @allure.step("Waiting for element and performing action: {locator}")
    def wait_and_perform(self, locator: str, action: callable) -> None:
        self.wait_for_element(locator)
        action(self.page.locator(locator))

    @allure.step("Waiting for element: {locator}")
    def wait_for_element(
        self, locator: str, state: str = "visible", timeout: int = 10000
    ) -> None:
        self.page.wait_for_selector(locator, state=state, timeout=timeout)

    @allure.step("Filling field: {locator}")
    def fill_field(self, locator: str, value: str) -> None:
        self.wait_and_perform(
            locator, lambda element: element.click() or element.fill(value)
        )

    @allure.step("Clicking element: {locator}")
    def click_element(self, locator: str) -> None:
        self.wait_and_perform(locator, lambda element: element.click())

    @allure.step("Verify element value: {locator}")
    def verify_field_value(
        self, locator: str, expected_value: str, timeout: int = 10000
    ) -> None:
        expect(self.page.locator(locator)).to_have_value(
            expected_value, timeout=timeout
        )

    @allure.step("Verify selected value in dropdown: {locator}")
    def verify_dropdown_value(self, locator: str, expected_value: str) -> None:
        self.wait_for_element(locator)
        expect(self.page.locator(locator)).to_have_text(expected_value.strip())

    @allure.step("Verify selected value in radio: {locator}")
    def verify_radio_selected(self, locator: str) -> None:
        self.wait_for_element(locator)
        class_value = self.page.locator(locator).get_attribute("class")
        assert (
            "oxd-radio-input--active"
            in self.page.locator(locator).get_attribute("class")
        ), f"Expected 'oxd-radio-input--active' in class attribute, but got: {class_value}"
