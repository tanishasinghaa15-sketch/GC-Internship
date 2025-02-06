import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


options = Options()
options.add_argument("--user-data-dir=C:/Users/YC/AppData/Local/Google/Chrome/User Data")  
options.add_argument("--profile-directory=Profile 1")  
options.add_argument("--disable-gpu") 
options.add_argument("--no-sandbox") 
options.add_argument("--start-maximized")  


options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  


driver = uc.Chrome(options=options)


driver.get("https://www.google.com")


search_box = driver.find_element(By.NAME, "q")  
time.sleep(random.uniform(1, 3)) 
action = ActionChains(driver)
action.move_by_offset(random.randint(100, 300), random.randint(100, 300)).perform()
time.sleep(random.uniform(1, 2))
action.move_to_element(search_box).perform() 


search_box.send_keys("Selenium Python")
time.sleep(1) 
search_box.send_keys(Keys.RETURN)


time.sleep(3) 


results = driver.find_elements(By.CSS_SELECTOR, "h3")

for result in results:
    print(result.text) 


driver.quit()
