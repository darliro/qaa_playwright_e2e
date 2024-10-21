import allure
from base.base_page import BasePage
from config.url_config import Links


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    @allure.step("Enter login: {login}")
    def enter_login(self, login: str) -> None:
        self.fill_field("input[placeholder='Username']", login)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.fill_field("input[placeholder='Password']", password)

    @allure.step("Click submit button")
    def click_submit_button(self) -> None:
        self.click_element("button[type='submit']")

    @allure.step("Verify 'Dashboard' page is loaded")
    def verify_dashboard_page_loaded(self) -> None:
        self.verify_url(expected_url=Links.DASHBOARD_PAGE)
