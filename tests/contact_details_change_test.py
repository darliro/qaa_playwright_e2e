import pytest
import allure
from base.base_test import BaseTest


class TestContactDetailsFeature(BaseTest):
    @allure.title("Change Contact Details")
    @pytest.mark.regression
    def test_contact_details_change(self, data_generator):
        street_1 = data_generator("street_1")
        street_2 = data_generator("street_2")
        city = data_generator("city")

        with allure.step("Login and navigate to dashboard"):
            self.login_page.open_page()
            self.login_page.enter_login(self.data.LOGIN)
            self.login_page.enter_password(self.data.PASSWORD)
            self.login_page.click_submit_button()
            self.dashboard_page.open_page()

        with allure.step("Navigate to contact details"):
            self.dashboard_page.click_my_info_link()
            self.contact_details_page.open_page()

        with allure.step("Update contact details information"):
            self.contact_details_page.update_street_1(street_1)
            self.contact_details_page.update_street_2(street_2)
            self.contact_details_page.update_city(city)
            self.contact_details_page.click_save_button()

        with allure.step("Verify contact details update"):
            self.contact_details_page.verify_street_1_is_updated(street_1)
            self.contact_details_page.verify_street_2_is_updated(street_2)
            self.contact_details_page.verify_city_is_updated(city)

        with allure.step("Capture screenshot after update"):
            self.contact_details_page.make_screenshot("Contact_info_change_success")
