import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

# Automatically install the correct version of Chromedriver
chromedriver_autoinstaller.install()

# Path to the Chrome binary (needed for headless Chrome)
chrome_binary_path = "/usr/bin/google-chrome-stable"

# Set up Chrome options to run headlessly
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Needed for some environments (like CI)
chrome_options.add_argument("--disable-dev-shm-usage")  # Needed for some environments (like CI)
chrome_options.binary_location = chrome_binary_path  # Explicitly set Chrome binary location

# Set up the WebDriver
service = Service("chromedriver")  # This should find the installed chromedriver automatically
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_website():
    try:
        # Open the website
        driver.get("https://example.com")
        time.sleep(3)  # Let the page load

        # Example of scraping content - modify this as needed
        element = driver.find_element(By.CSS_SELECTOR, "h1")
        print(f"Heading: {element.text}")

        # You can scrape more data here and print it
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_website()
