import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleScraper:
    def __init__(self, query, num_scrolls=3, result_limit=10, captcha_timeout=30):
        self.query = query
        self.num_scrolls = num_scrolls
        self.result_limit = result_limit
        self.captcha_timeout = captcha_timeout
        self.driver = webdriver.Chrome()
        self.results = []

    def scrape(self):
        print(f"Starting search for: {self.query}")
        self.driver.get(f"https://www.google.com/search?q={self.query}")

        start_time = time.time()
        
        while time.time() - start_time < self.captcha_timeout:
            try:
               
                captcha_element = self.driver.find_element(By.CSS_SELECTOR, "div.g-recaptcha")
                if captcha_element:
                    print("CAPTCHA detected, waiting for resolution...")
                    time.sleep(2)  
                else:
                    break
            except:
               
                break

        for _ in range(self.num_scrolls):
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.MjjYud"))
            )
            time.sleep(2)

        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.MjjYud")
        for element in elements:
            if len(self.results) >= self.result_limit:
                break
            try:
                title = element.find_element(By.CSS_SELECTOR, "h3").text
                url = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                description = element.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                self.results.append({"Title": title, "URL": url, "Description": description})
            except Exception as e:
                print(f"Skipping element due to error: {e}")

        print("Scraping complete.")
        self.driver.quit()

    def save_to_csv(self, file_name="google_results.csv"):
        df = pd.DataFrame(self.results)
        df.to_csv(file_name, index=False)
        print(f"Results saved to {file_name}")

if __name__ == "__main__":
    search_query = input("Enter search query: ")
    scraper = GoogleScraper(query=search_query, result_limit=5, captcha_timeout=30)  
    scraper.scrape()
    scraper.save_to_csv("search_results.csv")
