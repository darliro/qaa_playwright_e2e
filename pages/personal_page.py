import allure
from playwright.sync_api import expect
from base.base_page import BasePage
from config.url_config import Links
from config.selectors_config import PERSONAL_PAGE


class PersonalPage(BasePage):
    PAGE_URL: str = Links.PERSONAL_PAGE

    FIRST_NAME_INPUT: str = PERSONAL_PAGE["first_name_input"]
    LAST_NAME_INPUT: str = PERSONAL_PAGE["last_name_input"]
    MIDDLE_NAME_INPUT: str = PERSONAL_PAGE["middle_name_input"]
    EMPLOYEE_ID_INPUT: str = PERSONAL_PAGE["employee_id_input"]
    OTHER_ID_INPUT: str = PERSONAL_PAGE["other_id_input"]
    DRIVERS_LICENSE_NUMBER_INPUT: str = PERSONAL_PAGE["drivers_license_number_input"]
    LICENSE_EXPIRY_DATE_ICON: str = PERSONAL_PAGE["license_expiry_date_icon"]
    NATIONALITY_ICON: str = PERSONAL_PAGE["nationality_icon"]
    MARITAL_STATUS_ICON: str = PERSONAL_PAGE["marital_status_icon"]
    DATE_OF_BIRTH_ICON: str = PERSONAL_PAGE["date_of_birth_icon"]
    GENDER_RADIO: str = PERSONAL_PAGE["gender_radio"]
    SAVE_BUTTON: str = PERSONAL_PAGE["save_button"]
    SPINNER: str = PERSONAL_PAGE["loading_spinner"]

    @allure.step("Update first name to '{new_name}'")
    def update_first_name(self, new_name: str) -> None:
        self.fill_field(self.FIRST_NAME_INPUT, new_name)

    @allure.step("Update last name to '{new_name}'")
    def update_last_name(self, new_name: str) -> None:
        self.fill_field(self.LAST_NAME_INPUT, new_name)

    @allure.step("Update middle_name to '{new_name}'")
    def update_middle_name(self, new_name: str) -> None:
        self.fill_field(self.MIDDLE_NAME_INPUT, new_name)

    @allure.step("Click 'Save' button")
    def click_save_button(self) -> None:
        self.page.locator(self.SAVE_BUTTON).click()
        self.wait_for_element(self.SPINNER, state="hidden")

    @allure.step("Verify first name is updated to '{expected_name}'")
    def verify_first_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator(self.FIRST_NAME_INPUT)).to_have_value(expected_name)

    @allure.step("Verify last name is updated to '{expected_name}'")
    def verify_last_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator(self.LAST_NAME_INPUT)).to_have_value(expected_name)

    @allure.step("Verify middle_name is updated to '{expected_name}'")
    def verify_middle_name_is_updated(self, expected_name: str) -> None:
        expect(self.page.locator(self.MIDDLE_NAME_INPUT)).to_have_value(expected_name)
