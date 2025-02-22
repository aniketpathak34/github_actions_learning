from selenium import webdriver

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get('http://example.com')

# Print the title of the page
print("Title of the page is:", driver.title)

# Close the browser
driver.quit()
