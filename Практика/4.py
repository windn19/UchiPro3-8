import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://ru.wikipedia.org'
URL = '/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%AF%D0%B7%D1%8B%D0%BA%D0%B8_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

response = requests.get(f'{BASE_URL}{URL}')
soup = BeautifulSoup(response.text, features='html.parser')

tag_div = soup.find('div', attrs={'class': 'mw-category'})
tags_a = tag_div.find_all('a')
for tag_a in tags_a[30:40]:
    detail_url = f'{BASE_URL}{tag_a["href"]}'
    detail_response = requests.get(detail_url)
    detail_soup = BeautifulSoup(detail_response.text, features='html.parser')
    content = detail_soup.find('div', attrs={'id': 'mw-content-text'})
    description = content.find('p')
    print(description.text.strip())
