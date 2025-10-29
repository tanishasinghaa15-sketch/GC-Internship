# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Go to Google
driver.get("https://www.google.com")

# Find the search box
search_box = driver.find_element(By.NAME, "q")

# Type your search term
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(2)

# Scrape result titles
titles = driver.find_elements(By.TAG_NAME, "h3")

print("Top Google Search Results:\n")
for title in titles:
    print("-", title.text)

# Close the browser
driver.quit()Internship: 
## Oboarding Task: 
1. Fork this repo
2. Create a folder with your name containing a .py file that uses selenium to scrape google search results.
3. Create a pull request

## Training 1: 

We will be going through this quick 32 minute video that will help us learn the industry standards and practices when it comes to python coding.

This will help us better understand how to collobarate and be a part of a development team.

Click on the image below to get started.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/25P5apB4XWM/0.jpg)](https://www.youtube.com/watch?v=25P5apB4XWM)

----------------------------------------------------------------------------------------------------------------------------------------------------



## Resource 1: View this Course at your liesure. 

### MIT Missing Semester Parts 1-7

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/2sjqTHE0zok/0.jpg)](https://www.youtube.com/watch?v=2sjqTHE0zok)

----------------------------------------------------------------------------------------------------------------------------------------------------


