import allure
from base.base_page import BasePage
from config.url_config import Links


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_INPUT = "input[name='firstName']"
    LAST_NAME_INPUT = "input[name='lastName']"
    MIDDLE_NAME_INPUT = "input[name='middleName']"
    EMPLOYEE_ID_INPUT = "//label[text()='Employee Id']/following::input[1]"
    OTHER_ID_INPUT = "//label[text()='Other Id']/following::input[1]"
    SAVE_BUTTON = "//p[contains(@class, 'orangehrm-form-hint')]/following-sibling::button[@type='submit']"
    LOADING_SPINNER = ".oxd-loading-spinner"

    @allure.step("Update first name to '{new_first_name}'")
    def update_first_name(self, new_first_name: str) -> None:
        self.fill_field(self.FIRST_NAME_INPUT, new_first_name)

    @allure.step("Update last name to '{new_last_name}'")
    def update_last_name(self, new_last_name: str) -> None:
        self.fill_field(self.LAST_NAME_INPUT, new_last_name)

    @allure.step("Update middle name to '{new_middle_name}'")
    def update_middle_name(self, new_middle_name: str) -> None:
        self.fill_field(self.MIDDLE_NAME_INPUT, new_middle_name)

    @allure.step("Update Employee ID to '{new_employee_id}'")
    def update_employee_id(self, new_employee_id: str) -> None:
        self.fill_field(self.EMPLOYEE_ID_INPUT, new_employee_id)

    @allure.step("Update Other ID to '{new_other_id}'")
    def update_other_id(self, new_other_id: str) -> None:
        self.fill_field(self.OTHER_ID_INPUT, new_other_id)

    @allure.step("Click 'Save' button")
    def click_save_button(self) -> None:
        self.wait_for_element(self.SAVE_BUTTON)
        self.page.locator(self.SAVE_BUTTON).click()
        self.wait_for_element(self.LOADING_SPINNER, state="hidden")

    @allure.step("Verify first name is updated to '{expected_name}'")
    def verify_first_name_is_updated(self, expected_name: str) -> None:
        self.verify_field_value(self.FIRST_NAME_INPUT, expected_name)

    @allure.step("Verify last name is updated to '{expected_name}'")
    def verify_last_name_is_updated(self, expected_name: str) -> None:
        self.verify_field_value(self.LAST_NAME_INPUT, expected_name)

    @allure.step("Verify middle name is updated to '{expected_name}'")
    def verify_middle_name_is_updated(self, expected_name: str) -> None:
        self.verify_field_value(self.MIDDLE_NAME_INPUT, expected_name)

    @allure.step("Verify employee ID is updated to '{expected_employee_id}'")
    def verify_employee_id_is_updated(self, expected_employee_id: str) -> None:
        self.verify_field_value(self.EMPLOYEE_ID_INPUT, expected_employee_id)

    @allure.step("Verify other ID is updated to '{expected_other_id}'")
    def verify_other_id_is_updated(self, expected_other_id: str) -> None:
        self.verify_field_value(self.OTHER_ID_INPUT, expected_other_id)
