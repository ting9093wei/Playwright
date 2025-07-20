from playwright.sync_api import sync_playwright

# Variables
username = 'xpath=//*[@id="username"]'
password = 'xpath=//*[@id="password"]'
submit_button = 'xpath=//*[@id="submit"]'
login_success_title = 'xpath=//*[@id="loop-container"]/div/article/div[1]/h1'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill(username, "student")
    page.fill(password, "Password123")
    page.click(submit_button)
    if page.is_visible(login_success_title):
        print("Login successful")
    else:
        print("Login failed")
    browser.close()
