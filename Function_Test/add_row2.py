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
    # Wait for the second input field to be displayed
    if page.wait_for_selector(row2_input).is_visible():
        print("Test passed")
    else:
        print("Test failed")
    browser.close()
