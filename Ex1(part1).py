# Exercise 1: Change the URL to fetch post number 5
import requests

url = 'https://jsonplaceholder.typicode.com/posts/5'

response = requests.get(url)

print(f'URL :{url}')
print(f'Status Code : {response.status_code}')
print("Response Data ::::::")
print(response.json())