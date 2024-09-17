import allure
from base.base_page import BasePage
from config.url_config import Links
from config.selectors_config import DASHBOARD_PAGE


class DashboardPage(BasePage):
    PAGE_URL: str = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON: str = DASHBOARD_PAGE["my_info_button"]

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self) -> None:
        self.page.locator(self.MY_INFO_BUTTON).click()

    @allure.step("Verify 'My Info' page is loaded")
    def verify_my_info_page_loaded(self) -> None:
        self.verify_url(expected_url=Links.PERSONAL_PAGE)
