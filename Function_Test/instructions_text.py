# Open page
# Find the instructions text element
# Push add button
# Verify instruction text element is no longer displayed

from playwright.sync_api import sync_playwright
import time

# Variables
add_btn = '#add_btn'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 2560, "height": 1440})
    page.goto("https://practicetestautomation.com/practice-test-exceptions/")
    # Find the instructions text element
    page.get_by_text('Push “Add” button to add another row').is_visible()
    # Push add button
    page.click(add_btn)
    # Verify instruction text element is no longer displayed
    if not page.get_by_text('Push “Add” button to add another row').is_visible():
        print("Test passed")
    else:
        print("Test failed")
    browser.close()