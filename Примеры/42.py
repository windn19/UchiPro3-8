import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.python.org/3/')
soup = BeautifulSoup(response.text, features='html.parser')

tag_div = soup.find('div', attrs={'class': 'sphinxsidebarwrapper'})
print(tag_div.find('ul'))
