from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_google_search(query, num_results=10):
    """
    Scrape Google search results for a given query.
    
    Args:
        query (str): The search query
        num_results (int): Number of results to scrape (default: 10)
    
    Returns:
        list: List of dictionaries containing title, link, and description
    """
    # Initialize Chrome driver (make sure chromedriver is in PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    results = []
    
    try:
        # Navigate to Google
        driver.get('https://www.google.com')
        
        # Wait for search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        
        # Enter search query and submit
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        
        # Find search result elements
        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        
        # Extract information from each result
        for result in search_results[:num_results]:
            try:
                # Extract title
                title_elem = result.find_element(By.CSS_SELECTOR, 'h3')
                title = title_elem.text
                
                # Extract link
                link_elem = result.find_element(By.CSS_SELECTOR, 'a')
                link = link_elem.get_attribute('href')
                
                # Extract description (snippet)
                try:
                    desc_elem = result.find_element(By.CSS_SELECTOR, 'div[data-sncf]')
                    description = desc_elem.text
                except:
                    description = 'No description available'
                
                # Add to results if valid
                if title and link:
                    results.append({
                        'title': title,
                        'link': link,
                        'description': description
                    })
                    
            except Exception as e:
                continue
        
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
    
    finally:
        # Close the browser
        driver.quit()
    
    return results

def main():
    """
    Main function to demonstrate the scraper.
    """
    # Example search query
    query = input("Enter search query: ")
    num_results = int(input("Number of results to fetch (default 10): ") or 10)
    
    print(f"\nSearching Google for: '{query}'\n")
    results = scrape_google_search(query, num_results)
    
    # Display results
    print(f"Found {len(results)} results:\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   URL: {result['link']}")
        print(f"   Description: {result['description']}")
        print()

if __name__ == "__main__":
    main()
