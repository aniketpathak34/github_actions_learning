import requests
from bs4 import BeautifulSoup

# Define the URL to scrape (Example: GitHub trending repositories)
url = "https://github.com/trending"

# Send GET request to the website
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad HTTP status codes

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the trending repositories
repositories = soup.find_all('h1', {'class': 'h3 lh-condensed'})

# Print the repository names and their URLs
for repo in repositories:
    repo_name = repo.get_text(strip=True)
    repo_url = 'https://github.com' + repo.find('a')['href']
    print(f"{repo_name}: {repo_url}")
