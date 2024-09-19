import pytest
import allure
from base.base_test import BaseTest


class TestProfileFeature(BaseTest):
    @allure.title("Change Profile Name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(
        self, page, random_first_name, random_last_name, random_middle_name
    ):
        with allure.step("Login and navigate to dashboard"):
            self.login_page.open_page()
            self.login_page.enter_login(self.data.LOGIN)
            self.login_page.enter_password(self.data.PASSWORD)
            self.login_page.click_submit_button()
            self.dashboard_page.open_page()

        with allure.step("Navigate to personal info"):
            self.dashboard_page.click_my_info_link()
            self.personal_page.open_page()

        with allure.step("Update profile information'"):
            self.personal_page.update_first_name(random_first_name)
            self.personal_page.update_last_name(random_last_name)
            self.personal_page.update_middle_name(random_middle_name)
            self.personal_page.click_save_button()

        with allure.step("Verify profile information update"):
            self.personal_page.verify_first_name_is_updated(random_first_name)
            self.personal_page.verify_last_name_is_updated(random_last_name)
            self.personal_page.verify_middle_name_is_updated(random_middle_name)

        with allure.step("Capture screenshot after update"):
            self.personal_page.make_screenshot("Profile_info_change_success")
