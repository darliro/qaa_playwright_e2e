import os
import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext


@pytest.fixture(scope="session")
def browser() -> Browser:
    """Launches the browser with headless or headed mode."""
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def browser_context(browser: Browser) -> BrowserContext:
    """Creates a new browser context with no viewport setting."""
    context: BrowserContext = browser.new_context(no_viewport=True)
    yield context
    context.close()


@pytest.fixture()
def page(browser_context: BrowserContext) -> Page:
    """Opens a new page with a specified size and closes it after the test."""
    page: Page = browser_context.new_page()
    page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.width, screen.height);")
    yield page
    page.close()
