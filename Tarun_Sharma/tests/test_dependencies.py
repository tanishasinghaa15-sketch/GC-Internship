import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestDependencies(unittest.TestCase):

    def test_selenium_setup(self):
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            
            driver.get("https://www.python.org")
            time.sleep(random.uniform(2, 4))   
            
            ele = driver.find_element(By.CLASS_NAME, "menu")
            link = ele.find_element(By.TAG_NAME, "a")
            
            self.assertTrue(link.text, "No text found in the link element")
            self.assertTrue(link.get_attribute("href").startswith("http"), "Invalid link")

        except Exception as e:
            self.fail(f"Test failed due to error: {e}")

        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()
