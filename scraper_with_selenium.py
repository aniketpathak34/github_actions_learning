from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional)
chrome_options.add_argument('--no-sandbox')  # Disables the sandbox security model (necessary in some environments)

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Define the URL to scrape
url = "https://www.example.com"

# Open the website
driver.get(url)

# Perform actions or scrape data
element = driver.find_element(By.TAG_NAME, 'h1')
print(element.text)

# Close the driver
driver.quit()
