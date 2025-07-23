# Open page
# Click Add button
# Wait for the second row to load
# Type text into the second input field
# Push Save button using locator By.name(“Save”)
# Verify text saved

from playwright.sync_api import sync_playwright
import time

# Variables
add_btn = 'xpath=//*[@id="add_btn"]'
row2_input = 'xpath=//*[@id="row2"]/input'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 2560, "height": 1440})
    page.goto("https://practicetestautomation.com/practice-test-exceptions/")
    page.click(add_btn)
    page.wait_for_selector(row2_input)
    # Verify Row 2 input field is displayed
    page.fill(row2_input, "Pasta")
    save_btn = page.locator('[Name="Save"]:visible')
    save_btn.click()
    if page.get_by_text("Row 2 was saved").is_visible() :
        print("Test passed")
    else:
        print("Test failed")
    browser.close()