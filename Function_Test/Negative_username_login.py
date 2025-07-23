# Negative username test
# Open page
# Type username incorrectUser into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your username is invalid!

from playwright.sync_api import sync_playwright

# Variables
username = 'xpath=//*[@id="username"]'
password = 'xpath=//*[@id="password"]'
submit_button = 'xpath=//*[@id="submit"]'
login_success_title = 'xpath=//*[@id="loop-container"]/div/article/div[1]/h1'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill(username, "incorrectUser")
    page.fill(password, "Password123")
    page.click(submit_button)
    # Verify error message is displayed
    error_message = 'xpath=//*[@id="error"]'
    page.is_visible(error_message)
    page_content = page.content()
    if 'Your username is invalid!' in page_content:
        print("Negative username test passed: Error message displayed correctly")
    else:
        print("Error message not displayed as expected")
    browser.close()
