# Open page
# Click Add button
# Verify Row 2 input field is displayed

from playwright.sync_api import sync_playwright

# Variables
add_button = 'xpath=//*[@id="add_btn"]'
row2_input = 'xpath=//*[@id="row2"]/input'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 2560, "height": 1440})
    page.goto("https://practicetestautomation.com/practice-test-exceptions/")
    page.click(add_button)
    page.wait_for_selector(row2_input)
    # Verify Row 2 input field is displayed
    if page.is_visible(row2_input) :
        print("Test passed: Row 2 input field is displayed")
    else:
        print("Test failed: Row 2 input field is not displayed")
    browser.close()
