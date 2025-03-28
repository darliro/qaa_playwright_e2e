import pytest
import allure
from base.base_test import BaseTest


class TestProfileFeature(BaseTest):
    @allure.title("Change Profile Details")
    @pytest.mark.regression
    def test_personal_details_change(self, data_generator):
        first_name = data_generator("first_name")
        last_name = data_generator("last_name")
        middle_name = data_generator("middle_name")
        employee_id = data_generator("id")
        other_id = data_generator("id")
        drivers_license_number = data_generator("id")
        expiry_date = data_generator("date")
        nationality = data_generator("nationality")
        marital_status = data_generator("marital_status")
        date_of_birth = data_generator("date")
        gender = data_generator("gender")

        with allure.step("Login and navigate to dashboard"):
            self.login_page.open_page()
            self.login_page.enter_login(self.data.LOGIN)
            self.login_page.enter_password(self.data.PASSWORD)
            self.login_page.click_submit_button()
            self.dashboard_page.open_page()

        with allure.step("Navigate to personal info"):
            self.dashboard_page.click_my_info_link()
            self.personal_details_page.open_page()

        with allure.step("Update personal details information"):
            self.personal_details_page.update_first_name(first_name)
            self.personal_details_page.update_last_name(last_name)
            self.personal_details_page.update_middle_name(middle_name)
            self.personal_details_page.update_employee_id(employee_id)
            self.personal_details_page.update_other_id(other_id)
            self.personal_details_page.update_drivers_license_number(
                drivers_license_number
            )
            self.personal_details_page.set_expiry_date_to_today()
            self.personal_details_page.update_nationality_to_second_option()
            self.personal_details_page.update_marital_status_to_second_option()
            self.personal_details_page.set_date_of_birth_to_today()
            self.personal_details_page.update_gender_to_second_option()
            self.personal_details_page.click_save_button()

        with allure.step("Verify personal details update"):
            self.personal_details_page.verify_first_name_is_updated(first_name)
            self.personal_details_page.verify_last_name_is_updated(last_name)
            self.personal_details_page.verify_middle_name_is_updated(middle_name)
            self.personal_details_page.verify_employee_id_is_updated(employee_id)
            self.personal_details_page.verify_other_id_is_updated(other_id)
            self.personal_details_page.verify_drivers_license_number_is_updated(
                drivers_license_number
            )
            self.personal_details_page.verify_license_expiry_date_is_updated(
                expiry_date
            )
            self.personal_details_page.verify_nationality_is_updated(nationality)
            self.personal_details_page.verify_marital_status_is_updated(marital_status)
            self.personal_details_page.verify_date_of_birth_is_updated(date_of_birth)
            self.personal_details_page.verify_gender_is_updated(gender)

        with allure.step("Capture screenshot after update"):
            self.personal_details_page.make_screenshot("Profile_info_change_success")
