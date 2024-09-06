import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):
    @allure.title("Change Profile Name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self, random_first_name):
        """
        Verifies that the user's profile name can be changed and saved.
        """
        with allure.step("Login and navigate to dashboard"):
            self.login_page.open()
            self.login_page.enter_login(self.data.LOGIN)
            self.login_page.enter_password(self.data.PASSWORD)
            self.login_page.click_submit_button()
            self.dashboard_page.verify_url()

        with allure.step("Navigate to personal info page"):
            self.dashboard_page.click_my_info_link()
            self.personal_page.verify_url()

        with allure.step(f"Change profile name to '{random_first_name}'"):
            self.personal_page.change_name(random_first_name)
            self.personal_page.save_changes()

        with allure.step("Verify changes and take a screenshot"):
            self.personal_page.verify_changes()
            self.personal_page.make_screenshot("Profile name change success")
