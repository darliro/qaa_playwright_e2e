import allure
from base.base_page import BasePage
from config.url_config import Links
from playwright.sync_api import expect


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    @allure.step("Update first name to '{new_first_name}'")
    def update_first_name(self, new_first_name: str) -> None:
        self.page.locator("input[name='firstName']").fill(new_first_name)

    @allure.step("Update last name to '{new_last_name}'")
    def update_last_name(self, new_last_name: str) -> None:
        self.page.locator("input[name='lastName']").fill(new_last_name)

    @allure.step("Update middle name to '{new_middle_name}'")
    def update_middle_name(self, new_middle_name: str) -> None:
        self.page.locator("input[name='middleName']").fill(new_middle_name)

    @allure.step("Update Employee ID to '{new_employee_id}'")
    def update_employee_id(self, new_employee_id: str) -> None:
        self.page.locator(
            "//input[contains(@class, 'oxd-input oxd-input--active')][1]"
        ).fill(new_employee_id)

    @allure.step("Update Other ID to '{new_other_id}'")
    def update_other_id(self, new_other_id: str) -> None:
        self.page.locator(
            "//input[contains(@class, 'oxd-input oxd-input--active')][2]"
        ).fill(new_other_id)

    @allure.step("Click 'Save' button")
    def click_save_button(self) -> None:
        self.page.locator("//button[@type='submit'][1]").click()
        self.wait_for_element(".oxd-loading-spinner", state="hidden")

    @allure.step("Verify first name is updated to '{expected_name}'")
    def verify_first_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator("input[name='firstName']")).to_have_value(
            expected_name
        )

    @allure.step("Verify last name is updated to '{expected_name}'")
    def verify_last_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator("input[name='lastName']")).to_have_value(expected_name)

    @allure.step("Verify middle name is updated to '{expected_name}'")
    def verify_middle_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator("input[name='middleName']")).to_have_value(
            expected_name
        )

    @allure.step("Verify employee ID is updated to '{expected_employee_id}'")
    def verify_employee_id_is_updated(self, expected_employee_id: str) -> None:
        expect(
            self.page.locator(
                "//input[contains(@class, 'oxd-input oxd-input--active')][1]"
            ).to_have_value(expected_employee_id)
        )

    @allure.step("Verify other ID is updated to '{expected_other_id}'")
    def verify_other_id_is_updated(self, expected_other_id: str) -> None:
        expect(
            self.page.locator(
                "//input[contains(@class, 'oxd-input oxd-input--active')][2]"
            ).to_have_value(expected_other_id)
        )
