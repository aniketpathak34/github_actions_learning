import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to run in headless mode and avoid user data conflicts
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandbox for CI environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage for Docker

# Specify a unique user data directory to avoid conflicts
chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")

# Set up WebDriver wait

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)

def trend_google_topics(driver, wait, url):
    """Fetch trending topics from Google Trends."""
    try:
        driver.get(url)
        
        # Wait for the elements to be loaded
        elements = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//tr//td//div[contains(@class, "mZ3RIc")]')
        ))

        # Collect the text of the trending topics
        trending_titles = [element.text for element in elements]
        
        # This is where you would normally save the data to a database
        # But for now, we're simply collecting and returning the data
        return trending_titles

    except Exception as e:
        print("Error fetching trends:", traceback.format_exc())

def fetch_g_search_headlines():
    """Main function to fetch Google search headlines."""
    try:
        url = "https://trends.google.com/trending?geo=IN"
        trending_titles = trend_google_topics(driver, wait, url)

        if trending_titles:
            # Normally, you'd save the trending titles here, for example in a database
            # Here we're just simulating by printing them
            print("Fetched the following trending titles:", trending_titles)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()

# Call the fetch_g_search_headlines function
fetch_g_search_headlines()
