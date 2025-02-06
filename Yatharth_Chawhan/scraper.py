import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Set up Chrome options
options = Options()
options.add_argument("--user-data-dir=C:/Users/YC/AppData/Local/Google/Chrome/User Data")  # Your Chrome user data path
options.add_argument("--profile-directory=Profile 1")  # Specific Chrome profile (if you have more than one)
options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("--no-sandbox")  # Disable sandboxing in headless mode
options.add_argument("--start-maximized")  # Maximize window on startup

# Specify the location of the Chrome binary explicitly
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome executable

# Initialize the driver using undetected-chromedriver
driver = uc.Chrome(options=options)

# Open Google
driver.get("https://www.google.com")

# Find search bar, enter query, and submit
search_box = driver.find_element(By.NAME, "q")  # Locate search bar
time.sleep(random.uniform(1, 3)) 
action = ActionChains(driver)
action.move_by_offset(random.randint(100, 300), random.randint(100, 300)).perform()
time.sleep(random.uniform(1, 2))
action.move_to_element(search_box).perform()  # Move the mouse to the search box

# Typing into the search box
search_box.send_keys("Selenium Python")
time.sleep(1)  # Human-like delay
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)  # Simple wait (better to use WebDriverWait)

# Extract search result titles and links
results = driver.find_elements(By.CSS_SELECTOR, "h3")

for result in results:
    print(result.text)  # Print result title

# Close browser
driver.quit()
