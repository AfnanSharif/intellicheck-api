import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"  # Replace with the desired URL

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find specific elements (e.g., titles, links, paragraphs)
titles = soup.find_all('h2')
links = soup.find_all('a')
paragraphs = soup.find_all('p')

# Extract information from elements
for title in titles:
    print(title.text)

for link in links:
    print(link['href'])

for paragraph in paragraphs:
    print(paragraph.text)