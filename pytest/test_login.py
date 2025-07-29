import pytest
import allure
import time
from playwright.sync_api import sync_playwright, Page

# Variables
class TestLocators:
    username = 'xpath=//*[@id="username"]'
    password = 'xpath=//*[@id="password"]'
    submit_button = 'xpath=//*[@id="submit"]'
    logout_button = 'xpath=//*[@id="loop-container"]/div/article/div[2]/div/div/div/a'

# 封裝 fixture：避免每個測試重複寫啟動/關閉瀏覽器
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        yield page
        browser.close()

def test_positive_login(page : Page):
    """Test case for successful login with correct credentials."""
    with allure.step("Step 1: Open login page and verify URL"):
        page.goto("https://practicetestautomation.com/practice-test-login/")
        assert "practice-test-login" in page.url, "Page did not load correctly"

    with allure.step("Step 2: Login with correct username and password"):
        page.fill(TestLocators.username, "student")
        page.fill(TestLocators.password, "Password123")
        page.click(TestLocators.submit_button)

    with allure.step("Step 3: Verify successful login by checking URL"):
        page.wait_for_url("https://practicetestautomation.com/logged-in-successfully/")
        assert "logged-in-successfully" in page.url, "Login was not successful"

    with allure.step("Step 4: Verify new page contains expected text"):
        page.wait_for_selector(TestLocators.logout_button)
        page.get_by_text("Congratulations student. You successfully logged in!").is_visible()
        assert page.get_by_text("Congratulations student. You successfully logged in!").is_visible(), "Expected text not found on the page"
    
    with allure.step("Step 5: Verify Log out button is displayed"):
        page.is_visible(TestLocators.logout_button)
        assert page.is_visible(TestLocators.logout_button), "Log out button is not visible"


def test_negative_username_login(page : Page):
    """Test case for login with an invalid username."""
    with allure.step("Step 1: Open login page and verify URL"):
        page.goto("https://practicetestautomation.com/practice-test-login/")
        assert "practice-test-login" in page.url, "Page did not load correctly"

    with allure.step("Step 2: Login with incorrect username and correct password"):
        page.fill(TestLocators.username, "wronguser")
        page.fill(TestLocators.password, "Password123")
        page.click(TestLocators.submit_button)

    with allure.step("Step 3: Verify error message is displayed"):
        error_username_message = 'xpath=//*[@id="error"]'
        page.is_visible(error_username_message)
        assert page.is_visible(error_username_message), "Error message for invalid username not found"


def test_negative_password_login(page : Page):
    """Test case for login with an invalid password."""
    with allure.step("Step 1: Open login page and verify URL"):
        page.goto("https://practicetestautomation.com/practice-test-login/")
        assert "practice-test-login" in page.url, "Page did not load correctly"

    with allure.step("Step 2: Login with correct username and incorrect password"):
        page.fill(TestLocators.username, "student")
        page.fill(TestLocators.password, "wrongpassword")
        page.click(TestLocators.submit_button)

    with allure.step("Step 3: Verify error message is displayed"):
        error_password_message = 'xpath=//*[@id="error"]'
        page.is_visible(error_password_message)
        assert page.is_visible(error_password_message), "Error message for invalid username not found"