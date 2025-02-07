from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from typing import List, Dict
import time
import logging

class StealthyGoogleScraper:
    """A class for performing stealth Google searches that avoid detection."""
    
    def __init__(self, timeout: int = 10):
        """
        Initialize the scraper with custom Chrome options.
        
        Args:
            timeout (int): Wait timeout in seconds for page elements
        """
        self.timeout = timeout
        self.driver = None
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging for the scraper."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def _configure_chrome_options(self) -> webdriver.ChromeOptions:
        """
        Configure Chrome options for stealth operation.
        
        Returns:
            ChromeOptions: Configured options object
        """
        options = webdriver.ChromeOptions()
        
        # Basic Chrome settings
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        
        # Stealth settings
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # Realistic user agent
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36")
        
        return options
    
    def _inject_stealth_scripts(self):
        """Inject scripts to bypass automation detection."""
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
                
                // Additional stealth
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['en-US', 'en']
                });
                
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5]
                });
            """
        })
    
    def _handle_cookie_consent(self):
        """Handle Google's cookie consent popup if present."""
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='L2AGLb']"))
            )
            cookie_button.click()
            time.sleep(1)
        except TimeoutException:
            self.logger.info("No cookie consent popup found")
    
    def _type_humanly(self, element, text: str):
        """
        Type text with random delays to simulate human typing.
        
        Args:
            element: WebElement to type into
            text (str): Text to type
        """
        for char in text:
            element.send_keys(char)
            # Random delay between 0.1 and 0.3 seconds
            time.sleep(0.1 + time.random() * 0.2)
    
    def search(self, query: str) -> List[Dict[str, str]]:
        """
        Perform a stealth Google search.
        
        Args:
            query (str): Search query
            
        Returns:
            List[Dict[str, str]]: List of search results with titles and URLs
            
        Raises:
            Exception: If search fails
        """
        try:
            # Initialize driver with stealth options
            self.driver = webdriver.Chrome(options=self._configure_chrome_options())
            self._inject_stealth_scripts()
            
            # Navigate to Google
            self.logger.info(f"Searching for: {query}")
            self.driver.get("https://www.google.com")
            
            # Handle cookie popup
            self._handle_cookie_consent()
            
            # Find and fill search box
            search_box = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            
            # Type query with human-like delays
            self._type_humanly(search_box, query)
            time.sleep(0.5)  # Small pause before hitting enter
            search_box.send_keys(Keys.RETURN)
            
            # Wait for results
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
            
            # Let the page fully load
            time.sleep(2)
            
            # Extract results
            results = []
            search_results = self.driver.find_elements(By.CSS_SELECTOR, "div.g")
            
            for result in search_results:
                try:
                    title = result.find_element(By.CSS_SELECTOR, "h3").text
                    link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                    
                    if title and link:
                        results.append({
                            "title": title,
                            "url": link
                        })
                except NoSuchElementException:
                    continue
                
            self.logger.info(f"Found {len(results)} results")
            return results
            
        except Exception as e:
            self.logger.error(f"Search failed: {str(e)}")
            raise
        
        finally:
            if self.driver:
                self.driver.quit()

def main():
    """Main function to demonstrate usage."""
    scraper = StealthyGoogleScraper()
    search_query = "Agney Nalapat"
    
    try:
        results = scraper.search(search_query)
        
        print(f"\nSearch results for: {search_query}\n")
        for idx, result in enumerate(results, 1):
            print(f"{idx}. {result['title']}")
            print(f"   {result['url']}\n")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
