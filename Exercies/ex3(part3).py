# Exercise 3: Add input validation (check if user_id is a number)

def get_user_info():
    user_id = input("Enter user ID : ")

    # Input validation
    if not user_id.isdigit():
        print("Invalid input")
        return

    print("Valid user ID:", user_id)

get_user_info()