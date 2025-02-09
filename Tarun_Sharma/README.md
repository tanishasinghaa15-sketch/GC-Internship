# Web Scraper Tool

# A scraping tool to automatically fetch results from the web

# Note: Tool is in development phase-

# Issue#\_1- Bypass bot detection

## Features

- Google search results are automatically fetched for a given query
- Results are saved in a JSON file
- Robust Tool: includes unit tests for core functionalities

### Prerequisites

- Python 3.x installed
- Google Chrome installed
- ChromeDriver (automatically managed)

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/Internships/GC-Internships/Tarun_Sharma.git
   cd Tarun_Sharma
   ```

2. Virtual Environment:

```sh
python -m venv venv
venv/Scripts/activate
```

3. Dependencies Installation:

   ```sh
   python -m venv venv
   venv/Scripts/activate  # windows
   pip install -r requirements.txt

   ```

4. Running the Scaping tool:
   ```sh
   python scraper.py
   ```
5. Testing the Tool:

```sh
python  -m unittest tests/test_dependencies.py
python -m unittest tests/test_scraper.py
```

<!--  or try python -m unittest discover -s tests
 -->
