import requests

params = {'first': 1, 'second': 'two'}
url = 'https://example.com'

response = requests.get(url=url, params=params)
print(response.url)
print(response.text)
