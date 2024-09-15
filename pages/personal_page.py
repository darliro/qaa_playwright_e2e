import allure
from playwright.sync_api import expect
from base.base_page import BasePage
from config.link_config import Links
from config.selectors_config import PERSONAL_PAGE


class PersonalPage(BasePage):
    PAGE_URL: str = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD: str = PERSONAL_PAGE["first_name_field"]
    SAVE_BUTTON: str = PERSONAL_PAGE["save_button"]
    SPINNER: str = PERSONAL_PAGE["spinner"]

    @allure.step("Update first name to '{new_name}'")
    def update_first_name(self, new_name: str) -> None:
        self.clear_and_fill(self.FIRST_NAME_FIELD, new_name)

    @allure.step("Click 'Save' button")
    def click_save_button(self) -> None:
        self.page.locator(self.SAVE_BUTTON).click()
        self.wait_for_spinner_to_disappear()

    @allure.step("Verify first name is updated to '{expected_name}'")
    def verify_first_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator(self.FIRST_NAME_FIELD)).to_have_value(
            expected_name, timeout=10000
        )

    def wait_for_spinner_to_disappear(self) -> None:
        expect(self.page.locator(self.SPINNER)).to_be_hidden()
