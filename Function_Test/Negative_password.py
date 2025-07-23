# Negative password test
# Open page
# Type username student into Username field
# Type password incorrectPassword into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your password is invalid!

from playwright.sync_api import sync_playwright

# Variables
username = 'xpath=//*[@id="username"]'
password = 'xpath=//*[@id="password"]'
submit_button = 'xpath=//*[@id="submit"]'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill(username, "student")
    page.fill(password, "incorrectPassword")
    page.click(submit_button)
    # Verify error message text
    error_msg = 'xpath=//*[@id="error"]'
    page.is_visible(error_msg)
    page_content = page.content()
    if 'Your password is invalid!' in page_content :
        print("Negative password test passed: Error message displayed correctly")
    else:
        print("Error message not displayed as expected")  
    browser.close()
