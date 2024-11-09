import allure
from base.base_page import BasePage
from config.url_config import Links


class ContactDetailsPage(BasePage):
    PAGE_URL = Links.CONTACTS_DETAILS_PAGE

    STREET_1_INPUT = "//label[text()='Street 1']/following::input[1]"
    STREET_2_INPUT = "//label[text()='Street 2']/following::input[1]"
    CITY_INPUT = "//label[text()='City']/following::input[1]"

    SAVE_BUTTON = "//button[@type='submit']"
    LOADING_SPINNER = ".oxd-loading-spinner"

    @allure.step("Update street_1 to '{new_street_1}'")
    def update_street_1(self, new_street_1: str) -> None:
        self.fill_field(self.STREET_1_INPUT, new_street_1)

    @allure.step("Update street_2 to '{new_street_2}'")
    def update_street_2(self, new_street_2: str) -> None:
        self.fill_field(self.STREET_2_INPUT, new_street_2)

    @allure.step("Update city to '{new_city}'")
    def update_city(self, new_city: str) -> None:
        self.fill_field(self.CITY_INPUT, new_city)

    @allure.step("Click 'Save' button")
    def click_save_button(self) -> None:
        self.click_element(self.SAVE_BUTTON)
        self.wait_for_element(self.LOADING_SPINNER, state="hidden")

    @allure.step("Verify street_1 is updated to '{expected_street_1}'")
    def verify_street_1_is_updated(self, expected_name: str) -> None:
        self.verify_field_value(self.STREET_1_INPUT, expected_name)

    @allure.step("Verify street_2 is updated to '{expected_street_2}'")
    def verify_street_2_is_updated(self, expected_name: str) -> None:
        self.verify_field_value(self.STREET_2_INPUT, expected_name)

    @allure.step("Verify city is updated to '{expected_city}'")
    def verify_city_is_updated(self, expected_name: str) -> None:
        self.verify_field_value(self.CITY_INPUT, expected_name)
