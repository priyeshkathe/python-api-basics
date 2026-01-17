# Exercise 1: Fetch user with ID 5 and print their phone number
#             URL: https://jsonplaceholder.typicode.com/users/5
#
# Exercise 2: Check if a resource exists before printing data
#             if response.status_code == 200:
#                 print(data)
#             else:
#                 print("Resource not found!")

import requests
url ='https://jsonplaceholder.typicode.com/users/5'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'Phone numbers : {data["phone"]}')
else :
    print(response.status_code,"Erro Data Nclearot found")
