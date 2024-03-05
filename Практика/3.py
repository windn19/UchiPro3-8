import requests
from bs4 import BeautifulSoup

URL = 'https://docs.python.org/3/library/functions.html'

response = requests.get(URL)
soup = BeautifulSoup(response.text, features='html.parser')
# print(type(soup))

tags_div = soup.find_all('div', attrs={'class': 'line'})

for tag_div in tags_div:
    tag_a = tag_div.find('a')
    if tag_a:
        print(tag_a.text, f'{URL}{tag_a["href"]}')
