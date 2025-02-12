from fake_useragent import UserAgent

ua = UserAgent()
USER_AGENT = ua.random

CHROME_OPTIONS = [
    "--headless=new", "--disable-gpu", "--no-sandbox",
     f"user-agent={USER_AGENT}" ,
      "--disable-blink-features=AutomationControlled",
       "--disable-infobars",
       "--remote-debugging-port=9222",
    "--disable-dev-shm-usage",
]
