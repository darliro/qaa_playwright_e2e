import allure
from base.base_page import BasePage
from config.url_config import Links


class DashboardPage(BasePage):
    PAGE_URL: str = Links.DASHBOARD_PAGE

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self) -> None:
        self.click_element("a:has-text('My info')")

    @allure.step("Verify 'My Info' page is loaded")
    def verify_my_info_page_loaded(self) -> None:
        self.verify_url(expected_url=Links.PERSONAL_PAGE)
