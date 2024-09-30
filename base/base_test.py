import pytest
from config.data_config import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage
from playwright.sync_api import Page


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, request) -> None:
        """
        Runs automatically and initializes data and the necessary page objects.
        """
        self.data = Data()
        self.login_page = LoginPage(page)
        self.dashboard_page = DashboardPage(page)
        self.personal_page = PersonalPage(page)
