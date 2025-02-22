import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

# Automatically install ChromeDriver if it's not present
chromedriver_autoinstaller.install()

# Check if chromedriver is installed correctly
chromedriver_path = os.path.join(os.getcwd(), "chromedriver")
if not os.path.exists(chromedriver_path):
    print("Chromedriver is not installed correctly.")
    exit(1)

# Set up Chrome options to run headlessly
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# Set up the WebDriver
service = Service(chromedriver_path)
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
