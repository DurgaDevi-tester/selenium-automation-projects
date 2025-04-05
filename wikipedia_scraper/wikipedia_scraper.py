from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the gecko driver service
driver = webdriver.Firefox(service=Service("/snap/bin/geckodriver"))

try:
    # Open Wikipedia
    driver.get("https://www.wikipedia.org")

    # Locate the search box
    search_box = driver.find_element(By.ID, "searchInput")
    search_query = "Python (programming language)"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)  # You can replace this with explicit waits if needed

    # Extract the page title
    page_title = driver.find_element(By.ID, "firstHeading").text
    print(f"Page Title: {page_title}")

    # Extract the first paragraph
    first_paragraph = driver.find_element(By.XPATH,"//p[not(@class)]").text
    print("\nFirst Paragraph:")
    print(first_paragraph)

    # Save the results to a text file
    with open("wikipedia_search_result.txt", "w") as file:
        file.write(f"Page Title: {page_title}\n\n")
        file.write("First Paragraph:\n")
        file.write(first_paragraph)

    print("\nResults saved to 'wikipedia_search_result.txt'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()