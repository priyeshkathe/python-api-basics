# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false

import requests

def search_todos():
    status = input("Enter status (true / false): ").lower()

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": status}

    response = requests.get(url, params=params)
    todos = response.json()

    if todos:
        print(f"\nTodos with completed = {status}:\n")
        for todo in todos[:10]:  # show only first 10
            print("-", todo["title"])
    else:
        print("No todos found.")

search_todos()
