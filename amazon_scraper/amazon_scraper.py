from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Amazon and search for "laptop"
driver.get("https://www.amazon.in/")
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
driver.find_element(By.ID, "nav-search-submit-button").click()

# Wait for search results to load
time.sleep(3)

# Extract product names and prices
product_names = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
product_prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

# Ensure equal product count
num_products = min(len(product_names), len(product_prices))

# Save to CSV file
with open("amazon_products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product Name", "Price"])

    for i in range(min(5, num_products)):  # Limit to 5 products
        price = f"₹{product_prices[i].text}" if i < len(product_prices) else "Price Not Available"
        writer.writerow([product_names[i].text, price])
        print(f"{i+1}. {product_names[i].text}")
        print(f"   {price}")

# Close browser
driver.quit()
