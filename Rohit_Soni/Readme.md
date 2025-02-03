# Google Search Results Scraper

This Python script automates the process of searching Google and extracting search results, including their titles and URLs. The results are saved into a CSV file for easy reference.

---

## Features
- **Automated Google Search**: Performs a search query on Google using Selenium WebDriver.
- **Scrapes Search Results**: Extracts the title and link of search results from the Google search page.
- **Saves to CSV**: Outputs the results into a neatly formatted CSV file.

---

## Requirements
1. Python 3.x
2. Google Chrome
3. ChromeDriver (compatible with your Chrome version)
4. Required Python libraries:
   - `selenium`
   - `csv`
   - `time`
   - `random`

Install Selenium using:
```bash
pip install selenium