import requests

response = requests.get('https://www.example.com/')
print(response) # <Response [200]>
print(response.text)
