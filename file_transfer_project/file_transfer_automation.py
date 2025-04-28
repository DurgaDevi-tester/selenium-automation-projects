from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import os

# set directory
download_dir = "/home/sb/Downloads"

driver = webdriver.Firefox(service=Service("/snap/bin/geckodriver"))

try:
    #===FILE DOWNLOAD===#
    driver.get("https://demoqa.com/upload-download")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()
    time.sleep(2)
    print("File downloaded successfully.")

    #check if file exists
    files = [os.path.join(download_dir,f) for f in os.listdir(download_dir)]

    #Filter only files (ignore subdirs)
    files = [f for f in files if os.path.isfile(f)]

    #Sort files by modified time(latest first)
    latest_file = max(files, key=os.path.getmtime)

    print("Latest downloaded file:", latest_file)

    #==FILE UPLOAD==#
    driver.get("https://the-internet.herokuapp.com/upload")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#file-upload").send_keys(latest_file)
    driver.find_element(By.CSS_SELECTOR, "#file-submit").click()
    time.sleep(2)

    print("File uploaded succesfully.")

finally:
    driver.quit()