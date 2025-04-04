from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Firefox driver
driver = webdriver.Firefox(service=Service("/snap/bin/geckodriver"))

# Open DuckDuckGo
driver.get("https://www.duckduckgo.com")

# Search for "selenium python tutorial"
search_box = driver.find_element(By.ID, 'searchbox_input')
search_query = "selenium python tutorial"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for search result links to load
try:
    result_links = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'eVNpHGjtxRBq_gLOfGDr')]"))
    )

    # Extract and print the first 5 URLs
    with open("duckduckgo_results.txt", "w") as f:
        for idx, link in enumerate(result_links[:5], start=1):
            url = link.get_attribute("href")
            print(f"{idx}. {url}")
            f.write(f"{idx}. {url}\n")

except Exception as e:
    print("Error locating search results:", e)

# Close the browser
driver.quit()