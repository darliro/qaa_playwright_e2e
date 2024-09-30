import allure
from base.base_page import BasePage
from config.url_config import Links


class DashboardPage(BasePage):
    PAGE_URL: str = Links.DASHBOARD_PAGE

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self) -> None:
        self.page.get_by_text("My info").click()

    @allure.step("Verify 'My Info' page is loaded")
    def verify_my_info_page_loaded(self) -> None:
        self.verify_url(expected_url=Links.PERSONAL_PAGE)
