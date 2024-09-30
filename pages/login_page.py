import allure
from base.base_page import BasePage
from config.url_config import Links


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    @allure.step("Enter login: {login}")
    def enter_login(self, login: str) -> None:
        self.page.get_by_placeholder("Username").fill(login)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.page.get_by_placeholder("Password").fill(password)

    @allure.step("Click submit button")
    def click_submit_button(self) -> None:
        self.page.get_by_role("button", name="Login").click()

    @allure.step("Verify 'Dashboard' page is loaded")
    def verify_dashboard_page_loaded(self) -> None:
        self.verify_url(expected_url=Links.DASHBOARD_PAGE)
