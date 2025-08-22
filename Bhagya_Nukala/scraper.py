import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class GoogleSearchScraper:
    def __init__(self, query, max_results=15, delay=2):
        self.query = query
        self.max_results = max_results
        self.delay = delay
        self.driver = None
        self.results = []

    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def search(self):
        self.driver.get("https://www.google.com/")
        box = self.driver.find_element(By.NAME, "q")
        box.send_keys(self.query)
        box.send_keys(Keys.RETURN)
        time.sleep(self.delay)

    def collect_results(self):
        cards = self.driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")
        for card in cards[:self.max_results]:
            try:
                title = card.find_element(By.TAG_NAME, "h3").text
                link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
                snippet = card.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                self.results.append({"Title": title, "Link": link, "Snippet": snippet})
            except Exception:
                continue

    def save_csv(self, filename="google_search.csv"):
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"[INFO] Results saved to {filename}")

    def run(self):
        self.start_driver()
        self.search()
        self.collect_results()
        self.driver.quit()
        self.save_csv()


if __name__ == "__main__":
    query = input("Enter your search query: ")
    scraper = GoogleSearchScraper(query=query, max_results=10, delay=2)
    scraper.run()
    print("[DONE] Scraping finished.")