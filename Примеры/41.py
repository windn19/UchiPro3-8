import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.python.org/3/')
soup = BeautifulSoup(response.text, features='html.parser')

print(soup.find('div', attrs={'class': 'sphinxsidebarwrapper'}))
