import requests
from bs4 import BeautifulSoup

response = requests.get('https://peps.python.org/')
soup = BeautifulSoup(response.text, features='html.parser')
# print(soup.prettify())
section = soup.find('section', attrs={'id': 'numerical-index'})
# print(section)
tags_tr = section.find_all('tr')
print(len(tags_tr))