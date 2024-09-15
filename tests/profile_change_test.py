import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):
    @allure.title("Change Profile Name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self, page, random_first_name):
        with allure.step("Open login page"):
            self.login_page.open_page()

        with allure.step("Login and navigate to dashboard"):
            self.login_page.enter_login(self.data.LOGIN)
            self.login_page.enter_password(self.data.PASSWORD)
            self.login_page.click_submit_button()
            self.dashboard_page.open_page()

        with allure.step("Navigate to personal info page"):
            self.dashboard_page.click_my_info_link()
            self.personal_page.open_page()

        with allure.step(f"Update profile name to '{random_first_name}'"):
            self.personal_page.update_first_name(random_first_name)
            self.personal_page.click_save_button()

        with allure.step("Verify profile name update"):
            self.personal_page.verify_first_name_is_updated(random_first_name)
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="Profile_name_change_success",
                attachment_type=allure.attachment_type.PNG,
            )
