import requests
from bs4 import BeautifulSoup

cities = []

URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
response = requests.get(URL)
soup = BeautifulSoup(response.text, features='html.parser')

table = soup.find('table')
tr_tags = table.find_all('tr')

for tr_tag in tr_tags[1:]:
    td_tags = tr_tag.find_all('td')
    try:
        cities.append([td_tags[2].text, int(td_tags[5]['data-sort-value'])])
    except Exception as e:
        print(td_tags[5])
for city, population in sorted(cities, key=lambda x: -x[1]):
    print(f'Город: {city}, население: {population}')