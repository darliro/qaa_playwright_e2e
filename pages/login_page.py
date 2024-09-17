import allure
from base.base_page import BasePage
from config.url_config import Links
from config.selectors_config import LOGIN_PAGE


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD: str = LOGIN_PAGE["username_input"]
    PASSWORD_FIELD: str = LOGIN_PAGE["password_input"]
    SUBMIT_BUTTON: str = LOGIN_PAGE["submit_button"]

    @allure.step("Enter login: {login}")
    def enter_login(self, login: str) -> None:
        self.page.locator(self.USERNAME_FIELD).fill(login)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.page.locator(self.PASSWORD_FIELD).fill(password)

    @allure.step("Click submit button")
    def click_submit_button(self) -> None:
        self.page.locator(self.SUBMIT_BUTTON).click()

    @allure.step("Verify 'Dashboard' page is loaded")
    def verify_dashboard_page_loaded(self) -> None:
        self.verify_url(expected_url=Links.DASHBOARD_PAGE)
