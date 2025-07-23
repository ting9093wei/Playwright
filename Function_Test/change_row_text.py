# Open page
# Clear input field
# Type text into the input field
# Verify text changed

from playwright.sync_api import sync_playwright
import time

# Variables
add_btn = '#add_btn'
row1_input = '#row1 > input'
row2_input = '#row2 > input'
edit_btn = '#edit_btn'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 2560, "height": 1440})
    page.goto("https://practicetestautomation.com/practice-test-exceptions/")
    page.click(edit_btn)
    # Type text into the input field
    page.fill(row1_input, "")
    page.fill(row1_input, "Pasta")
    save_btn = page.locator('[Name="Save"]:visible')
    save_btn.click()
    # Verify text changed
    value = page.get_attribute(row1_input, "value")
    if value == "Pasta":
        print("Test passed: Row 1 input changed to Pasta")
    else:
        print(f"Test failed: Row 1 input value is {value}")
    browser.close()
