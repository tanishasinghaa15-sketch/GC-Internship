import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from config import CHROME_OPTIONS  
from utils import save_results, load_results   

def get_driver():
 
    chrome_options = Options()
    for opt in CHROME_OPTIONS:
        chrome_options.add_argument(opt)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def scrape_google_search(query):
 
    driver = get_driver()
    search_url = f"https://www.google.com/search?q={query}"
    
    driver.get(search_url)
    time.sleep(random.uniform(2, 5))  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2, 5))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2, 5))
    results = []
   
    search_results = driver.find_elements(By.CLASS_NAME, "tF2Cxc")
    for result in search_results:
        try:
        
            title_element = result.find_element(By.TAG_NAME, "h3")
            link_element = result.find_element(By.TAG_NAME, "a")
            desc_element = result.find_element(By.CLASS_NAME, "VwiC3b")

            title = title_element.text if title_element else "No Title"
            link = link_element.get_attribute("href") if link_element else "No Link"
            desc = desc_element.text if desc_element else "No Description"

            results.append({"title": title, "link": link, "desc": desc})
        except Exception as e:
            print(f"Skipping result due to error: {e}")

    driver.quit()

    save_results(results, "results.json")
    return results

if __name__ == "__main__":
    query = "winter vacations in India"
    try:
        data = scrape_google_search(query)
    except Exception as e:
        print(f"Error: {e}")
        data = []
      # here we will get  the eror
    print(f"Total scraper results: {len(data)}")
    
    saved_data = load_results("results.json")  
    for item in data:
        print(f"Title: {item['title']}\nLink: {item['link']}\nSnippet: {item['desc']}\n")
