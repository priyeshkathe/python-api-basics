# Exercise 1: Add retry logic - if request fails, try again up to 3 times
#             Hint: Use a for loop and time.sleep() between retries

import requests
import time

def fetch_with_retry(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            print(f"Attempt {attempt}...")
            response = requests.get(url, timeout=5)
            response.raise_for_status()   
            return response.json()        

        except Exception as e:
            print("Request failed:", e)

            if attempt < retries:
                print("Retrying in 2 seconds...\n")
                time.sleep(2)
            else:
                print("All retries failed.")

    return None


url = "https://jsonplaceholder.typicode.com/posts/1"
data = fetch_with_retry(url)

if data:
    print("\nSuccess! Title:", data["title"])
else:
    print("\nCould not fetch data.")
