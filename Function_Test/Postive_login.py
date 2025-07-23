# Positive LogIn test
# Open page
# Type username student into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Verify button Log out is displayed on the new page

from playwright.sync_api import sync_playwright

# Variables
username = 'xpath=//*[@id="username"]'
password = 'xpath=//*[@id="password"]'
submit_button = 'xpath=//*[@id="submit"]'
logout_button = 'xpath=//*[@id="loop-container"]/div/article/div[2]/div/div/div/a'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # Login with correct username and password
    page.fill(username, "student")
    page.fill(password, "Password123")
    page.click(submit_button)
    page.wait_for_url("https://practicetestautomation.com/logged-in-successfully/")
    page_content = page.content()
    # Verify new page contains expected text
    page.get_by_text("Congratulations,successfully logged in").is_visible()
    if page.is_visible(logout_button):
        page.click(logout_button)
        print("Logged out successfully")
    else:
        print("Log out button not visible, login may have failed")
    browser.close()
