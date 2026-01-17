# Exercise 3: What happens if you fetch a post that doesn't exist?
#             Try: https://jsonplaceholder.typicode.com/posts/999

import requests

url = 'https://jsonplaceholder.typicode.com/posts/999'

response = requests.get(url)

print(f'Status Code : {response.status_code}')
print(response.json())