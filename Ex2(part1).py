# Exercise 2: Fetch a list of all users

import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

print(f'Status Code : {response.status_code}')
print(response.json())