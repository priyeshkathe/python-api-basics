# Exercise 3: Count how many comments are on post ID 1
#             URL: https://jsonplaceholder.typicode.com/posts/1/comments

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1/comments'

response = requests.get(url)

if response.status_code == 200 :
    print("Data Found.....")
    comments = response.json()
    print("Total Comments in post is : ",len(comments))
else:
    print(response.status_code,"Error Data Not Found")
