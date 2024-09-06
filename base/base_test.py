import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.webdriver import WebDriver
from config.data_config import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage


class BaseTest:
    """
    Initializes the base test configuration.
    """

    data: Data = None
    login_page: LoginPage = None
    dashboard_page: DashboardPage = None
    personal_page: PersonalPage = None

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request: FixtureRequest, driver: WebDriver) -> None:
        """
        Fixture for initializing base pages and data for tests.
        """
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
