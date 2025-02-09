import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scraper import scrape_google_search
from utils import save_results, load_results

class TestScraper(unittest.TestCase):
    
    def test_selenium_setup(self):
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.quit()
        except Exception as e:
            self.fail(f"Selenium WebDriver setup failed: {e}")
            
    def test_scrape_google_search(self):
        query = "Top universities in India"
        results = scrape_google_search(query)
        
        self.assertIsInstance(results, list, "Results should be a list")
        self.assertGreater(len(results), 0, "Results list should not be empty")
        
        first_result = results[0]
        self.assertIn("title", first_result, "Each result should have a title")
        self.assertIn("link", first_result, "Each result should have a link")
        self.assertIn("desc", first_result, "Each result should have a description")

    def test_save_and_load_results(self):
        test_output_data = [
            {"title": "Test Title", "link": "https://example.com", "desc": "Test Description"}
        ]
        filename = "test_results.json"
        
        save_results(test_output_data, filename)
        self.assertTrue(os.path.exists(filename), "JSON file should be created")

        loaded_test_data = load_results(filename)
        self.assertEqual(loaded_test_data, test_output_data, "Loaded data should match saved data")

        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
