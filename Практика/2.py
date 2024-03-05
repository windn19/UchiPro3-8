import requests
from bs4 import BeautifulSoup

response = requests.get('https://pypi.org/project/PyQt6/#history')
soup = BeautifulSoup(response.text, features='html.parser')

tags_div = soup.find_all('div', attrs={'class': 'release'})

for tag_div in tags_div:
    tag_a = tag_div.find('a')
    tags_p = tag_a.find_all('p')
    print(tags_p[0].text.strip(), tags_p[1].text.strip())