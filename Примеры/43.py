import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.python.org/3/')
soup = BeautifulSoup(response.text, features='html.parser')

tag_div = soup.find('div', attrs={'class': 'sphinxsidebarwrapper'})
tag_ul = tag_div.find('ul')
tags_a = tag_ul.find_all('a')
for tag_a in tags_a:
    print(tag_a.text, tag_a['href'])
