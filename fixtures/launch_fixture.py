import pytest
from playwright.sync_api import Page, Browser, BrowserContext


@pytest.fixture(scope="session")
def browser_context(browser: Browser) -> BrowserContext:
    """Creates a new browser context, ensuring the browser runs in head mode."""
    context: BrowserContext = browser.new_context(no_viewport=True)
    yield context
    context.close()


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    """Opens a new page with specified viewport size and closes it after the test."""
    page: Page = context.new_page()
    page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.width, screen.height);")
    yield page
    page.close()
