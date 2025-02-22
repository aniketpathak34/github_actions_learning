from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to run in headless mode and avoid user data conflicts
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandbox for CI environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage for Docker

# Specify a unique user data directory to avoid conflicts
chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to a webpage
driver.get("http://example.com")

# Print the title of the page
print("Title of the page is:", driver.title)

# Close the browser
driver.quit()
