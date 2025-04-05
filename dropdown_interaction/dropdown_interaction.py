from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
import time

# Set up WebDriver
driver = webdriver.Firefox(service = Service("/snap/bin/geckodriver"))

try:
    # Step 1: Navigate to the DemoQA page
    driver.get("https://demoqa.com/select-menu")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Step 2: Handle the single select dropdown
    single_dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
    single_dropdown.select_by_visible_text("Green")
    print("Single dropdown: Selected 'Green'")
    time.sleep(2)

    # Step 3: Handle the multi-select dropdown
    driver.execute_script("window.scrollTo(0, 300)")  # Scroll down for visibility
    multi_dropdown = Select(driver.find_element(By.ID, "cars"))

    # Select multiple options
    multi_dropdown.select_by_visible_text("Volvo")
    multi_dropdown.select_by_value("audi")
    print("Multi-select dropdown: Selected 'Volvo' and 'Audi'")
    time.sleep(2)

    # Optional: Deselect options (only works for multi-select)
    multi_dropdown.deselect_by_visible_text("Volvo")
    print("Multi-select dropdown: Deselected 'Volvo'")
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Step 4: Quit the driver
    driver.quit()