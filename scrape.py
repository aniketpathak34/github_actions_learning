import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to run headlessly
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Needed for some environments (like CI)
chrome_options.add_argument("--disable-dev-shm-usage")  # Needed for some environments (like CI)

# Install the correct version of chromedriver using webdriver-manager
service = Service(ChromeDriverManager().install())  # This installs the correct version

# Set up the WebDriver
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
