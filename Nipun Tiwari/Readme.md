# Stealth Google Scraper

A Python-based web scraper that performs Google searches while avoiding detection. This scraper implements various stealth techniques to mimic human behavior and bypass automated detection systems.

## Features

- Stealth browser configuration to avoid detection
- Human-like typing behavior with random delays
- Comprehensive error handling and logging
- Cookie consent popup handling
- Clean result extraction with titles and URLs

## Prerequisites

- Python 3.7 or higher
- Chrome browser installed
- ChromeDriver (matching your Chrome version)

## Installation

1. First, create a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

2. Install required dependencies:
```bash
pip install selenium==4.15.2 webdriver-manager==4.0.1
```

## Project Structure

```
stealth_scraper/
│
├── stealth_scraper.py    # Main scraper implementation
└── README.md            # This file
```

## Usage

1. Basic usage:
```python
from stealth_scraper import StealthyGoogleScraper

# Create scraper instance
scraper = StealthyGoogleScraper()

# Perform search
try:
    results = scraper.search("your search query")
    
    # Print results
    for idx, result in enumerate(results, 1):
        print(f"{idx}. {result['title']}")
        print(f"   {result['url']}\n")
        
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

2. With custom timeout:
```python
# Create scraper with 15-second timeout
scraper = StealthyGoogleScraper(timeout=15)
```

## Running in Jupyter Notebook

For Jupyter Notebook environments, you may need additional configuration:

1. Install dependencies in your Jupyter environment:
```python
!pip install selenium==4.15.2 webdriver-manager==4.0.1
```

2. Use the same code as above, but you might want to add the headless option:
```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Add this for Jupyter web environments
```

## Troubleshooting

1. **ChromeDriver Issues**
   - Make sure Chrome browser is installed
   - Verify ChromeDriver version matches your Chrome version
   - Try updating both Chrome and ChromeDriver to latest versions

2. **Selenium Errors**
   - Update Selenium: `pip install --upgrade selenium`
   - Check if your Python version is compatible
   - Verify all dependencies are correctly installed

3. **Detection Issues**
   - Try reducing the search frequency
   - Ensure you're not making too many requests in a short time
   - Consider using proxies for high-volume scraping

## Common Issues and Solutions

1. "WebDriver not found":
```bash
# Install webdriver-manager
pip install webdriver-manager

# Then in your code:
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
```

2. Cookie consent popup not handled:
- The script automatically handles the common Google cookie consent popup
- If you encounter a different version, you might need to modify the `_handle_cookie_consent` method

## Best Practices

1. **Rate Limiting**
   - Add delays between searches
   - Don't make too many requests in succession
   - Consider implementing exponential backoff for retries

2. **Error Handling**
   - Always use try-except blocks
   - Implement proper cleanup in finally blocks
   - Log errors for debugging

3. **Resource Management**
   - Always close the browser after use
   - Use context managers when possible
   - Clean up resources in case of errors

## Limitations

- Only supports Google search
- May need adjustments for different regions/languages
- Not suitable for high-volume scraping without additional measures
- Subject to Google's terms of service and robot detection

## Legal Disclaimer

This tool is for educational purposes only. Before using it, make sure to:
1. Review and comply with Google's terms of service
2. Respect robots.txt
3. Implement appropriate rate limiting
4. Consider using official APIs for production use

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
