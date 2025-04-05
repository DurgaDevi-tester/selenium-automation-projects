from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Firefox(service=Service("/snap/bin/geckodriver"))

try:
    # Open the target page
    driver.get("https://demoqa.com/browser-windows")
    
    # Click on the 'New Tab' button
    new_tab_button = driver.find_element(By.ID, "tabButton")
    new_tab_button.click()

    # Wait for the new tab to load
    time.sleep(3)

    # Get all window handles and switch to the new tab
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[1])

    # Extract and print the heading text from the new tab
    new_tab_text = driver.find_element(By.ID, "sampleHeading").text
    print("Text from new tab:", new_tab_text)

    # Switch back to the original tab
    driver.switch_to.window(all_handles[0])

finally:
    # Close the browser
    driver.quit()
