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
    page.wait_for_selector(row1_input)
    # Type text into the input field
    page.fill(row1_input, "")
    page.fill(row2_input, "Pasta")
    row1_content = page.
    browser.close()
