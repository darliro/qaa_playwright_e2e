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

    DRIVERS_LICENSE_NUMBER_INPUT = (
        '//label[text()="Driver\'s License Number"]/following::input[1]'
    )
    LICENSE_EXPIRY_DATE_INPUT = "(//input[@placeholder='yyyy-dd-mm'])[1]"
    TODAY_DATEPICKER = "div.oxd-date-input-link.--today"

    NATIONALITY_DROPDOWN_BUTTON = "(//i[contains(@class, 'oxd-select-text--arrow')])[1]"
    SECOND_OPTION_IN_NATIONALITY_LIST = "(//div[@role='option'])[2]"
    SELECTED_NATIONALITY_TEXT = "(//div[@class='oxd-select-text-input'])[1]"

    MARITAL_STATUS_DROPDOWN_BUTTON = (
        "(//i[contains(@class, 'oxd-select-text--arrow')])[2]"
    )
    SECOND_OPTION_IN_MARITAL_STATUS_LIST = "(//div[@role='option'])[2]"
    SELECTED_MARITAL_STATUS_TEXT = "(//div[@class='oxd-select-text-input'])[2]"

    DATE_OF_BIRTH_DATE_INPUT = "(//input[@placeholder='yyyy-dd-mm'])[2]"
    GENDER_RADIOBUTTON = "(//span[contains(@class, 'oxd-radio-input')])[2]"

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

    @allure.step("Update Driver's License Number to '{new_drivers_license_number}'")
    def update_drivers_license_number(self, new_drivers_license_number: str) -> None:
        self.fill_field(self.DRIVERS_LICENSE_NUMBER_INPUT, new_drivers_license_number)

    @allure.step("Set expiry date to today")
    def set_expiry_date_to_today(self) -> None:
        self.click_element(self.LICENSE_EXPIRY_DATE_INPUT)
        self.select_today_date()

    @allure.step("Select 'Today' in date picker")
    def select_today_date(self) -> None:
        self.click_element(self.TODAY_DATEPICKER)

    @allure.step("Update nationality to the second option in the list")
    def update_nationality_to_second_option(self) -> None:
        self.click_element(self.NATIONALITY_DROPDOWN_BUTTON)
        self.click_element(self.SECOND_OPTION_IN_NATIONALITY_LIST)

    @allure.step("Update marital status to the second option in the list")
    def update_marital_status_to_second_option(self) -> None:
        self.click_element(self.MARITAL_STATUS_DROPDOWN_BUTTON)
        self.click_element(self.SECOND_OPTION_IN_MARITAL_STATUS_LIST)

    @allure.step("Set date of birth to today")
    def set_date_of_birth_to_today(self) -> None:
        self.click_element(self.DATE_OF_BIRTH_DATE_INPUT)
        self.select_today_date()

    @allure.step("Update gender to the second option in the list")
    def update_gender_to_second_option(self) -> None:
        self.click_element(self.GENDER_RADIOBUTTON)

    @allure.step("Click 'Save' button")
    def click_save_button(self) -> None:
        self.click_element(self.SAVE_BUTTON)
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

    @allure.step(
        "Verify driver's license number is updated to '{expected_drivers_license_number}'"
    )
    def verify_drivers_license_number_is_updated(
        self, expected_drivers_license_number: str
    ) -> None:
        self.verify_field_value(
            self.DRIVERS_LICENSE_NUMBER_INPUT, expected_drivers_license_number
        )

    @allure.step("Verify license expiry date is updated to '{expected_expiry_date}'")
    def verify_license_expiry_date_is_updated(self, expected_expiry_date: str) -> None:
        self.verify_field_value(self.LICENSE_EXPIRY_DATE_INPUT, expected_expiry_date)

    @allure.step("Verify selected nationality is '{expected_value}'")
    def verify_nationality_is_updated(self, expected_value: str) -> None:
        self.verify_dropdown_value(self.SELECTED_NATIONALITY_TEXT, expected_value)

    @allure.step("Verify selected marital status is '{expected_value}'")
    def verify_marital_status_is_updated(self, expected_value: str) -> None:
        self.verify_dropdown_value(self.SELECTED_MARITAL_STATUS_TEXT, expected_value)

    @allure.step("Verify date of birth is updated to '{expected_date_of_birth}'")
    def verify_date_of_birth_is_updated(self, expected_date_of_birth: str) -> None:
        self.verify_field_value(self.DATE_OF_BIRTH_DATE_INPUT, expected_date_of_birth)

    @allure.step("Verify gender is updated to '{expected_gender}'")
    def verify_gender_is_updated(self, expected_gender: str) -> None:
        if expected_gender.lower() == "female":
            self.verify_radio_selected(self.GENDER_RADIOBUTTON)
