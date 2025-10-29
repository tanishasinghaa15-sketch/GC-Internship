from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Chrome driver initialize (auto handled by webdriver-manager)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 2: Open Google
driver.get("https://www.google.com")

# Step 3: Search for a query
search_box = driver.find_element(By.NAME, "q")
search_query = "Internship for students"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Step 4: Wait for page to load
time.sleep(3)

# Step 5: Collect top 10 search results
results = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf > a')

print(f"\n🔍 Google Search Results for: {search_query}\n")
for index, result in enumerate(results[:10], start=1):
    print(f"{index}. {result.get_attribute('href')}")

# Step 6: Close the browser
driver.quit()
