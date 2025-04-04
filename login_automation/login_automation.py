from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time

# Setup Firefox WebDriver
driver = webdriver.Firefox(service=Service("/snap/bin/geckodriver"))

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter username and password
driver.find_element(By.ID, 'username').send_keys("student")
driver.find_element(By.ID, 'password').send_keys("Password123")
driver.find_element(By.ID, 'submit').click()

# Check if login was successful
try:
    driver.find_element(By.XPATH, "//a[text()='Log out']")
    print("Login Successful")
except Exception as e:
    print("Login Failed:", e)

# Take screenshot
screenshot_path = "log_in.png"
driver.save_screenshot(screenshot_path)
Image.open(screenshot_path).show()

# Wait and close browser
time.sleep(2)
driver.quit()
