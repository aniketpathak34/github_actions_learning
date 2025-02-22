import requests
from bs4 import BeautifulSoup

# Define the URL to scrape (Example: GitHub trending repositories)
url = "https://github.com/trending"

try:
    # Send GET request to the website
    print(f"Sending request to {url}...")
    response = requests.get(url)
    
    # Raise an error for bad HTTP status codes
    response.raise_for_status()  
    print(f"Request successful! Status code: {response.status_code}")
    
    # Parse the HTML content
    print("Parsing the HTML content...")
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the trending repositories
    print("Finding trending repositories...")
    repositories = soup.find_all('h1', {'class': 'h3 lh-condensed'})

    # Check if repositories were found
    if not repositories:
        print("No repositories found. Check the scraping logic or the website structure.")
    else:
        # Print the repository names and their URLs
        print("Trending repositories:")
        for repo in repositories:
            repo_name = repo.get_text(strip=True)
            repo_url = 'https://github.com' + repo.find('a')['href']
            print(f"{repo_name}: {repo_url}")
    
    print("Scraper finished successfully!")

except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
